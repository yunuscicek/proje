from googletrans import Translator

translator = Translator()


result = translator.translate('shift', dest="tr")

#print(result.text)


for i in range(1000):
    try:
        print(result.extra_data["parsed"][6][i][0][0][5][0][0])
    except IndexError:
        break
