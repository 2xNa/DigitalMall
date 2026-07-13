import uuid
from django.db import models
from django.contrib.auth.models import User
from Goods.models import Product


class Order(models.Model):
    """订单"""
    STATUS_CHOICES = [
        ('Pending', '待支付'),
        ('Paid', '已支付'),
        ('Shipped', '已发货'),
        ('Completed', '已完成'),
        ('Cancelled', '已取消'),
    ]
    PAY_METHOD_CHOICES = [
        ('Alipay', '支付宝'),
        ('WeChat', '微信支付'),
        ('BankCard', '银行卡'),
    ]
    OrderNo = models.CharField('订单编号', max_length=64, unique=True, default=uuid.uuid4)
    OrderUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='下单用户')
    OrderTotalPrice = models.DecimalField('订单总价', max_digits=10, decimal_places=2, default=0)
    OrderStatus = models.CharField('订单状态', max_length=20, choices=STATUS_CHOICES, default='Pending')
    OrderPayMethod = models.CharField('支付方式', max_length=20, choices=PAY_METHOD_CHOICES, default='Alipay')
    OrderAddress = models.CharField('收货地址', max_length=300, default='')
    OrderPhone = models.CharField('联系电话', max_length=20, default='')
    OrderReceiver = models.CharField('收货人', max_length=50, default='')
    OrderRemark = models.TextField('订单备注', blank=True, default='')
    CreateTime = models.DateTimeField('创建时间', auto_now_add=True)
    UpdateTime = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'
        ordering = ['-CreateTime']

    def __str__(self):
        return self.OrderNo


class OrderItem(models.Model):
    """订单项"""
    ItemOrder = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='所属订单')
    ItemProduct = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='商品')
    ItemProductName = models.CharField('商品名称', max_length=200, default='')
    ItemProductImage = models.CharField('商品图片', max_length=300, default='')
    ItemPrice = models.DecimalField('商品单价', max_digits=10, decimal_places=2)
    ItemQuantity = models.IntegerField('商品数量', default=1)
    ItemTotalPrice = models.DecimalField('小计金额', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = '订单项'
        verbose_name_plural = '订单项'

    def __str__(self):
        return f'{self.ItemProductName} x {self.ItemQuantity}'
