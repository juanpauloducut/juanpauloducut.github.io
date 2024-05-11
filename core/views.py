from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout


from item.models import Category, Item

from .forms import SignupForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect ('/login')
    else: 
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form' : form
    })

def index(request):
    # Your view logic goes here
    return render(request, 'core/index.html')

def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout
    return render(request, 'core/index.html')  # Replace 'home' with the URL name of the page you want to redirect to