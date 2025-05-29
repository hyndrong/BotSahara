from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from config import BOT_DESCRIPTION
from services.translator import TranslationService

translation_service = TranslationService()

def get_main_menu():
    """Membuat keyboard menu utama"""
    keyboard = [
        ['/id_ar Terjemahkan ID→AR'],
        ['/ar_id Terjemahkan AR→ID'],
        ['/help', '/about']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def start(update, context):
    """Handler untuk command /start"""
    menu = get_main_menu()
    update.message.reply_text(
        BOT_DESCRIPTION,
        reply_markup=menu,
        parse_mode='Markdown'
    )

def help_command(update, context):
    """Handler untuk command /help"""
    update.message.reply_text(
        "Cara menggunakan bot:\n\n"
        "1. Kirim teks dalam bahasa Indonesia atau Arab untuk terjemahan otomatis\n"
        "2. Atau gunakan perintah:\n"
        "/id_ar [teks] - Terjemahkan Indonesia ke Arab\n"
        "/ar_id [teks] - Terjemahkan Arab ke Indonesia\n\n"
        "Contoh: /id_ar Selamat pagi",
        reply_markup=get_main_menu()
    )

def about(update, context):
    """Handler untuk command /about"""
    update.message.reply_text(
        "🤖 Bot Penerjemah Indonesia-Arab\n\n"
        "Versi: 1.0\n"
        "Dibuat dengan Python dan Google Translate API\n"
        "Github: https://github.com/your-repo\n\n"
        "Gunakan /help untuk bantuan",
        reply_markup=get_main_menu()
    )

def translate_id_ar(update, context):
    """Handler untuk command /id_ar"""
    text = ' '.join(context.args)
    if not text:
        update.message.reply_text("Mohon sertakan teks untuk diterjemahkan. Contoh: /id_ar Selamat pagi")
        return
    
    translation = translation_service.translate_id_to_ar(text)
    if translation:
        update.message.reply_text(
            f"Terjemahan Indonesia → Arab:\n\n{translation}",
            reply_markup=get_main_menu()
        )
    else:
        update.message.reply_text("Gagal menerjemahkan. Silakan coba lagi.")

def translate_ar_id(update, context):
    """Handler untuk command /ar_id"""
    text = ' '.join(context.args)
    if not text:
        update.message.reply_text("Mohon sertakan teks untuk diterjemahkan. Contoh: /ar_id صباح الخير")
        return
    
    translation = translation_service.translate_ar_to_id(text)
    if translation:
        update.message.reply_text(
            f"Terjemahan Arab → Indonesia:\n\n{translation}",
            reply_markup=get_main_menu()
        )
    else:
        update.message.reply_text("Gagal menerjemahkan. Silakan coba lagi.")

def setup_command_handlers(dispatcher):
    """Mendaftarkan semua command handler"""
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about))
    dispatcher.add_handler(CommandHandler("id_ar", translate_id_ar))
    dispatcher.add_handler(CommandHandler("ar_id", translate_ar_id))