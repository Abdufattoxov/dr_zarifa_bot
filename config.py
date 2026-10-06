# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8441911382:AAEcI9J-_WduvaRJnHKxvArs5OPsgh6cUfc")

# Ruxsat berilgan xodimlar va rahbarlar ID lari (Bo'sh bo'lsa barcha xodimlar kirishi mumkin)
# Masalan: ADMIN_IDS = [123456789, 987654321]
ADMIN_IDS = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
