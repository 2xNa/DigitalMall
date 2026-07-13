from django.contrib import admin
from .models import Category, Product, ProductReview, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['CategoryName', 'CategorySort', 'IsVisible', 'CreateTime']
    list_editable = ['CategorySort', 'IsVisible']
    search_fields = ['CategoryName']
    list_filter = ['IsVisible']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductName', 'ProductCategory', 'ProductPrice', 'ProductSales', 'IsNew', 'IsHot', 'IsRecommend', 'IsOnSale', 'CreateTime']
    list_editable = ['IsNew', 'IsHot', 'IsRecommend', 'IsOnSale']
    list_filter = ['ProductCategory', 'IsNew', 'IsHot', 'IsRecommend', 'IsOnSale']
    search_fields = ['ProductName', 'ProductDesc', 'ProductTags']
    readonly_fields = ['ProductSales']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['ReviewProduct', 'ReviewUser', 'ReviewRating', 'ReviewTime']
    list_filter = ['ReviewRating']
    search_fields = ['ReviewContent']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['FavoriteUser', 'FavoriteProduct', 'FavoriteTime']
    search_fields = ['FavoriteUser__username', 'FavoriteProduct__ProductName']
