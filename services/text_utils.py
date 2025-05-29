def clean_text(text):
    """Membersihkan teks input"""
    if not text:
        return None
    return text.strip()

def is_arabic(text):
    """Deteksi sederhana apakah teks berbahasa Arab"""
    arabic_chars = set('ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي')
    return any(char in arabic_chars for char in text)

def format_translation(source, translation, source_lang, target_lang):
    """Format hasil terjemahan"""
    return f"""
🔹 *Bahasa Sumber* ({source_lang}):
{source}

🔸 *Terjemahan* ({target_lang}):
{translation}
"""