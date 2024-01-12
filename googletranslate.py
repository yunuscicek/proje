from googletrans import Translator

translator = Translator()

def Ceviri(kelime):

    split_text = kelime.splitlines()
    clean_text = "".join(split_text)
    kelime = clean_text
    ceviri = ""

    try:
        result = translator.translate(kelime, dest="tr")
    except:
        return "Error: Connection Failed"
    
    ceviri = result.text + "\n"
    
    for i in range(100):
        try:
            ceviri = ceviri + result.extra_data["parsed"][6][i][0][0][5][0][0] + "\n"
        except IndexError:
            break

    ceviri = ceviri.replace(".",". ")
    
    return ceviri
