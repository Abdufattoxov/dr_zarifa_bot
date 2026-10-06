# -*- coding: utf-8 -*-
"""
Dr. Zarifa - Xodimlar va Rahbariyat uchun Ichki Ishchi Bot
Mavzular jadvali: Dr_Zarifa_Ginekologik_Mavzular_Jadval.pdf
Ssenariy qoidalari: dr-zarifa-reels
"""

import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import config
from topics import get_active_topics, SECTIONS
from reels_engine import generate_10_hooks, generate_full_reels_script

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Xodimlar sessiyasi uchun xotira
ACTIVE_TOPICS = get_active_topics()
USER_STATE = {} # user_id -> {"topic_index": 0, "hooks": [], "chosen_hook": None}

def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎬 Yangi Reels Ssenariy"), KeyboardButton(text="📊 Kunlik Analitika")],
            [KeyboardButton(text="📑 Mavzular Ro'yxati"), KeyboardButton(text="ℹ️ Bot Qo'llanmasi")]
        ],
        resize_keyboard=True
    )

def is_authorized(user_id: int) -> bool:
    if not config.ADMIN_IDS:
        return True
    return user_id in config.ADMIN_IDS

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if not is_authorized(message.from_user.id):
        await message.answer("Kechirasiz, ushbu bot faqat Dr. Zarifa xodimlari va rahbariyat uchun mo'ljallangan.")
        return

    USER_STATE[message.from_user.id] = {"topic_index": 0, "hooks": [], "chosen_hook": None}
    
    welcome_text = (
        "👋 **Assalomu alaykum, hamkasb!**\n\n"
        "Ushbu bot **Dr. Zarifa (@dr.zarifa_ginekolog)** sahifasi xodimlari va rahbariyati uchun maxsus ishchi kabinet hisoblanadi.\n\n"
        "📌 **Imkoniyatlar:**\n"
        "• Tasdiqlangan PDF-jadval asosida navbatdagi mavzularni olish;\n"
        "• Har bir mavzuga 10 ta professional ilmoq (hook) tanlash;\n"
        "• 30 soniyalik Reels ssenariysi va Chatplace uchun Lid-magnit loyihasini generatsiya qilish;\n"
        "• Instagram va Chatplace bo'yicha eng so'nggi analitikani kuzatish.\n\n"
        "Boshlash uchun quyidagi menyudan kerakli bo'limni tanlang:"
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard(), parse_mode="Markdown")

@dp.message(F.text == "🎬 Yangi Reels Ssenariy")
async def handle_new_reels(message: types.Message):
    if not is_authorized(message.from_user.id):
        return

    state = USER_STATE.setdefault(message.from_user.id, {"topic_index": 0, "hooks": [], "chosen_hook": None})
    idx = state["topic_index"]
    if idx >= len(ACTIVE_TOPICS):
        idx = 0
        state["topic_index"] = 0

    topic = ACTIVE_TOPICS[idx]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⚡️ 10 ta Hook Generatsiya Qilish", callback_data="gen_hooks")],
            [
                InlineKeyboardButton(text="⬅️ Oldingi", callback_data="prev_topic"),
                InlineKeyboardButton(text="Keyingi ➡️", callback_data="next_topic")
            ]
        ]
    )

    text = (
        f"🎯 **NAVBATDAGI KONTENT MAVZUSI ({idx + 1}/{len(ACTIVE_TOPICS)}):**\n\n"
        f"📂 **Bo'lim:** {topic['section_name']}\n"
        f"📌 **Mavzu №{topic['topic_num']}:** {topic['title']}\n\n"
        "Ushbu mavzu bo'yicha 10 ta professional hook ko'rish uchun quyidagi tugmani bosing:"
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

@dp.callback_query(F.data.in_(["next_topic", "prev_topic"]))
async def cb_navigate_topic(callback: types.CallbackQuery):
    state = USER_STATE.setdefault(callback.from_user.id, {"topic_index": 0, "hooks": [], "chosen_hook": None})
    if callback.data == "next_topic":
        state["topic_index"] = (state["topic_index"] + 1) % len(ACTIVE_TOPICS)
    else:
        state["topic_index"] = (state["topic_index"] - 1) % len(ACTIVE_TOPICS)

    idx = state["topic_index"]
    topic = ACTIVE_TOPICS[idx]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⚡️ 10 ta Hook Generatsiya Qilish", callback_data="gen_hooks")],
            [
                InlineKeyboardButton(text="⬅️ Oldingi", callback_data="prev_topic"),
                InlineKeyboardButton(text="Keyingi ➡️", callback_data="next_topic")
            ]
        ]
    )

    text = (
        f"🎯 **NAVBATDAGI KONTENT MAVZUSI ({idx + 1}/{len(ACTIVE_TOPICS)}):**\n\n"
        f"📂 **Bo'lim:** {topic['section_name']}\n"
        f"📌 **Mavzu №{topic['topic_num']}:** {topic['title']}\n\n"
        "Ushbu mavzu bo'yicha 10 ta professional hook ko'rish uchun quyidagi tugmani bosing:"
    )
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "gen_hooks")
async def cb_generate_hooks(callback: types.CallbackQuery):
    state = USER_STATE.setdefault(callback.from_user.id, {"topic_index": 0, "hooks": [], "chosen_hook": None})
    idx = state["topic_index"]
    topic = ACTIVE_TOPICS[idx]

    hooks = generate_10_hooks(topic["title"])
    state["hooks"] = hooks

    hooks_text = f"🔥 **{topic['title']}** mavzusi uchun 10 ta professional Hook:\n\n"
    for h in hooks:
        hooks_text += f"**{h['id']}. [{h['type']}]:**\n\"{h['text']}\"\n\n"

    hooks_text += "👇 **O'zingizga ma'qul kelgan Hook raqamini bosing:**"

    buttons_row1 = [InlineKeyboardButton(text=f"{i}", callback_data=f"hook_{i}") for i in range(1, 6)]
    buttons_row2 = [InlineKeyboardButton(text=f"{i}", callback_data=f"hook_{i}") for i in range(6, 11)]

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            buttons_row1,
            buttons_row2,
            [InlineKeyboardButton(text="🔄 Boshqa mavzu tanlash", callback_data="next_topic")]
        ]
    )

    await callback.message.edit_text(hooks_text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data.startswith("hook_"))
async def cb_pick_hook(callback: types.CallbackQuery):
    hook_id = int(callback.data.split("_")[1])
    state = USER_STATE.setdefault(callback.from_user.id, {"topic_index": 0, "hooks": [], "chosen_hook": None})
    
    hooks = state.get("hooks", [])
    chosen = next((h for h in hooks if h["id"] == hook_id), None)
    if not chosen:
        await callback.answer("Hook topilmadi, qaytadan urinib ko'ring.", show_alert=True)
        return

    state["chosen_hook"] = chosen

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Ha, Lid-magnit tayyorlansin", callback_data="lm_yes"),
                InlineKeyboardButton(text="❌ Yo'q, faqat ssenariy", callback_data="lm_no")
            ],
            [InlineKeyboardButton(text="⬅️ Boshqa hook tanlash", callback_data="gen_hooks")]
        ]
    )

    text = (
        f"✅ **Siz tanlagan Hook (№{chosen['id']}):**\n"
        f"*{chosen['type']}*\n"
        f"\"{chosen['text']}\"\n\n"
        "❓ **Ushbu mavzu bo'yicha Lid-magnit (PDF qo'llanma) tayyorlansinmi?**\n"
        "*(Lid-magnit tanlansa, 30 soniyalik ssenariy tomoshabinni ushbu qo'llanmani Direct'dan olishga undaydigan 'most' bilan yakunlanadi)*"
    )
    await callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data.in_(["lm_yes", "lm_no"]))
async def cb_generate_final(callback: types.CallbackQuery):
    with_lm = (callback.data == "lm_yes")
    state = USER_STATE.setdefault(callback.from_user.id, {"topic_index": 0, "hooks": [], "chosen_hook": None})
    idx = state["topic_index"]
    topic = ACTIVE_TOPICS[idx]
    chosen_hook = state.get("chosen_hook")

    if not chosen_hook:
        await callback.answer("Iltimos, avval hookni tanlang.", show_alert=True)
        return

    script_output = generate_full_reels_script(topic["title"], chosen_hook, with_lm)

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Keyingi mavzuga o'tish", callback_data="next_topic")],
            [InlineKeyboardButton(text="🔄 Boshqa hook sinab ko'rish", callback_data="gen_hooks")]
        ]
    )

    await callback.message.edit_text(script_output, reply_markup=kb, parse_mode="Markdown")
    await callback.answer("Ssenariy tayyorlandi!")

@dp.message(F.text == "📊 Kunlik Analitika")
async def handle_analytics(message: types.Message):
    if not is_authorized(message.from_user.id):
        return

    analytics_text = (
        "📊 **@dr.zarifa_ginekolog — KUNLIK ANALITIKA STATISTIKASI**\n\n"
        "👥 **Auditoriya:**\n"
        "• Obunachilar: **1 305 ta**\n"
        "• Asosiy qatlam: Ayollar (25–34 va 35–44 yosh)\n"
        "• Geografiya: O'zbekiston (88.3%), Sirdaryo, Buxoro, Samarqand, Toshkent vil.\n\n"
        "🎬 **Reels & Qamrov:**\n"
        "• Eng virusli video: **314 659 ko'rishlar**, 251 835 qamrov\n"
        "• Ulashishlar (Shares): **3 550 ta**\n"
        "• Izohlar: **3 635 ta**\n\n"
        "🤖 **Chatplace Voronkasi:**\n"
        "• Direct'ga kirgan mijozlar: **1 788 kishi**\n"
        "• Telegram kanalga o'tganlar (Lidlar): **293 kishi**\n"
        "• Konversiya darajasi: **16.39%**\n\n"
        "⏰ **Post chiqarish uchun eng yaxshi vaqtlar:**\n"
        "• Chorshanba, Payshanba, Juma: **10:00 – 11:00** va **17:00 – 18:00**"
    )
    await message.answer(analytics_text, parse_mode="Markdown")

@dp.message(F.text == "📑 Mavzular Ro'yxati")
async def handle_topic_list(message: types.Message):
    if not is_authorized(message.from_user.id):
        return

    text = "📑 **GINEKOLOGIK MAVZULAR JADVALI (PDF ASOSIDA):**\n\n"
    text += "✅ **1. Hayz sikli va gormonal o'zgarishlar (15 ta mavzu)** — *Tayyorlangan*\n\n"
    text += "🔄 **2. Infeksiyalar, yallig'lanish va gigiyena (13 ta mavzu)** — *Hozirgi navbat:*\n"
    text += "1. Molochnitsa (Kandidoz)\n2. Bakterial vaginoz\n3. Sistit va infeksiyalar\n4. Yashirin infeksiyalar\n5. Bachadon ortiqlari shamollashi...\n\n"
    text += "⏳ **3. Bachadon, tuxumdon va anatomik o'zgarishlar (10 ta mavzu)**\n"
    text += "⏳ **4. Homiladorlik, bepushtlik va defitsitlar (12 ta mavzu)**\n\n"
    text += "Ssenariy yaratishni boshlash uchun **'🎬 Yangi Reels Ssenariy'** tugmasini bosing."
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "ℹ️ Bot Qo'llanmasi")
async def handle_help(message: types.Message):
    help_text = (
        "ℹ️ **BOT BO'YICHA QO'LLANMA:**\n\n"
        "1. **Mavzu tanlash:** '🎬 Yangi Reels Ssenariy' bo'limiga kiring. Bot avtomatik 2-bo'limdan mavzuni taklif qiladi.\n"
        "2. **Hook generatsiyasi:** '10 ta Hook' tugmasini bosing. Sizga 10 xil psixologik uslubdagi ilmoqlar beriladi.\n"
        "3. **Tugmani tanlash:** Ma'qul kelgan raqamni (1-10) bosing.\n"
        "4. **Lid-magnit:** Agar qo'llanma kerak bo'lsa 'Ha'ni bosing. Ssenariy yakunida Chatplace uchun trigger so'z va lid-magnit loyihasi beriladi.\n"
        "5. **Analitika:** '📊 Kunlik Analitika' orqali Instagram va Chatplace natijalarini kuzatib boring."
    )
    await message.answer(help_text, parse_mode="Markdown")

async def main():
    logger.info("Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
