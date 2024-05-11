from django import template

register = template.Library()

@register.filter
def calculate_subtotal(item):
    return int(item.quantity) * int(item.price)