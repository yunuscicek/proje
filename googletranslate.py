from googletrans import Translator

translator = Translator()

result = translator.translate("car", dest = "tr")
dict = result.extra_data['parsed']


print(dict)

