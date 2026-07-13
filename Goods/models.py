from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """商品分类"""
    CategoryName = models.CharField('分类名称', max_length=100, unique=True)
    CategoryIcon = models.CharField('分类图标', max_length=100, blank=True, default='fas fa-laptop')
    CategoryDesc = models.TextField('分类描述', blank=True, default='')
    CategorySort = models.IntegerField('排序权重', default=0)
    IsVisible = models.BooleanField('是否显示', default=True)
    CreateTime = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = '商品分类'
        ordering = ['CategorySort', '-CreateTime']

    def __str__(self):
        return self.CategoryName


class Product(models.Model):
    """商品"""
    ProductCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='所属分类')
    ProductName = models.CharField('商品名称', max_length=200)
    ProductPrice = models.DecimalField('商品价格', max_digits=10, decimal_places=2)
    ProductOriginalPrice = models.DecimalField('原价', max_digits=10, decimal_places=2, default=0)
    ProductImage = models.ImageField('商品图片', upload_to='products/', blank=True, default='')
    ProductDesc = models.TextField('商品描述', blank=True, default='')
    ProductDetail = models.TextField('商品详情', blank=True, default='')
    ProductSpecs = models.JSONField('商品规格', blank=True, default=dict)
    ProductStock = models.IntegerField('库存数量', default=100)
    ProductSales = models.IntegerField('销量', default=0)
    ProductTags = models.CharField('商品标签', max_length=200, blank=True, default='')
    IsNew = models.BooleanField('是否新品', default=True)
    IsHot = models.BooleanField('是否热销', default=False)
    IsRecommend = models.BooleanField('是否推荐', default=False)
    IsOnSale = models.BooleanField('是否促销', default=False)
    CreateTime = models.DateTimeField('创建时间', auto_now_add=True)
    UpdateTime = models.DateTimeField('更新时间', auto_now=True)

    @property
    def DiscountPercent(self):
        """计算折扣百分比"""
        if self.ProductOriginalPrice and self.ProductOriginalPrice > self.ProductPrice:
            return int((1 - float(self.ProductPrice) / float(self.ProductOriginalPrice)) * 100)
        return 0

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
        ordering = ['-CreateTime']

    def __str__(self):
        return self.ProductName


class ProductReview(models.Model):
    """商品评价"""
    RATING_CHOICES = [
        (1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星'),
    ]
    ReviewProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='评价商品')
    ReviewUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评价用户')
    ReviewRating = models.IntegerField('评分', choices=RATING_CHOICES, default=5)
    ReviewContent = models.TextField('评价内容', max_length=500)
    ReviewTime = models.DateTimeField('评价时间', auto_now_add=True)

    class Meta:
        verbose_name = '商品评价'
        verbose_name_plural = '商品评价'
        ordering = ['-ReviewTime']

    def __str__(self):
        return f'{self.ReviewUser.username} - {self.ReviewProduct.ProductName}'


class Favorite(models.Model):
    """商品收藏"""
    FavoriteUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name='收藏用户')
    FavoriteProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by', verbose_name='收藏商品')
    FavoriteTime = models.DateTimeField('收藏时间', auto_now_add=True)

    class Meta:
        verbose_name = '商品收藏'
        verbose_name_plural = '商品收藏'
        unique_together = ['FavoriteUser', 'FavoriteProduct']

    def __str__(self):
        return f'{self.FavoriteUser.username} - {self.FavoriteProduct.ProductName}'
