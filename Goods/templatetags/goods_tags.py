"""
Goods template tags - 自定义模板标签
"""

from django import template

register = template.Library()


@register.filter(name='split')
def split_filter(value, arg):
    """分割字符串"""
    return value.split(arg)


@register.filter(name='multiply')
def multiply_filter(value, arg):
    """乘法"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter(name='sub')
def sub_filter(value, arg):
    """减法"""
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0
