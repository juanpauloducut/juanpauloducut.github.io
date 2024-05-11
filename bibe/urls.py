
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/',include('dashboard.urls')), 
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include URLs of other apps
    path('conversation/', include('conversation.urls')),
    path('cart/', include('cart.urls', namespace='cart')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
