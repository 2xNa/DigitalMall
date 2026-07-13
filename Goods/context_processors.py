"""
DigitalMall 全局上下文处理器
"""

from .models import Category


def global_context(request):
    """全局上下文"""
    categories = Category.objects.filter(IsVisible=True).order_by('CategorySort')[:8]
    return {
        'global_categories': categories,
    }
