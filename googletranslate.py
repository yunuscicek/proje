from googletrans import Translator

translator = Translator()

result = translator.translate("car", dest = "tr")

print(result.text)

