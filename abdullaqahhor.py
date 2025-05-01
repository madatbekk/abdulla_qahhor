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
    text = """Abdulla Qahhor (1907-yil 17-sentyabrda Qoʻqon–1968-yil 25-mayda, Moskva ) — Oʻzbekiston xalq yozuvchisi (1967). Temirchi oilasida tugʻilgan. Bolaligi Qoʻqon va uning atrofidagi qishloqlarda oʻtdi. Oqqoʻrgʻon qishlogʻidagi Mamajon qorining usuli savtiya maktabida tahsil koʻrdi. Oilasi Qoʻqonga koʻchib kelgach „Istiqlol“ nomli shoʻro maktabiga oʻqishga kiradi, undan keyin internat, „Kommuna“, „Namuna“ maktablarida, soʻng bilim yurtida tahsil koʻradi. Bilim yurtining „Adib“ qoʻlyozma jurnalida dastlabki mashqlari bilan qatnashadi. Toshkentdagi „Qizil Oʻzbekiston“ gazetasi tahririyatining „Ishchi-batrak maktublari“ varaqasiga muharrirlik qildi (1925). U gazetada ishlash jarayonida Oʻrta Osiyo davlat universitetining ishchilar fakultetini tamomlaydi (1928). Abdulla Qahhor yana Qoʻqonga borib, dastlab oʻqituvchilarni qayta tayyorlash kursida muallimlik qiladi; koʻp oʻtmay „Yangi Fargʻona“ viloyat gazetasiga kotib va „Chigʻiriq“ hajviy boʻlimiga mudir etib tayinlanadi (1929). Abdulla Qahhorning „Oy kuyganda“ ilk hajviy sheʼri „Mushtum“ jurnalida Norin shilpiq taxallusi ostida bosildi (1924). Soʻng uning bir qancha hajviy sheʼr va hikoyalari „Mushtum“, „Yangi yoʻl“ jurnallari va „Qizil Oʻzbekiston“ gazetasida Mavlon kufur, Gulyor, Nish, Erkaboy, E-voy kabi taxalluslar ostida eʼlon qilindi. Abdulla Qahhor 30-yillarda yana Toshkentga qaytadi va Oʻrta Osiyo davlat universitetining pedagogika fakultetiga oʻqishga kiradi (1930), ayni paytda „Sovet adabiyoti“ jurnalida mas’ul kotib vazifasini bajaradi. Oʻzdavnashrda muharrir va tarjimon (1935–1953). 1954–1956-yillarda Oʻzbekiston yozuvchilari uyushmasi boshqaruvining raisi. Abdulla Qahhor umrining oxirlarida davolanish uchun Moskvaga boradi va oʻsha yerda vafot etadi. Toshkentdagi Chigʻatoy qabristoniga dafn etiladi.
"""
    await update.message.reply_text(text)

async def ijodi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    full_text = """Ijodi
Abdulla Qahhor ijodi sheʼriyat bilan boshlangan boʻlsada, uning adabiy merosi negizini nasriy asarlar tashkil etadi. „Boshsiz odam“ (1929) hikoyasi chop etilgan vaqtdan boshlab umrining oxirigacha hikoya, ocherk, publitsistika, qissa va roman janrlarida samarali ijod qildi. Abdulla Qahhorning dastlabki ijodidagi „Qishloq hukm ostida“ qissasi (1932) shoʻro mafkurasi asosida yozilgan. Uning „Boshsiz odam“ hikoyasi bilan boshlangan hikoyanavislik faoliyatida esa tarixiy oʻtmish aks ettirilgan. „Qoʻshchinor chiroqlari“ (1951) romanida (dastlabki varianti „Qoʻshchinor“, 1946) jamoalashtirish davrining voqealari badiiy tasvirlangan.

„Sarob“ romani
Abdulla Qahhorning 30-yillardagi ijodida uning birinchi romani – „Sarob“ muhim oʻrinni egallaydi. Yozuvchining ushbu romani bosh qahramon Saidiyning faoliyatini koʻrsatishga qaratilgan, yana unda 20-yillarning 2-yarmidagi oʻzbek xalqi hayotining maishiy, etnografik, iqtisodiy va maʼnaviy manzaralari yaqqol aks etib turadi. „Sarob“ keng mavzuli roman boʻlgani uchun yozuvchi oʻzining badiiy niyatini yalangʻoch holda koʻrsatmay, uni shu davr hayotining boshqa manzaralari koʻrinishida reallashtirishga uringan. Voqealar tasvirida yozuvchi hayot haqiqatini saqlab qolgan.

Mashhur asarlari

Abdulla Qahhor oʻrinli soʻz qoʻllash mahoratini puxta egallagan adibdir. Ijodida voqelikni realistik talqin etish ustuvorlik qiladi. Adib serqirra ijodkor sifatida adabiyotning deyarli barcha tur va janrlarida qalam tebratgan. „Olam yasharadi“ nomli birinchi hikoyalar toʻplami 1932-yilda bosilgan. Abdulla Qahhor ijodiy hayoti davomida 40 dan ziyod asar eʼlon qilgan. Bu kitoblar orasida 30 ga yaqin hikoyalar ham boʻlib, ular oʻzbek adabiyotida hikoya janrining badiiy ufqlarini kengaytirgani bilan ahamiyatlidir. Abdulla Qahhorning nasriy asarlari orasida „Qoʻshchinor chiroqlari“ romani hamda „Sinchalak“ (1958), „Oʻtmishdan ertaklar“ (1965) va „Muhabbat“ (1968) qissalari muhim oʻrin tutadi. Undan tashqari „Boshsiz odam“, „Anor“, „Bemor“, „Oʻgʻri“, „Dahshat“, „Millatchilar“, „Sanʼatkor“, „Adabiyot muallimi“, „Oʻjar“, „Asror bobo“ kabi oʻnlab hikoyalar yozgan. „Shohi soʻzana“ (1949), „Ogʻriq tishlar“ (1954), „Tobutdan tovush“ (1962), „Ayajonlarim“ (1966) nomli komediyalar muallifi. Feletonlar, adabiy-tanqidiy maqolalar ham yozgan.

Komediyalari
Abdulla Qahhorning isteʼdodi uchun komediya janri ham yaqin edi. Buni sezgan yozuvchi 50-yillar arafasida dramaturgiya sohasida ham qalam tebratib, shu davrning muhim mavzularidan biri – qoʻriq yerlarni oʻzlashtirish mavzuida „Shohi soʻzana“ („Yangi yer“, 1949–1953) komediyasini yaratdi. Shuni aytish lozimki, bu komediyada qoʻriq yerlarning – Mirzachoʻlning oʻzlashtirilishidan koʻra baʼzi kishilar ongidagi shoʻrning bartaraf etilishi mavzui birinchi oʻringa olib chiqilgan. Urushdan keyingi oʻzbek adabiyotidagi asosiy konflikt – yangilik bilan eskilik oʻrtasidagi ziddiyat bu komediyada oʻzining teran badiiy tasvirini topgan. Bu asarda Abdulla Qahhor ustalik bilan kulgili holatlar yaratgan va hajviy boʻyoqlardan mohirona foydalangan holda konfliktni oʻziga xos ravishda hal qilgan. Ushbu komediya xorijiy mamlakatlar sahnasida ham oʻynalib, oʻzbek teatr sanʼatining kamol topib borayotganini namoyish etdi. Bundan ilhomlangan yozuvchi „Ogʻriq tishlar“ (1954), „Tobutdan tovush“ (1962) hamda „Ayajonlarim“ (1967) komediyalarini yaratdi. Bu asarlarda, xususan, „Tobutdan tovush“da oʻsha davr uchun xos boʻlgan illatlar hajv oʻti ostiga olindi. Ayniqsa soʻnggi asarda Abdulla Qahhor oʻziga xos nozik tuygʻu bilan jamiyatdan poraxoʻrlikdek dahshatli illatni tag-tomiri bilan yoʻqotish istagida uning ayrim koʻrinishlarini sahnaga olib chiqdi, u „Soʻnggi nusxalar“ nomi bilan ham sahna yuzini koʻrdi.
"""

    # Matnni 4096 belgidan oshmasligi uchun bo‘lib yuborish
    chunk_size = 4000
    for i in range(0, len(full_text), chunk_size):
        await update.message.reply_text(full_text[i:i + chunk_size])

async def send_hikoyalar_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # GitHub'dagi PDF fayl manzili
    pdf_url = "https://github.com/foydalanuvchi/repositoriy_nomi/raw/main/Hikoyalar.pdf"
    await update.message.reply_document(document=pdf_url, caption="Abdulla Qahhorning hikoyalar to'plami")

async def send_sarob_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # GitHub'dagi PDF fayl manzili
    pdf_url = "https://github.com/foydalanuvchi/repositoriy_nomi/raw/main/Sarob_roman.pdf"
    await update.message.reply_document(document=pdf_url, caption="Abdulla Qahhorning 'Sarob' romani")

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
    application = Application.builder().token(TOKEN).post_init(post_init).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()
