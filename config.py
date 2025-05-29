import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
BOT_DESCRIPTION = """
🕌 Bot Penerjemah Indonesia-Arab 🕌

Fitur:
- Terjemahkan teks Indonesia → Arab
- Terjemahkan teks Arab → Indonesia
- Deteksi otomatis bahasa

Gunakan perintah berikut:
/start - Memulai bot
/help - Menampilkan bantuan
/id_ar - Terjemahkan Indonesia ke Arab
/ar_id - Terjemahkan Arab ke Indonesia
/about - Tentang bot ini
"""