import json
import uuid
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import ChatMessage, KeywordRule
from Goods.models import Product, Category


def chat_view(request):
    """聊天页面"""
    if request.user.is_authenticated:
        session_id = f'user_{request.user.id}_{uuid.uuid4().hex[:8]}'
    else:
        session_id = f'anonymous_{uuid.uuid4().hex[:8]}'

    context = {
        'page_title': '智能导购 - 数码潮品商城',
        'session_id': session_id,
    }
    return render(request, 'ChatBot/chat.html', context)


def chat_send(request):
    """处理聊天消息"""
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '').strip()
        session_id = data.get('session_id', '')

        if not message:
            return JsonResponse({'status': 'error', 'message': '消息不能为空'})

        # 保存用户消息
        ChatMessage.objects.create(
            MessageUser=request.user if request.user.is_authenticated else None,
            MessageSession=session_id,
            MessageRole='user',
            MessageContent=message,
        )

        reply = None
        mode = None

        # 1. 如果配置了API Key，优先调用大模型
        if settings.CHATBOT_API_KEY:
            reply, mode = llm_chat(message, session_id)

        # 2. 大模型无回复时，尝试关键词匹配
        if not reply:
            reply, mode = keyword_match(message)

        # 3. 兜底默认回复
        if not reply:
            reply = get_default_reply()
            mode = 'default'

        # 保存机器人回复
        ChatMessage.objects.create(
            MessageUser=request.user if request.user.is_authenticated else None,
            MessageSession=session_id,
            MessageRole='bot',
            MessageContent=reply,
            MessageMode=mode,
        )

        return JsonResponse({
            'status': 'success',
            'reply': reply,
            'mode': mode,
        })
    return JsonResponse({'status': 'error', 'message': '请求方式错误'})


def chat_history(request):
    """获取聊天历史"""
    session_id = request.GET.get('session_id', '')
    messages = ChatMessage.objects.filter(MessageSession=session_id)
    data = [{
        'role': msg.MessageRole,
        'content': msg.MessageContent,
        'mode': msg.MessageMode,
    } for msg in messages]
    return JsonResponse({'messages': data})


def keyword_match(message):
    """关键词匹配回复"""
    rules = KeywordRule.objects.filter(IsEnabled=True).order_by('-RulePriority')
    for rule in rules:
        if rule.RuleKeyword in message:
            # 如果有关联分类，尝试推荐商品
            if rule.RuleCategory:
                products = Product.objects.filter(
                    ProductCategory=rule.RuleCategory,
                    IsOnSale=True
                )[:3]
                if products:
                    product_list = '\n'.join([
                        f'  · {p.ProductName} - ¥{p.ProductPrice}'
                        for p in products
                    ])
                    return f'{rule.RuleResponse}\n\n📦 为您推荐以下商品：\n{product_list}', 'keyword'
            return rule.RuleResponse, 'keyword'
    return None, None


def llm_chat(message, session_id):
    """调用智谱AI大模型"""
    try:
        # 按分类组织商品信息
        categories = Category.objects.filter(IsVisible=True).order_by('CategorySort')
        category_blocks = []
        for cat in categories:
            products = Product.objects.filter(
                ProductCategory=cat, IsOnSale=True
            )[:6]
            if products:
                product_list = '\n'.join([
                    f'  · {p.ProductName} - ¥{p.ProductPrice}'
                    for p in products
                ])
                category_blocks.append(f'【{cat.CategoryName}】\n{product_list}')

        product_context = '\n\n'.join(category_blocks)
        category_names = '、'.join([c.CategoryName for c in categories])

        # 获取聊天历史（最近4轮）
        history = ChatMessage.objects.filter(MessageSession=session_id).order_by('CreateTime')[:8]
        history_messages = []
        for msg in history:
            role = 'assistant' if msg.MessageRole == 'bot' else 'user'
            history_messages.append({"role": role, "content": msg.MessageContent})

        system_prompt = f"""你是一个数码潮品商城的智能导购助手，名叫"小M"，性格热情专业。

商城经营以下品类：{category_names}

当前在售商品如下（按分类列出）：

{product_context}

请根据用户的需求推荐合适的商品。规则：
1. 推荐的商品必须是上面列表中明确列出的，不要编造不在列表中的商品
2. 从相关分类中挑选最适合的商品进行推荐
3. 回复控制在200字以内，简洁热情，可加emoji"""

        payload = {
            "model": settings.CHATBOT_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                *history_messages,
                {"role": "user", "content": message},
            ],
            "temperature": 0.7,
            "max_tokens": 500,
        }

        headers = {
            "Authorization": f"Bearer {settings.CHATBOT_API_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            settings.CHATBOT_API_URL,
            json=payload,
            headers=headers,
            timeout=30,
        )

        if response.status_code == 200:
            result = response.json()
            reply = result['choices'][0]['message']['content']
            return reply, 'llm'
        else:
            print(f'LLM API Error: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'LLM API Error: {e}')

    return None, None


def get_default_reply():
    """默认回复"""
    return """您好！我是智能导购助手 🤖

以下是一些您可以尝试的查询：
• 📱 推荐手机
• 💻 笔记本电脑
• 🎧 耳机推荐
• ⌚ 智能手表
• 🎮 游戏外设
• 🔌 充电配件

请问有什么可以帮您的吗？"""
