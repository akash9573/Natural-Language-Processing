from transformers import pipeline

# Load translation pipeline
translator = pipeline("translation_en_to_fr")

def translate_text(text):
    translation = translator(text)
    return translation[0]['translation_text']

text = "Hello, how are you?"
translated_text = translate_text(text)
print(translated_text)
