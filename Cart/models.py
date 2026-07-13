from django.db import models
from django.contrib.auth.models import User
from Goods.models import Product


class CartItem(models.Model):
    """购物车项"""
    CartUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items', verbose_name='用户')
    CartProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='商品')
    CartQuantity = models.IntegerField('商品数量', default=1)
    CartIsSelected = models.BooleanField('是否选中', default=True)
    CreateTime = models.DateTimeField('添加时间', auto_now_add=True)
    UpdateTime = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '购物车项'
        verbose_name_plural = '购物车项'
        unique_together = ['CartUser', 'CartProduct']

    @property
    def TotalPrice(self):
        """计算小计金额"""
        return float(self.CartProduct.ProductPrice) * self.CartQuantity

    def __str__(self):
        return f'{self.CartUser.username} - {self.CartProduct.ProductName} x {self.CartQuantity}'
