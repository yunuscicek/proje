from googletrans import Translator

translator = Translator()


result = translator.translate('shift', dest="tr")

# print(result.)


print(result.extra_data["parsed"][6][0][0][0][5][0][0])
print(result.extra_data["parsed"][6][1][0][0][5][0][0])
print(result.extra_data["parsed"][6][2][0][0][5][0][0])
print(result.extra_data["parsed"][6][3][0][0][5][0][0])
print(result.extra_data["parsed"][6][4][0][0][5][0][0])
print(result.extra_data["parsed"][6][5][0][0][5][0][0])
print(result.extra_data["parsed"][6][6][0][0][5][0][0])
print(result.extra_data["parsed"][6][7][0][0][5][0][0])
print(result.extra_data["parsed"][6][8][0][0][5][0][0])