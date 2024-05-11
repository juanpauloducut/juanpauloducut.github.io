
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "cart"

urlpatterns = [
    path("add/<item_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("", views.cart_detail, name="cart_detail"),
    path("checkout/", views.checkout, name='checkout'),
    path("place_order/", views.place_order, name='place_order'),
    path('thank_you/', views.thank_you, name='thank_you'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)