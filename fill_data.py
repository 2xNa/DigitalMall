"""
填充测试数据脚本
运行方式: python fill_data.py
"""
import os
import django

# 配置 Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DigitalMall.settings')
django.setup()

# 现在导入模型
from Goods.models import Category, Product
from ChatBot.models import KeywordRule
from django.contrib.auth.models import User
from Users.models import UserProfile

print('开始填充数据...')

# ===== 创建分类 =====
categories_data = [
    {'name': '手机', 'icon': 'fas fa-mobile-alt', 'desc': '最新智能手机，旗舰与性价比之选', 'sort': 1},
    {'name': '笔记本电脑', 'icon': 'fas fa-laptop', 'desc': '轻薄本、游戏本、商务本一应俱全', 'sort': 2},
    {'name': '平板电脑', 'icon': 'fas fa-tablet-alt', 'desc': '学习办公娱乐，平板让生活更便捷', 'sort': 3},
    {'name': '耳机音箱', 'icon': 'fas fa-headphones', 'desc': '沉浸式音频体验，降噪蓝牙全覆盖', 'sort': 4},
    {'name': '智能穿戴', 'icon': 'fas fa-clock', 'desc': '智能手表、手环，科技与时尚的结合', 'sort': 5},
    {'name': '摄影摄像', 'icon': 'fas fa-camera', 'desc': '专业相机、运动相机、无人机', 'sort': 6},
    {'name': '游戏外设', 'icon': 'fas fa-gamepad', 'desc': '键盘鼠标手柄，电竞利器', 'sort': 7},
    {'name': '充电配件', 'icon': 'fas fa-bolt', 'desc': '充电器、数据线、移动电源', 'sort': 8},
]

categories = {}
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(
        CategoryName=cat_data['name'],
        defaults={
            'CategoryIcon': cat_data['icon'],
            'CategoryDesc': cat_data['desc'],
            'CategorySort': cat_data['sort'],
            'IsVisible': True,
        }
    )
    categories[cat_data['name']] = cat
    print(f'{"创建" if created else "已存在"}分类: {cat.CategoryName}')

# ===== 创建商品 =====
products_data = [
    # 手机
    {'name': 'iPhone 16 Pro Max', 'category': '手机', 'price': 9999, 'original': 10999, 'desc': 'A18 Pro芯片，钛金属设计，4800万像素主摄', 'tags': '苹果,旗舰,5G', 'sales': 5680, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': '华为 Mate 70 Pro+', 'category': '手机', 'price': 8999, 'original': 9999, 'desc': '麒麟芯片，卫星通信，超感知影像系统', 'tags': '华为,旗舰,卫星通信', 'sales': 4320, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': False},
    {'name': '小米15 Ultra', 'category': '手机', 'price': 5999, 'original': 6499, 'desc': '骁龙8 Elite，徕卡光学，2K超感屏', 'tags': '小米,旗舰,徕卡', 'sales': 3890, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': 'OPPO Find X8 Pro', 'category': '手机', 'price': 5299, 'original': 5999, 'desc': '天玑9400，哈苏影像，潜望长焦', 'tags': 'OPPO,旗舰,哈苏', 'sales': 2150, 'is_new': True, 'is_hot': False, 'is_recommend': True, 'is_sale': True},
    {'name': 'Redmi K80 Pro', 'category': '手机', 'price': 3299, 'original': 3599, 'desc': '骁龙8 Elite，2K屏，5500mAh大电池', 'tags': '红米,性价比,游戏', 'sales': 6780, 'is_new': False, 'is_hot': True, 'is_recommend': False, 'is_sale': True},
    {'name': '三星 Galaxy S25 Ultra', 'category': '手机', 'price': 9699, 'original': 10199, 'desc': '骁龙8 Elite for Galaxy，S Pen，2亿像素', 'tags': '三星,旗舰,S Pen', 'sales': 1890, 'is_new': True, 'is_hot': False, 'is_recommend': True, 'is_sale': False},

    # 笔记本电脑
    {'name': 'MacBook Pro 16 M4 Max', 'category': '笔记本电脑', 'price': 27999, 'original': 29999, 'desc': 'M4 Max芯片，48GB统一内存，Liquid Retina XDR屏', 'tags': '苹果,专业,创作', 'sales': 2340, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': '联想 ThinkPad X1 Carbon', 'category': '笔记本电脑', 'price': 12999, 'original': 14999, 'desc': '酷睿Ultra 7，14英寸2.8K OLED，1.08kg超轻', 'tags': '商务,轻薄,ThinkPad', 'sales': 1890, 'is_new': False, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': '华硕 ROG 枪神8 Plus', 'category': '笔记本电脑', 'price': 16999, 'original': 18999, 'desc': 'i9-14900HX，RTX 4080，18英寸240Hz', 'tags': '游戏,ROG,高性能', 'sales': 1560, 'is_new': True, 'is_hot': True, 'is_recommend': False, 'is_sale': False},
    {'name': '华为 MateBook X Pro', 'category': '笔记本电脑', 'price': 11999, 'original': 13999, 'desc': '酷睿Ultra 9，3.1K触控屏，超级终端', 'tags': '华为,商务,触控', 'sales': 2100, 'is_new': True, 'is_hot': False, 'is_recommend': True, 'is_sale': True},
    {'name': '小米 RedmiBook Pro 16', 'category': '笔记本电脑', 'price': 5499, 'original': 5999, 'desc': '酷睿Ultra 5，3.1K 165Hz，大电池长续航', 'tags': '红米,性价比,办公', 'sales': 4560, 'is_new': False, 'is_hot': True, 'is_recommend': True, 'is_sale': True},

    # 平板电脑
    {'name': 'iPad Pro 13 M4', 'category': '平板电脑', 'price': 10999, 'original': 11499, 'desc': 'M4芯片，Ultra Retina XDR，Apple Pencil Pro', 'tags': '苹果,专业,创作', 'sales': 3450, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': False},
    {'name': '华为 MatePad Pro 13.2', 'category': '平板电脑', 'price': 5699, 'original': 6299, 'desc': '麒麟9000S，OLED柔性屏，星闪手写笔', 'tags': '华为,办公,星闪', 'sales': 2670, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': '小米平板7 Pro', 'category': '平板电脑', 'price': 2999, 'original': 3299, 'desc': '骁龙8s Gen3，11.2英寸144Hz，PC级WPS', 'tags': '小米,性价比,办公', 'sales': 5120, 'is_new': True, 'is_hot': True, 'is_recommend': False, 'is_sale': True},

    # 耳机音箱
    {'name': 'AirPods Pro 3', 'category': '耳机音箱', 'price': 1899, 'original': 1999, 'desc': 'H3芯片，自适应降噪，个性化空间音频', 'tags': '苹果,降噪,蓝牙', 'sales': 8900, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': '索尼 WH-1000XM6', 'category': '耳机音箱', 'price': 2699, 'original': 2999, 'desc': '行业标杆降噪，30小时续航，LDAC高清音质', 'tags': '索尼,降噪,头戴', 'sales': 4560, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': False},
    {'name': '华为 FreeBuds Pro 4', 'category': '耳机音箱', 'price': 1299, 'original': 1499, 'desc': '星闪连接，超感知降噪，Hi-Res认证', 'tags': '华为,降噪,星闪', 'sales': 3780, 'is_new': True, 'is_hot': False, 'is_recommend': True, 'is_sale': True},
    {'name': 'Bose SoundLink Flex', 'category': '耳机音箱', 'price': 1199, 'original': 1399, 'desc': 'IP67防水，PositionIQ自动调音，12小时续航', 'tags': 'Bose,蓝牙音箱,户外', 'sales': 2340, 'is_new': False, 'is_hot': False, 'is_recommend': False, 'is_sale': True},

    # 智能穿戴
    {'name': 'Apple Watch Ultra 3', 'category': '智能穿戴', 'price': 6499, 'original': 6999, 'desc': '双频GPS，潜水电脑，钛金属表壳', 'tags': '苹果,运动,专业', 'sales': 2890, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': False},
    {'name': '华为 Watch GT 5 Pro', 'category': '智能穿戴', 'price': 2488, 'original': 2888, 'desc': '14天超长续航，百种运动模式，健康监测', 'tags': '华为,运动,长续航', 'sales': 3450, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': '小米手环9 Pro', 'category': '智能穿戴', 'price': 299, 'original': 349, 'desc': '1.74英寸AMOLED，150+运动模式，NFC', 'tags': '小米,手环,性价比', 'sales': 12300, 'is_new': False, 'is_hot': True, 'is_recommend': False, 'is_sale': True},

    # 摄影摄像
    {'name': '索尼 A7R V', 'category': '摄影摄像', 'price': 25999, 'original': 27999, 'desc': '6100万像素，AI对焦，8K视频', 'tags': '索尼,全画幅,专业', 'sales': 890, 'is_new': False, 'is_hot': True, 'is_recommend': True, 'is_sale': False},
    {'name': '大疆 Mini 4 Pro', 'category': '摄影摄像', 'price': 5788, 'original': 6188, 'desc': '4K/60fps HDR，全向避障，249g轻巧', 'tags': '大疆,无人机,航拍', 'sales': 2340, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': 'GoPro Hero 13 Black', 'category': '摄影摄像', 'price': 3498, 'original': 3998, 'desc': '5.3K超清，10米防水，超强防抖', 'tags': 'GoPro,运动相机,防水', 'sales': 1670, 'is_new': True, 'is_hot': False, 'is_recommend': False, 'is_sale': True},

    # 游戏外设
    {'name': '罗技 G Pro X Superlight 2', 'category': '游戏外设', 'price': 999, 'original': 1099, 'desc': '63g超轻，LIGHTSPEED，HERO 2传感器', 'tags': '罗技,鼠标,电竞', 'sales': 5670, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': False},
    {'name': '雷蛇 黑寡妇 V4 Pro', 'category': '游戏外设', 'price': 2199, 'original': 2499, 'desc': '绿轴，RGB Chroma，磁吸手托', 'tags': '雷蛇,键盘,电竞', 'sales': 3210, 'is_new': False, 'is_hot': True, 'is_recommend': False, 'is_sale': True},
    {'name': '索尼 DualSense Edge', 'category': '游戏外设', 'price': 899, 'original': 999, 'desc': '自定义背键，可换摇杆，触觉反馈', 'tags': '索尼,手柄,PS5', 'sales': 4560, 'is_new': False, 'is_hot': True, 'is_recommend': True, 'is_sale': True},

    # 充电配件
    {'name': 'Anker 140W 氮化镓充电器', 'category': '充电配件', 'price': 399, 'original': 499, 'desc': '三口输出，140W大功率，折叠插脚', 'tags': 'Anker,充电器,GaN', 'sales': 8900, 'is_new': True, 'is_hot': True, 'is_recommend': True, 'is_sale': True},
    {'name': '小米 20000mAh 移动电源', 'category': '充电配件', 'price': 179, 'original': 199, 'desc': '50W快充，三口输出，LED数显', 'tags': '小米,移动电源,快充', 'sales': 15600, 'is_new': False, 'is_hot': True, 'is_recommend': False, 'is_sale': True},
    {'name': '贝尔金 三合一磁吸充电板', 'category': '充电配件', 'price': 599, 'original': 699, 'desc': 'Qi2协议，iPhone+Apple Watch+AirPods', 'tags': '贝尔金,无线充,苹果', 'sales': 3450, 'is_new': True, 'is_hot': False, 'is_recommend': True, 'is_sale': False},
]

for idx, prod_data in enumerate(products_data):
    product, created = Product.objects.get_or_create(
        ProductName=prod_data['name'],
        defaults={
            'ProductCategory': categories[prod_data['category']],
            'ProductPrice': prod_data['price'],
            'ProductOriginalPrice': prod_data['original'],
            'ProductDesc': prod_data['desc'],
            'ProductDetail': f'<h3>{prod_data["name"]}</h3><p>{prod_data["desc"]}</p><p>更多详细信息请咨询客服。</p>',
            'ProductTags': prod_data['tags'],
            'ProductStock': 100,
            'ProductSales': prod_data['sales'],
            'ProductImage': f'products/product_{idx % 30 + 1}.jpg',
            'IsNew': prod_data['is_new'],
            'IsHot': prod_data['is_hot'],
            'IsRecommend': prod_data['is_recommend'],
            'IsOnSale': prod_data['is_sale'],
        }
    )
    print(f'{"创建" if created else "已存在"}商品: {product.ProductName}')

# ===== 创建关键词规则 =====
rules_data = [
    {'keyword': '手机', 'category': '手机', 'response': '我们有多款手机在售，从旗舰到性价比应有尽有！', 'priority': 10},
    {'keyword': '笔记本', 'category': '笔记本电脑', 'response': '我们有轻薄本、游戏本、商务本等多种选择！', 'priority': 10},
    {'keyword': '电脑', 'category': '笔记本电脑', 'response': '我们有各类笔记本电脑可供选择，包括轻薄本和游戏本！', 'priority': 9},
    {'keyword': '平板', 'category': '平板电脑', 'response': '我们有多款平板电脑，适合学习、办公和娱乐！', 'priority': 10},
    {'keyword': '耳机', 'category': '耳机音箱', 'response': '我们有降噪耳机、蓝牙耳机、头戴式耳机等多种选择！', 'priority': 10},
    {'keyword': '音箱', 'category': '耳机音箱', 'response': '我们有蓝牙音箱、智能音箱等多种选择！', 'priority': 9},
    {'keyword': '手表', 'category': '智能穿戴', 'response': '我们有Apple Watch、华为手表等智能穿戴设备！', 'priority': 10},
    {'keyword': '相机', 'category': '摄影摄像', 'response': '我们有专业相机、运动相机和无人机等摄影设备！', 'priority': 10},
    {'keyword': '无人机', 'category': '摄影摄像', 'response': '我们有大疆无人机，适合航拍和创作！', 'priority': 9},
    {'keyword': '键盘', 'category': '游戏外设', 'response': '我们有机械键盘、电竞键盘等多种选择！', 'priority': 8},
    {'keyword': '鼠标', 'category': '游戏外设', 'response': '我们有电竞鼠标、办公鼠标等多种选择！', 'priority': 8},
    {'keyword': '充电', 'category': '充电配件', 'response': '我们有充电器、移动电源、数据线等充电配件！', 'priority': 8},
    {'keyword': '苹果', 'category': '手机', 'response': '我们有iPhone、MacBook、iPad等苹果全系列产品！', 'priority': 10},
    {'keyword': '华为', 'category': '手机', 'response': '我们有华为手机、笔记本、平板等全系列产品！', 'priority': 10},
    {'keyword': '小米', 'category': '手机', 'response': '我们有小米手机、平板、配件等高性价比产品！', 'priority': 9},
    {'keyword': '推荐', 'category': None, 'response': '为您推荐当前热销商品！您可以告诉我想要什么类型的数码产品，我来帮您精准推荐。', 'priority': 5},
    {'keyword': '便宜', 'category': None, 'response': '我们商城有很多优惠商品，查看首页促销专区，或告诉我您想要的品类！', 'priority': 5},
    {'keyword': '新品', 'category': None, 'response': '我们不断上新最新数码产品！查看首页新品专区，或告诉我您感兴趣的品类。', 'priority': 5},
]

for rule_data in rules_data:
    rule, created = KeywordRule.objects.get_or_create(
        RuleKeyword=rule_data['keyword'],
        defaults={
            'RuleCategory': categories.get(rule_data['category']),
            'RuleResponse': rule_data['response'],
            'RulePriority': rule_data['priority'],
            'IsEnabled': True,
        }
    )
    print(f'{"创建" if created else "已存在"}规则: {rule.RuleKeyword}')

# ===== 创建测试用户 =====
test_user, created = User.objects.get_or_create(
    username='testuser',
    defaults={
        'email': 'test@digitalmall.com',
    }
)
if created:
    test_user.set_password('test123456')
    test_user.save()
    UserProfile.objects.create(ProfileUser=test_user)
    print('创建测试用户: testuser / test123456')
else:
    print('测试用户已存在: testuser')

# 创建管理员
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'is_staff': True,
        'is_superuser': True,
        'email': 'admin@digitalmall.com',
    }
)
if created:
    admin_user.set_password('admin123456')
    admin_user.save()
    UserProfile.objects.create(ProfileUser=admin_user)
    print('创建管理员: admin / admin123456')
else:
    print('管理员已存在: admin')

print('\n===== 数据填充完成 =====')
print(f'分类数: {Category.objects.count()}')
print(f'商品数: {Product.objects.count()}')
print(f'关键词规则数: {KeywordRule.objects.count()}')
