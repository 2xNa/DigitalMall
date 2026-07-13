# DigitalMall 数码潮品商城

Python 课程大作业。基于 Django 6.0 的数码产品电商网站，赛博朋克风格 UI，集成 AI 智能导购。

## 功能

商品系统（分类、商品、评价、收藏）、购物车、订单管理、用户系统（注册登录、个人中心、浏览历史）、AI 导购（关键词匹配 + 智谱 GLM-4）。

后台管理使用 Django Admin，管理商品、订单、用户。

## 技术栈

后端 Django 6.0.6，数据库 SQLite3（可切换 PostgreSQL/MySQL），前端 Bootstrap 5 + Font Awesome 6 + 自定义 CSS，AI 引擎智谱 GLM-4 Flash（关键词匹配兜底），图片处理 Pillow，运行环境 Python 3.12。

## 快速启动

```
# 克隆
git clone https://github.com/2xNa/DigitalMall.git
cd DigitalMall

# 创建虚拟环境
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 安装依赖
pip install -r requirements.txt

# 复制环境变量模板（首次必须执行）
copy .env.example .env       # Windows
cp .env.example .env          # macOS / Linux

# 数据库迁移
python manage.py migrate

# 生成商品占位图
python generate_placeholders.py

# 填充测试数据
python fill_data.py

# 启动
python manage.py runserver
```

访问 http://127.0.0.1:8000

> Windows 中文系统如果 pip install 报编码错误，先执行 `$env:PYTHONIOENCODING='utf-8'` 再重试。

## 测试账号

| 角色 | 用户名 | 密码 |
|------|--------|--------|
| 普通用户 | testuser | test123456 |
| 管理员 | admin | admin123456 |

管理后台：http://127.0.0.1:8000/admin/

## 项目结构

```
DigitalMall/
├── manage.py                # 入口
├── fill_data.py             # 测试数据填充
├── requirements.txt         # 依赖
├── .gitignore
│
├── DigitalMall/             # 主配置
├── Goods/                   # 商品模块
├── Cart/                    # 购物车
├── Order/                   # 订单
├── Users/                   # 用户
├── ChatBot/                 # AI 导购
├── templates/               # HTML 模板
├── static/                  # CSS / JS
└── media/                   # 商品图片
```
