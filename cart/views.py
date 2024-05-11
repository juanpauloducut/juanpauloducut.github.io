
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Sum

from item.models import Item
from .models import Cart


@login_required
def add_to_cart(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity', 1))
        price = item.price  # Fetching the price from the Item object
        
        # Create or update the cart item
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=item,  # Assuming 'product' is the correct field name in Cart model
            defaults={'quantity': quantity, 'price': price}
        )

        if not created:
            # If the item already exists in the cart, update the quantity
            cart_item.quantity = F('quantity') + quantity
            cart_item.save()

        messages.success(request, f"{quantity} {item.name}{'s' if quantity > 1 else ''} added to your cart.")

        return redirect("cart:cart_detail")

    else:
        # If the request method is not POST, handle the error or redirect appropriately
        messages.error(request, "Invalid request method.")
        return redirect("item:items")

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:cart_detail")

@login_required
def cart_detail(request):
    # Retrieve cart items associated with the current user
    cart_items = Cart.objects.filter(user=request.user)

    # Calculate total price using aggregation
    total_price = cart_items.aggregate(total_price=Sum(F('price') * F('quantity')))['total_price'] or Decimal(0)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/cart_detail.html', context)

def calculate_total_price(cart_items):
    total_price = 0
    for item in cart_items:
        total_price += item.quantity * item.price
    return total_price


@login_required
def checkout(request):
    if request.method == 'POST':
        # Process the form data if POST request
        # Assuming you have code here to process the form data

        # Redirect to a thank you page or some other page
        return render(request, 'cart/checkout.html')

    else:
        # If the request method is GET, render the checkout page
        user_cart = Cart.objects.filter(user=request.user)
        
        # Calculate total price
        total_price = calculate_total_price(user_cart)
        
        # Get the shipping address from the request.POST data
        shipping_address = request.POST.get('shipping_address', '')

        context = {
            'user_cart': user_cart,
            'total_price': total_price,
            'shipping_address': shipping_address,
        }
        return render(request, 'cart/checkout.html', context)
    
    
def place_order(request):
    if request.method == 'POST':
        # Process the form data if POST request
        # Assuming you have code here to process the form data

        # Redirect to a thank you page or some other page
        return render(request, 'cart/place_order.html')

    else:
        # If the request method is GET, render the place order page
        # Retrieve the shipping address from the request.GET data
        shipping_address = request.GET.get('shipping_address', '')

        context = {
            'shipping_address': shipping_address,
        }

        return render(request, 'cart/place_order.html', context)


@login_required
def thank_you(request):
    # Clear the user's cart after checkout
    user_cart = Cart.objects.filter(user=request.user)
    user_cart.delete()

    return render(request, 'cart/thank_you.html')

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.price for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/cart.html', context)
