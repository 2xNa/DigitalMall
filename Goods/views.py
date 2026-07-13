from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Product, ProductReview, Favorite
from Users.models import BrowsingHistory


def index_view(request):
    """首页"""
    categories = Category.objects.filter(IsVisible=True).order_by('CategorySort')
    new_products = Product.objects.filter(IsNew=True, IsOnSale=True)[:8]
    hot_products = Product.objects.filter(IsHot=True)[:8]
    recommend_products = Product.objects.filter(IsRecommend=True)[:8]
    sale_products = Product.objects.filter(IsOnSale=True)[:8]
    context = {
        'page_title': '数码潮品商城 - 首页',
        'categories': categories,
        'new_products': new_products,
        'hot_products': hot_products,
        'recommend_products': recommend_products,
        'sale_products': sale_products,
    }
    return render(request, 'Goods/index.html', context)


def category_view(request, pk):
    """分类页面"""
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(ProductCategory=category, IsOnSale=True)

    # 排序
    sort = request.GET.get('sort', 'default')
    if sort == 'price_asc':
        products = products.order_by('ProductPrice')
    elif sort == 'price_desc':
        products = products.order_by('-ProductPrice')
    elif sort == 'sales':
        products = products.order_by('-ProductSales')
    elif sort == 'new':
        products = products.order_by('-CreateTime')
    else:
        products = products.order_by('-CreateTime')

    # 搜索
    keyword = request.GET.get('q', '')
    if keyword:
        products = products.filter(
            Q(ProductName__icontains=keyword) |
            Q(ProductDesc__icontains=keyword) |
            Q(ProductTags__icontains=keyword)
        )

    context = {
        'page_title': f'{category.CategoryName} - 数码潮品商城',
        'category': category,
        'products': products,
        'categories': Category.objects.filter(IsVisible=True),
        'keyword': keyword,
        'sort': sort,
    }
    return render(request, 'Goods/category.html', context)


def product_detail(request, pk):
    """商品详情"""
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    related_products = Product.objects.filter(
        ProductCategory=product.ProductCategory,
        IsOnSale=True
    ).exclude(pk=product.pk)[:4]

    # 记录浏览历史
    if request.user.is_authenticated:
        BrowsingHistory.objects.create(
            HistoryUser=request.user,
            HistoryProduct=product
        )

    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(
            FavoriteUser=request.user,
            FavoriteProduct=product
        ).exists()

    context = {
        'page_title': f'{product.ProductName} - 数码潮品商城',
        'product': product,
        'reviews': reviews,
        'related_products': related_products,
        'is_favorited': is_favorited,
    }
    return render(request, 'Goods/detail.html', context)


def product_search(request):
    """商品搜索"""
    keyword = request.GET.get('q', '')
    products = Product.objects.filter(IsOnSale=True)

    if keyword:
        products = products.filter(
            Q(ProductName__icontains=keyword) |
            Q(ProductDesc__icontains=keyword) |
            Q(ProductTags__icontains=keyword) |
            Q(ProductCategory__CategoryName__icontains=keyword)
        )

    # 排序
    sort = request.GET.get('sort', 'default')
    if sort == 'price_asc':
        products = products.order_by('ProductPrice')
    elif sort == 'price_desc':
        products = products.order_by('-ProductPrice')
    elif sort == 'sales':
        products = products.order_by('-ProductSales')
    elif sort == 'new':
        products = products.order_by('-CreateTime')
    else:
        products = products.order_by('-CreateTime')

    context = {
        'page_title': f'搜索"{keyword}" - 数码潮品商城' if keyword else '商品搜索',
        'products': products,
        'keyword': keyword,
        'sort': sort,
    }
    return render(request, 'Goods/category.html', context)


@login_required
def add_review(request, pk):
    """添加评价"""
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        rating = request.POST.get('rating', 5)
        content = request.POST.get('content', '')

        if not content:
            return JsonResponse({'status': 'error', 'message': '评价内容不能为空'})

        ProductReview.objects.create(
            ReviewProduct=product,
            ReviewUser=request.user,
            ReviewRating=int(rating),
            ReviewContent=content,
        )
        return JsonResponse({'status': 'success', 'message': '评价成功'})
    return JsonResponse({'status': 'error', 'message': '请求方式错误'})


@login_required
def toggle_favorite(request, pk):
    """切换收藏状态"""
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        favorite, created = Favorite.objects.get_or_create(
            FavoriteUser=request.user,
            FavoriteProduct=product,
        )
        if created:
            return JsonResponse({'status': 'success', 'message': '收藏成功'})
        else:
            favorite.delete()
            return JsonResponse({'status': 'success', 'message': '已取消收藏'})
    return JsonResponse({'status': 'error', 'message': '请求方式错误'})
