from django.urls import path
from . import views

app_name = 'ChatBot'

urlpatterns = [
    path('', views.chat_view, name='ChatView'),
    path('send/', views.chat_send, name='ChatSend'),
    path('history/', views.chat_history, name='ChatHistory'),
]
