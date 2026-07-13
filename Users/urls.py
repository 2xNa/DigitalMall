from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('login/', views.user_login, name='UserLogin'),
    path('register/', views.user_register, name='UserRegister'),
    path('logout/', views.user_logout, name='UserLogout'),
    path('profile/', views.user_profile, name='UserProfileView'),
    path('profile/update/', views.update_profile, name='UpdateProfile'),
    path('favorites/', views.favorite_list, name='FavoriteListView'),
    path('history/', views.browsing_history, name='BrowsingHistoryView'),
]
