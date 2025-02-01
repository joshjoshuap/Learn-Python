from translate import Translator
translator = Translator(to_lang="zh")

try:
    with open('./simple_projects/text_to_translate.txt', mode='r', encoding="utf-8") as text_file:
        text = text_file.read()
        translate_text = translator.translate(text)
    with open('./simple_projects/translated_text.txt', mode='w', encoding="utf-8") as translated_text_file:
        translated_text_file.write(translate_text)
except FileNotFoundError as error:
    print("File doesn't exist")
    print(error)