from django.db import models
from django.contrib.auth.models import User
from Goods.models import Category


class ChatMessage(models.Model):
    """聊天记录"""
    ROLE_CHOICES = [
        ('user', '用户'),
        ('bot', '机器人'),
    ]
    MODE_CHOICES = [
        ('keyword', '关键词匹配'),
        ('llm', '大模型'),
        ('default', '默认回复'),
    ]
    MessageUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_messages', null=True, blank=True, verbose_name='用户')
    MessageSession = models.CharField('会话ID', max_length=100, default='')
    MessageRole = models.CharField('消息角色', max_length=20, choices=ROLE_CHOICES, default='user')
    MessageContent = models.TextField('消息内容')
    MessageMode = models.CharField('回复模式', max_length=20, choices=MODE_CHOICES, default='default')
    CreateTime = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '聊天记录'
        verbose_name_plural = '聊天记录'
        ordering = ['CreateTime']

    def __str__(self):
        return f'{self.MessageRole}: {self.MessageContent[:30]}'


class KeywordRule(models.Model):
    """关键词规则"""
    RuleKeyword = models.CharField('关键词', max_length=100)
    RuleCategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='关联分类')
    RuleResponse = models.TextField('回复内容')
    RulePriority = models.IntegerField('优先级', default=0)
    IsEnabled = models.BooleanField('是否启用', default=True)

    class Meta:
        verbose_name = '关键词规则'
        verbose_name_plural = '关键词规则'
        ordering = ['-RulePriority']

    def __str__(self):
        return self.RuleKeyword
