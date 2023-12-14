from googletrans import Translator

translator = Translator()


def GoogleTranslateKelimeCeviri(kelime):
    
    ceviri = ""
    result = translator.translate(kelime, dest="tr")
    
    for i in range(1000):
       
        try:

            ceviri = ceviri + result.extra_data["parsed"][6][i][0][0][5][0][0] + "\n"
        
        except IndexError:

            break

    return ceviri


def GoogleTranslateCumleCeviri(cumle):
    
    result = translator.translate(cumle, dest="tr")
    
    return result.text