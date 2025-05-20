from googletrans import Translator

def translate_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, src="en", dest="hi")
    return translated_text.text

# Taking user input
english_text = input("Enter text in English: ")

# Translating to Hindi
hindi_translation = translate_to_hindi(english_text)

# Display the result
print("Translated text in Hindi:", hindi_translation)
