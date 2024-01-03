from googletrans import Translator
import time

translator = Translator()

def Ceviri(kelime):
    zamanBaslangic = time.time()
    ceviri = ""
    result = translator.translate(kelime, dest="tr")
    ceviri = result.text + "\n"
    print("Google: ")
    print(time.time() - zamanBaslangic)
    
    for i in range(1000):
       
        try:

            ceviri = ceviri + result.extra_data["parsed"][6][i][0][0][5][0][0] + "\n"
        
        except IndexError:

            break
    
    return ceviri


def GoogleTranslateCumleCeviri(cumle):
    
    result = translator.translate(cumle, dest="tr")
    
    return result.text