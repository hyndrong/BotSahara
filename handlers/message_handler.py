from telegram.ext import MessageHandler, Filters
from services.translator import TranslationService
from services.text_utils import clean_text, is_arabic, format_translation

translation_service = TranslationService()

def handle_text_message(update, context):
    text = clean_text(update.message.text)
    if not text:
        update.message.reply_text("Mohon kirim teks yang valid")
        return
    
    if is_arabic(text):
        # Terjemahkan Arab -> Indonesia
        translation = translation_service.translate_ar_to_id(text)
        if translation:
            response = format_translation(
                text, translation, 
                "Arab", "Indonesia"
            )
        else:
            response = "Gagal menerjemahkan Arab → Indonesia"
    else:
        # Terjemahkan Indonesia -> Arab
        translation = translation_service.translate_id_to_ar(text)
        if translation:
            response = format_translation(
                text, translation,
                "Indonesia", "Arab"
            )
        else:
            response = "Gagal menerjemahkan Indonesia → Arab"
    
    update.message.reply_text(
        response,
        parse_mode='Markdown'
    )

def setup_message_handlers(dispatcher):
    """Mendaftarkan message handler"""
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, handle_text_message)
    )