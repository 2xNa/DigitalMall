from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CartItem
from Goods.models import Product


@login_required
def cart_view(request):
    """购物车页面"""
    cart_items = CartItem.objects.filter(CartUser=request.user).select_related('CartProduct')
    total_price = sum(item.TotalPrice for item in cart_items if item.CartIsSelected)
    total_count = cart_items.count()
    context = {
        'page_title': '购物车 - 数码潮品商城',
        'cart_items': cart_items,
        'total_price': total_price,
        'total_count': total_count,
    }
    return render(request, 'Cart/cart.html', context)


@login_required
def cart_add(request, pk):
    """添加商品到购物车"""
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        quantity = int(request.POST.get('quantity', 1))

        cart_item, created = CartItem.objects.get_or_create(
            CartUser=request.user,
            CartProduct=product,
            defaults={'CartQuantity': quantity}
        )
        if not created:
            cart_item.CartQuantity += quantity
            cart_item.save()

        return JsonResponse({
            'status': 'success',
            'message': f'已加入购物车',
            'cart_count': CartItem.objects.filter(CartUser=request.user).count()
        })
    return JsonResponse({'status': 'error', 'message': '请求方式错误'})


@login_required
def cart_update(request, pk):
    """更新购物车商品数量"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk, CartUser=request.user)
        quantity = int(request.POST.get('quantity', 1))
        if quantity <= 0:
            cart_item.delete()
            return JsonResponse({'status': 'success', 'message': '已移除'})
        cart_item.CartQuantity = quantity
        cart_item.save()
        return JsonResponse({
            'status': 'success',
            'total_price': cart_item.TotalPrice,
        })
    return JsonResponse({'status': 'error', 'message': '请求方式错误'})


@login_required
def cart_remove(request, pk):
    """移除购物车商品"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk, CartUser=request.user)
        cart_item.delete()
        return JsonResponse({'status': 'success', 'message': '已移除'})
    return JsonResponse({'status': 'error', 'message': '请求方式错误'})


@login_required
def cart_toggle_select(request, pk):
    """切换商品选中状态"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk, CartUser=request.user)
        cart_item.CartIsSelected = not cart_item.CartIsSelected
        cart_item.save()
        selected_items = CartItem.objects.filter(CartUser=request.user, CartIsSelected=True)
        total_price = sum(item.TotalPrice for item in selected_items)
        return JsonResponse({
            'status': 'success',
            'is_selected': cart_item.CartIsSelected,
            'total_price': total_price,
        })
    return JsonResponse({'status': 'error', 'message': '请求方式错误'})
