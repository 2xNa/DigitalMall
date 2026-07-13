from django.urls import path
from . import views

app_name = 'Goods'

urlpatterns = [
    path('', views.index_view, name='IndexView'),
    path('category/<int:pk>/', views.category_view, name='CategoryView'),
    path('product/<int:pk>/', views.product_detail, name='ProductDetail'),
    path('search/', views.product_search, name='ProductSearchView'),
    path('review/<int:pk>/', views.add_review, name='AddReview'),
    path('favorite/<int:pk>/', views.toggle_favorite, name='ToggleFavorite'),
]
