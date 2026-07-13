from django.contrib import admin
from .models import ChatMessage, KeywordRule


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['MessageUser', 'MessageSession', 'MessageRole', 'MessageMode', 'CreateTime']
    list_filter = ['MessageRole', 'MessageMode']
    search_fields = ['MessageContent', 'MessageSession']


@admin.register(KeywordRule)
class KeywordRuleAdmin(admin.ModelAdmin):
    list_display = ['RuleKeyword', 'RuleCategory', 'RulePriority', 'IsEnabled']
    list_editable = ['RulePriority', 'IsEnabled']
    list_filter = ['IsEnabled']
    search_fields = ['RuleKeyword', 'RuleResponse']
