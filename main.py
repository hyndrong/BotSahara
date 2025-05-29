from telegram.ext import Updater, Dispatcher
from config import TELEGRAM_TOKEN
from handlers.command_handler import setup_command_handlers
from handlers.message_handler import setup_message_handlers
import logging
from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health():
    return "OK", 200

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Inisialisasi bot dengan request timeout
        updater = Updater(
            TELEGRAM_TOKEN,
            use_context=True,
            request_kwargs={
                'read_timeout': 20,
                'connect_timeout': 20
            }
        )
        
        dispatcher = updater.dispatcher
        
        # Setup handlers
        setup_command_handlers(dispatcher)
        setup_message_handlers(dispatcher)
        
        # Mulai bot
        logger.info("Bot sedang berjalan...")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"Error saat menjalankan bot: {e}")

if __name__ == '__main__':
    main()
