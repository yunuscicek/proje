from googletrans import Translator

translator = Translator()
result = translator.translate("train",dest="tr")

print(result.extra_data['parsed'])