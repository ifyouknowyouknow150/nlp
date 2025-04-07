from googletrans import Translator


def translate_text(text, target_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"


# List of common language codes
language_codes = {
    "tamil": "ta",
    "hindi": "hi",
    "malayalam": "ml",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "chinese": "zh-cn",
    "japanese": "ja"
}

while True:
    text = input("Enter English text (or type 'exit' to quit): ")
    if text.lower() == "exit":
        break

    print("Available languages:", ", ".join(language_codes.keys()))
    lang = input("Enter target language: ").lower()

    if lang in language_codes:
        translated_text = translate_text(text, language_codes[lang])
        print(f"Translated ({lang}): {translated_text}\n")
    else:
        print("❌ Invalid language. Please try again.\n")
