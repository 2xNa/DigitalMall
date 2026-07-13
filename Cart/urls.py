from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('', views.cart_view, name='CartView'),
    path('add/<int:pk>/', views.cart_add, name='CartAddView'),
    path('update/<int:pk>/', views.cart_update, name='CartUpdateView'),
    path('remove/<int:pk>/', views.cart_remove, name='CartRemoveView'),
    path('toggle/<int:pk>/', views.cart_toggle_select, name='CartToggleSelect'),
]
