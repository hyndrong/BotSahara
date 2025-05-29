from googletrans import Translator
import logging

logger = logging.getLogger(__name__)

class TranslationService:
    def __init__(self):
        self.translator = Translator(service_urls=[
            'translate.google.com',
            'translate.google.co.id'
        ])
    
    def detect_language(self, text):
        try:
            return self.translator.detect(text).lang
        except Exception as e:
            logger.error(f"Error detecting language: {e}")
            return None
    
    def translate(self, text, source, target):
        try:
            result = self.translator.translate(text, src=source, dest=target)
            return result.text
        except Exception as e:
            logger.error(f"Translation error: {e}")
            return None

    def translate_id_to_ar(self, text):
        return self.translate(text, 'id', 'ar')
    
    def translate_ar_to_id(self, text):
        return self.translate(text, 'ar', 'id')