from googletrans import Translator

translator = Translator()

translate = translator.translate("İyi akşamlar.", dest="english")
print(translate.text)
