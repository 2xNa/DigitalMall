"""
DigitalMall 主路由配置
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Goods.urls')),
    path('cart/', include('Cart.urls')),
    path('order/', include('Order.urls')),
    path('', include('Users.urls')),
    path('chatbot/', include('ChatBot.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
