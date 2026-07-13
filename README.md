# DigitalMall 🚀 数码潮品商城

> *用 Python / Django 构建的全栈数码产品电商平台，赛博朋克风格 UI + AI 智能导购*

---

## 📋 项目简介

DigitalMall 是一个功能完整的数码产品电商网站，涵盖商品浏览、购物车、订单管理、用户系统以及 **AI 智能导购机器人**。前端采用暗色赛博朋克风格设计，使用 Bootstrap 5 + 自定义 CSS，后端基于 Django 6.0。

### 🎯 核心功能

| 模块 | 功能 |
|------|------|
| 🏪 **商品系统** | 分类导航、商品展示、搜索排序、商品详情、评价收藏 |
| 🛒 **购物车** | 增删改查、数量调整、勾选结算 |
| 📦 **订单系统** | 下单、订单列表、详情、取消 |
| 👤 **用户系统** | 注册登录、个人信息、浏览历史 |
| 🤖 **AI 导购** | 关键词匹配 + 智谱 GLM-4 大模型双重回复 |
| 🔧 **管理后台** | Django Admin 商品/订单/用户管理 |

---

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| **后端框架** | Django 6.0.6 |
| **数据库** | SQLite3（可切换 PostgreSQL/MySQL） |
| **前端** | Bootstrap 5、Font Awesome 6、自定义 CSS |
| **AI 引擎** | 智谱 AI GLM-4 Flash（关键词匹配兜底） |
| **图片处理** | Pillow |
| **运行时** | Python 3.12 |

---

## 🚀 快速启动

### 1️⃣ 克隆项目

```bash
git clone https://github.com/YOUR_USERNAME/DigitalMall.git
cd DigitalMall
```

### 2️⃣ 创建虚拟环境

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

> ⚠️ Windows 中文系统如果报编码错误，先执行 `$env:PYTHONIOENCODING='utf-8'` 再重试。

### 4️⃣ 配置环境变量

```bash
# 复制环境变量模板（首次必须执行）
copy .env.example .env      # Windows
cp .env.example .env         # macOS / Linux
```

> 编辑 `.env` 文件，填入你自己的 SECRET_KEY 和智谱 AI API Key（可选，不填则使用关键词兜底回复）。

### 5️⃣ 数据库迁移

```bash
python manage.py migrate
```

### 6️⃣ 生成商品占位图

```bash
python generate_placeholders.py
```

> 自动在 `media/products/` 下生成 30 张版权安全的占位图。

### 7️⃣ 填充测试数据

```bash
python fill_data.py
```

### 8️⃣ 启动开发服务器

```bash
python manage.py runserver
```

访问 **http://127.0.0.1:8000** 🎉

---

## 🔐 测试账号

| 角色 | 用户名 | 密码 |
|------|--------|------|
| 👤 普通用户 | `testuser` | `test123456` |
| 🔧 管理员 | `admin` | `admin123456` |

管理后台：http://127.0.0.1:8000/admin/

---

## 📁 项目结构

```
DigitalMall/
├── manage.py              # Django 管理入口
├── fill_data.py           # 测试数据填充脚本
├── requirements.txt       # 依赖清单
├── .gitignore             # Git 忽略规则
├── README.md              # 项目说明（你正在看这个）
│
├── DigitalMall/           # 主配置
│   ├── settings.py        # 全局配置
│   ├── urls.py            # URL 路由
│   └── wsgi.py            # WSGI 入口
│
├── Goods/                 # 商品模块
│   ├── models.py          # Category, Product, ProductReview, Favorite
│   ├── views.py           # 首页、分类、详情、搜索、评价、收藏
│   └── templatetags/      # 自定义模板标签
│
├── Cart/                  # 购物车模块
│   ├── models.py          # CartItem
│   └── views.py           # 购物车 CRUD
│
├── Order/                 # 订单模块
│   ├── models.py          # Order, OrderItem
│   └── views.py           # 下单、列表、详情、取消
│
├── Users/                 # 用户模块
│   ├── models.py          # UserProfile, BrowsingHistory
│   └── views.py           # 登录注册、个人中心、收藏、浏览历史
│
├── ChatBot/               # AI 导购模块
│   ├── models.py          # ChatMessage, KeywordRule
│   └── views.py           # 聊天界面、关键词匹配、LLM 调用
│
├── templates/             # HTML 模板
├── static/                # CSS / JS
└── media/                 # 上传文件（商品图片等）
```

---

## 🌟 项目亮点

1. **全栈实现** - 前后端分离思想 + Django Template 一体化
2. **AI 导购** - 集成大模型，关键词 + LLM 双引擎，体验流畅
3. **赛博朋克 UI** - 暗色主题 + 霓虹渐变色，视觉冲击力强
4. **响应式布局** - 移动端适配，手机电脑都能用
5. **代码规范** - 清晰的项目结构，模块化设计，中文注释
