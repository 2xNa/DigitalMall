from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Order, OrderItem
from Cart.models import CartItem


@login_required
def order_create(request):
    """创建订单页面"""
    cart_items = CartItem.objects.filter(CartUser=request.user, CartIsSelected=True).select_related('CartProduct')
    if not cart_items:
        return redirect('Cart:CartView')

    total_price = sum(item.TotalPrice for item in cart_items)
    total_count = sum(item.CartQuantity for item in cart_items)

    # 获取默认收货信息
    profile = request.user.profile
    context = {
        'page_title': '确认订单 - 数码潮品商城',
        'selected_items': cart_items,
        'total_price': total_price,
        'total_count': total_count,
        'default_receiver': request.user.username,
        'default_phone': profile.ProfilePhone,
        'default_address': profile.ProfileAddress,
    }
    return render(request, 'Order/order_create.html', context)


@login_required
def order_submit(request):
    """提交订单"""
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(CartUser=request.user, CartIsSelected=True)
        if not cart_items:
            return redirect('Cart:CartView')

        total_price = sum(item.TotalPrice for item in cart_items)
        receiver = request.POST.get('receiver', request.user.username)
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        remark = request.POST.get('remark', '')
        pay_method = request.POST.get('pay_method', 'Alipay')

        # 创建订单
        order = Order.objects.create(
            OrderUser=request.user,
            OrderTotalPrice=total_price,
            OrderReceiver=receiver,
            OrderPhone=phone,
            OrderAddress=address,
            OrderRemark=remark,
            OrderPayMethod=pay_method,
        )

        # 创建订单项并清空购物车
        for cart_item in cart_items:
            OrderItem.objects.create(
                ItemOrder=order,
                ItemProduct=cart_item.CartProduct,
                ItemProductName=cart_item.CartProduct.ProductName,
                ItemProductImage=cart_item.CartProduct.ProductImage.url if cart_item.CartProduct.ProductImage else '',
                ItemPrice=cart_item.CartProduct.ProductPrice,
                ItemQuantity=cart_item.CartQuantity,
                ItemTotalPrice=cart_item.TotalPrice,
            )
            cart_item.delete()

        return redirect('Order:OrderSuccessView', order_no=order.OrderNo)
    return redirect('Cart:CartView')


@login_required
def order_success(request, order_no):
    """订单创建成功页面"""
    order = get_object_or_404(Order, OrderNo=order_no, OrderUser=request.user)
    order_items = order.items.all()
    context = {
        'page_title': '下单成功 - 数码潮品商城',
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'Order/order_success.html', context)


@login_required
def order_list(request):
    """订单列表"""
    orders = Order.objects.filter(OrderUser=request.user).prefetch_related('items')
    context = {
        'page_title': '我的订单 - 数码潮品商城',
        'orders': orders,
    }
    return render(request, 'Order/order_list.html', context)


@login_required
def order_detail(request, order_no):
    """订单详情"""
    order = get_object_or_404(Order, OrderNo=order_no, OrderUser=request.user)
    order_items = order.items.all()
    context = {
        'page_title': '订单详情 - 数码潮品商城',
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'Order/order_detail.html', context)


@login_required
def order_cancel(request, order_no):
    """取消订单"""
    order = get_object_or_404(Order, OrderNo=order_no, OrderUser=request.user)
    if order.OrderStatus == 'Pending':
        order.OrderStatus = 'Cancelled'
        order.save()
    return redirect('Order:OrderListView')
