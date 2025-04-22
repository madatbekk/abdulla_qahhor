from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, MenuButtonCommands
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from telegram.ext import filters

TOKEN = "7671995152:AAEe-UEx1QxMMFl05zezurpAA3PVRJxpgJw"

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

Temirchi oilasida tugʻilgan. Bolaligi Qoʻqon va uning atrofidagi qishloqlarda oʻtdi. Oqqoʻrgʻon qishlogʻidagi Mamajon qorining usuli savtiya maktabida tahsil koʻrdi. Oilasi Qoʻqonga koʻchib kelgach „Istiqlol“ nomli shoʻro maktabiga oʻqishga kiradi, undan keyin internat, „Kommuna“, „Namuna“ maktablarida, soʻng bilim yurtida tahsil koʻradi. 

Bilim yurtining „Adib“ qoʻlyozma jurnalida dastlabki mashqlari bilan qatnashadi. Toshkentdagi „Qizil Oʻzbekistan“ gazetasi tahririyatining „Ishchi-batrak maktublari“ varaqasiga muharrirlik qildi (1925). U gazetada ishlash jarayonida Oʻrta Osiyo davlat universitetining ishchilar fakultetini tamomlaydi (1928). 

Abdulla Qahhor yana Qoʻqonga borib, dastlab oʻqituvchilarni qayta tayyorlash kursida muallimlik qiladi; koʻp oʻtmay „Yangi Fargʻona“ viloyat gazetasiga kotib va „Chigʻiriq“ hajviy boʻlimiga mudir etib tayinlanadi (1929). 

Abdulla Qahhorning „Oy kuyganda“ ilk hajviy sheʼri „Mushtum“ jurnalida Norin shilpiq taxallusi ostida bosildi (2004). Soʻng uning bir qancha hajviy sheʼr va hikoyalari „Mushtum“, „Yangi yoʻl“ jurnallari va „Qizil Oʻzbekistan“ gazetasida Mavlon kufur, Gulyor, Nish, Erkaboy, E-voy kabi taxalluslar ostida eʼlon qilindi. 

Abdulla Qahhor 30-yillarda yana Toshkentga qaytadi va Oʻrta Osiyo davlat universitetining pedagogika fakultetiga oʻqishga kiradi (1930), ayni paytda „Sovet adabiyoti“ jurnalida mas'ul kotib vazifasini bajaradi. 

Oʻzdavnashrda muharrir va tarjimon (1935–1953). 1954–1956-yillarda Oʻzbekiston yozuvchilari uyushmasi boshqaruvining raisi. 

Abdulla Qahhor umrining oxirlarida davolanish uchun Moskvaga boradi va oʻsha yerda vafot etadi. Toshkentdagi Chigʻatoy qabristoniga dafn etiladi."""
    await update.message.reply_text(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Abdulla Qahhor hayoti":
        await hayoti(update, context)
    elif text == "Ijodi":
        await update.message.reply_text("Ijodi bo'limi tayyorlanmoqda...")
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
