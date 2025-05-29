from googletrans import Translator
import logging
from googletrans.constants import DEFAULT_USER_AGENT
import random

logger = logging.getLogger(__name__)

class TranslationService:
    def __init__(self):
        self.translator = Translator(
            service_urls=[
                'translate.google.com',
                'translate.google.co.id',
            ],
            user_agent=DEFAULT_USER_AGENT,
            raise_exception=True
        )
    
    def _get_random_service_url(self):
        return random.choice(self.translator.service_urls)
    
    def translate(self, text, source, target):
        try:
            return self.translator.translate(
                text,
                src=source,
                dest=target,
                service_url=self._get_random_service_url()
            ).text
        except Exception as e:
            logger.error(f"Translation error: {e}")
            return None

    def translate_id_to_ar(self, text):
        return self.translate(text, 'id', 'ar')
    
    def translate_ar_to_id(self, text):
        return self.translate(text, 'ar', 'id')
