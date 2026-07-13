from django.db import models
from django.contrib.auth.models import User
from Goods.models import Product


class UserProfile(models.Model):
    """用户信息扩展"""
    GENDER_CHOICES = [
        ('Male', '男'),
        ('Female', '女'),
        ('Other', '其他'),
    ]
    ProfileUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='关联用户')
    ProfileAvatar = models.ImageField('头像', upload_to='avatars/', blank=True, default='')
    ProfilePhone = models.CharField('手机号', max_length=20, blank=True, default='')
    ProfileAddress = models.CharField('默认地址', max_length=300, blank=True, default='')
    ProfileGender = models.CharField('性别', max_length=10, choices=GENDER_CHOICES, default='Other')
    ProfileBirthday = models.DateField('生日', blank=True, null=True)
    CreateTime = models.DateTimeField('注册时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.ProfileUser.username


class BrowsingHistory(models.Model):
    """浏览历史"""
    HistoryUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='browsing_history', verbose_name='用户')
    HistoryProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='浏览商品')
    HistoryTime = models.DateTimeField('浏览时间', auto_now_add=True)

    class Meta:
        verbose_name = '浏览历史'
        verbose_name_plural = '浏览历史'
        ordering = ['-HistoryTime']

    def __str__(self):
        return f'{self.HistoryUser.username} - {self.HistoryProduct.ProductName}'
