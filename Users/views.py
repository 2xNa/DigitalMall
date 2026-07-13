from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import UserProfile, BrowsingHistory
from Goods.models import Favorite


def user_login(request):
    """用户登录"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'Users/login.html', {'page_title': '登录 - 数码潮品商城'})


def user_register(request):
    """用户注册"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email', '')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, '两次密码输入不一致')
            return render(request, 'Users/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, '用户名已存在')
            return render(request, 'Users/register.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        UserProfile.objects.create(ProfileUser=user)
        messages.success(request, '注册成功，请登录')
        return redirect('Users:UserLogin')

    return render(request, 'Users/register.html', {'page_title': '注册 - 数码潮品商城'})


def user_logout(request):
    """用户注销"""
    logout(request)
    return redirect('Goods:IndexView')


@login_required
def user_profile(request):
    """个人中心"""
    profile = request.user.profile
    favorite_count = Favorite.objects.filter(FavoriteUser=request.user).count()
    order_count = request.user.orders.count()
    recent_orders = request.user.orders.all()[:5]
    context = {
        'page_title': '个人中心 - 数码潮品商城',
        'favorite_count': favorite_count,
        'order_count': order_count,
        'recent_orders': recent_orders,
    }
    return render(request, 'Users/profile.html', context)


@login_required
def update_profile(request):
    """更新个人信息"""
    if request.method == 'POST':
        profile = request.user.profile
        profile.ProfilePhone = request.POST.get('phone', '')
        profile.ProfileAddress = request.POST.get('address', '')
        profile.ProfileGender = request.POST.get('gender', 'Other')
        if request.FILES.get('avatar'):
            profile.ProfileAvatar = request.FILES['avatar']
        profile.save()
        messages.success(request, '信息更新成功')
        return redirect('Users:UserProfileView')
    return redirect('Users:UserProfileView')


@login_required
def favorite_list(request):
    """收藏列表"""
    favorites = Favorite.objects.filter(FavoriteUser=request.user).select_related('FavoriteProduct')
    context = {
        'page_title': '我的收藏 - 数码潮品商城',
        'favorites': favorites,
    }
    return render(request, 'Users/favorites.html', context)


@login_required
def browsing_history(request):
    """浏览历史"""
    history = BrowsingHistory.objects.filter(HistoryUser=request.user).select_related('HistoryProduct')[:50]
    context = {
        'page_title': '浏览历史 - 数码潮品商城',
        'history': history,
    }
    return render(request, 'Users/history.html', context)
