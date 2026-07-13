from django.contrib import admin
from .models import UserProfile, BrowsingHistory


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['ProfileUser', 'ProfilePhone', 'ProfileGender', 'CreateTime']
    search_fields = ['ProfileUser__username', 'ProfilePhone']


@admin.register(BrowsingHistory)
class BrowsingHistoryAdmin(admin.ModelAdmin):
    list_display = ['HistoryUser', 'HistoryProduct', 'HistoryTime']
    search_fields = ['HistoryUser__username', 'HistoryProduct__ProductName']
