from googletrans import Translator

translator = Translator()

result = translator.translate("kapı")
print(result.extra_data[1])
