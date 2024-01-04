from googletrans import Translator

translator = Translator()

def Ceviri(kelime):

    ceviri = ""
    result = translator.translate(kelime, dest="tr")
    ceviri = result.text + "\n"

    for i in range(100):
       
        try:

            ceviri = ceviri + result.extra_data["parsed"][6][i][0][0][5][0][0] + "\n"
        
        except IndexError:

            break
    
    return ceviri