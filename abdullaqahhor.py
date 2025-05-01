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
    text = """Abdulla Qahhor (1907-yil 17-sentyabrda Qoʻqon–1968-yil 25-mayda, Moskva ) — Oʻzbekiston xalq yozuvchisi (1967). Temirchi oilasida tugʻilgan..."""
    await update.message.reply_text(text)

async def ijodi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    full_text = """Ijodi
Abdulla Qahhor ijodi sheʼriyat bilan boshlangan boʻlsada..."""
    
    chunk_size = 4000
    for i in range(0, len(full_text), chunk_size):
        await update.message.reply_text(full_text[i:i + chunk_size])

async def send_hikoyalar_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # To'g'ri raw havola
    pdf_url = "https://github.com/madatbekk/abdullaqahhor/raw/main/Hikoyalar.pdf"
    try:
        await update.message.reply_document(
            document=pdf_url,
            caption="Abdulla Qahhorning hikoyalar to'plami",
            timeout=30
        )
    except Exception as e:
        await update.message.reply_text("Hikoyalar yuklanmadi. Iltimos keyinroq urinib ko'ring.")
        print(f"PDF yuklashda xato: {e}")

async def send_sarob_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # To'g'ri raw havola
    pdf_url = "https://github.com/madatbekk/abdullaqahhor/raw/main/Sarob_roman.pdf"
    try:
        await update.message.reply_document(
            document=pdf_url,
            caption="Abdulla Qahhorning 'Sarob' romani",
            timeout=30
        )
    except Exception as e:
        await update.message.reply_text("Roman yuklanmadi. Iltimos keyinroq urinib ko'ring.")
        print(f"PDF yuklashda xato: {e}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Abdulla Qahhor hayoti":
        await hayoti(update, context)
    elif text == "Ijodi":
        await ijodi(update, context)
    elif text == "Hikoyalari va to'plamlar":
        await send_hikoyalar_pdf(update, context)
    elif text == "Romanlari":
        await send_sarob_pdf(update, context)
    else:
        await update.message.reply_text("Noto'g'ri buyruq. Iltimos, menyudan tanlang.")

async def post_init(application: Application):
    await application.bot.set_my_commands([
        ("start", "Botni ishga tushirish"),
    ])

def main():
    application = Application.builder() \
        .token(TOKEN) \
        .post_init(post_init) \
        .read_timeout(30) \
        .write_timeout(30) \
        .build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Polling ishlatish (webhook emas)
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )

if __name__ == '__main__':
    main()
