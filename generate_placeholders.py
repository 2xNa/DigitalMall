"""Generate placeholder product images for DigitalMall (copyright-safe)."""
import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "media/products"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color palette for placeholders
COLORS = [
    "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7",
    "#DDA0DD", "#98D8C8", "#F7DC6F", "#BB8FCE", "#85C1E9",
    "#F1948A", "#82E0AA", "#F8C471", "#AED6F1", "#D7BDE2",
    "#A3E4D7", "#FADBD8", "#F9E79F", "#A9CCE3", "#D5F5E3",
    "#FAD7A0", "#E8DAEF", "#CCD1D1", "#D4E6F1", "#ABEBC6",
    "#F5CBA7", "#D2B4DE", "#A9DFBF", "#F0B27A", "#C39BD3",
]

PRODUCT_NAMES = [
    "iPhone 16 Pro Max", "Huawei Mate 70 Pro+", "Xiaomi 15 Ultra",
    "OPPO Find X8 Pro", "Redmi K80 Pro", "Samsung Galaxy S25 Ultra",
    "MacBook Pro 16 M4 Max", "ThinkPad X1 Carbon", "ASUS ROG Strix 8 Plus",
    "Huawei MateBook X Pro", "RedmiBook Pro 16", "iPad Pro 13 M4",
    "Huawei MatePad Pro 13.2", "Xiaomi Pad 7 Pro", "AirPods Pro 3",
    "Sony WH-1000XM6", "Huawei FreeBuds Pro 4", "Bose SoundLink Flex",
    "Apple Watch Ultra 3", "Huawei Watch GT 5 Pro", "Xiaomi Watch 9 Pro",
    "Sony A7R V", "DJI Mini 4 Pro", "GoPro Hero 13 Black",
    "Logitech G Pro X Superlight 2", "Razer Viper V4 Pro",
    "PS DualSense Edge", "Anker 140W Charger", "Xiaomi 20000mAh Power Bank",
    "iHealth Pulse Oximeter",
]

W, H = 600, 600
font_size = 32

try:
    font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", font_size)
except:
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

for i in range(30):
    img = Image.new("RGB", (W, H), COLORS[i])
    draw = ImageDraw.Draw(img)

    # Darker gradient overlay at the bottom
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    for y in range(H // 2, H):
        alpha = int(180 * (y - H // 2) / (H // 2))
        overlay_draw.line([(0, y), (W, y)], fill=(0, 0, 0, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(img)

    # Product icon emoji-like indicator
    icons = ["📱", "💻", "⌚️", "🎧", "📷", "🎮", "🔋", "⌨️"]
    icon_text = icons[i % len(icons)]
    try:
        icon_font = ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf", 100)
    except:
        icon_font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), icon_text, font=icon_font)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2, H // 2 - 120), icon_text, fill="white", font=icon_font)

    # Product name
    name = PRODUCT_NAMES[i]
    bbox = draw.textbbox((0, 0), name, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2, H // 2 + 40), name, fill="white", font=font)

    # Price tag indicator
    price_label = f"¥ {(i + 1) * 499 + 999}"
    try:
        price_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 26)
    except:
        price_font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), price_label, font=price_font)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2, H // 2 + 90), price_label, fill="#FFD700", font=price_font)

    # Product number
    num_label = f"#{i + 1:02d}"
    try:
        num_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 22)
    except:
        num_font = ImageFont.load_default()
    draw.text((20, 15), num_label, fill=(255, 255, 255, 120), font=num_font)

    # DigitalMall watermark
    draw.text((W - 160, H - 40), "DigitalMall", fill=(255, 255, 255, 60), font=num_font)

    fname = f"product_{i+1}.jpg"
    img.convert("RGB").save(os.path.join(OUTPUT_DIR, fname), "JPEG", quality=85)
    print(f"[OK] Created: {fname}")

print(f"\nAll 30 placeholder images generated in {OUTPUT_DIR}/")
