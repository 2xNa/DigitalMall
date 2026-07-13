from django.urls import path
from . import views

app_name = 'Order'

urlpatterns = [
    path('create/', views.order_create, name='OrderCreateView'),
    path('submit/', views.order_submit, name='OrderSubmitView'),
    path('success/<str:order_no>/', views.order_success, name='OrderSuccessView'),
    path('list/', views.order_list, name='OrderListView'),
    path('detail/<str:order_no>/', views.order_detail, name='OrderDetailView'),
    path('cancel/<str:order_no>/', views.order_cancel, name='OrderCancelView'),
]
