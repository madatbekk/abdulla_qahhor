import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, MenuButtonCommands
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from telegram.ext import filters

async def set_menu_button(update: Update):
    await update.get_bot().set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonCommands()
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    welcome_message = f"Assalomu alaykum {user.first_name}, botga xush kelibsiz!\n\nMen Abdulla Qahhorning hayoti va ijodi haqida ma'lumot beruvchi botman. Quyidagi bo'limlardan o'zingizga keraklisini tanlang."

    menu_buttons = [
        [KeyboardButton("Abdulla Qahhor hayoti")],
        [KeyboardButton("Ijodi")],
        [KeyboardButton("Hikoyalari va to'plamlar")],
        [KeyboardButton("Romanlari")]
    ]
    reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)
    await set_menu_button(update)

async def hayoti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """Abdulla Qahhor (1907-yil 17-sentyabrda Qoʻqon–1968-yil 25-mayda, Moskva) — Oʻzbekiston xalq yozuvchisi (1967). 

Temirchi oilasida tugʻilgan... (matn shu yerda davom etadi, siz allaqachon bergan to‘liq hayoti matni)
"""
    await update.message.reply_text(text)

async def ijodi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    full_text = """Ijodi
Abdulla Qahhor ijodi sheʼriyat bilan boshlangan boʻlsada, uning adabiy merosi negizini nasriy asarlar tashkil etadi. „Boshsiz odam“ (1929) hikoyasi chop etilgan vaqtdan boshlab umrining oxirigacha hikoya, ocherk, publitsistika, qissa va roman janrlarida samarali ijod qildi. Abdulla Qahhorning dastlabki ijodidagi „Qishloq hukm ostida“ qissasi (1932) shoʻro mafkurasi asosida yozilgan. Uning „Boshsiz odam“ hikoyasi bilan boshlangan hikoyanavislik faoliyatida esa tarixiy oʻtmish aks ettirilgan. „Qoʻshchinor chiroqlari“ (1951) romanida (dastlabki varianti „Qoʻshchinor“, 1946) jamoalashtirish davrining voqealari badiiy tasvirlangan.

„Sarob“ romani
Abdulla Qahhorning 30-yillardagi ijodida uning birinchi romani – „Sarob“ muhim oʻrinni egallaydi. Yozuvchining ushbu romani bosh qahramon Saidiyning faoliyatini koʻrsatishga qaratilgan...


"""

    # Matnni 4096 belgidan oshmasligi uchun bo‘lib yuborish
    chunk_size = 4000
    for i in range(0, len(full_text), chunk_size):
        await update.message.reply_text(full_text[i:i + chunk_size])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Abdulla Qahhor hayoti":
        await hayoti(update, context)
    elif text == "Ijodi":
        await ijodi(update, context)
    elif text == "Hikoyalari va to'plamlar":
        await update.message.reply_text("Hikoyalari va to'plamlar bo'limi tayyorlanmoqda...")
    elif text == "Romanlari":
        await update.message.reply_text("Romanlari bo'limi tayyorlanmoqda...")
    else:
        await update.message.reply_text("Noto'g'ri buyruq. Iltimos, menyudan tanlang.")

async def post_init(application: Application):
    await application.bot.set_my_commands([
        ("start", "Botni ishga tushirish"),
    ])

def main():
    application = Application.builder().token(TOKEN).post_init(post_init).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()
