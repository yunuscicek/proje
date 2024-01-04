import requests
from bs4 import BeautifulSoup as bs
import time

def Ceviri(text):
    
    text = text.replace(" ","-")

    zamanBaslangic = time.time()

    ceviri = ""
    url = "https://dictionary.cambridge.org/tr/sözlük/ingilizce/"
    url = f"{url}/{text}" 

    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    page = requests.get(url, headers= header)
    soup = bs(page.text, "html.parser")
    translation = soup.find_all('div', {'class':'ddef_h'})
    
    i = 1
    
    print("Cambridge: ")
    print(time.time() - zamanBaslangic)

    if page.status_code == 200:   
         
        for result in translation:
             
            ceviri = ceviri + str(i) + ". "  

            

            ceviri = ceviri + result.text + "\n"
            i = i + 1
        i = 1
        cambridge_ceviri = ceviri
        return ceviri 

    else:
        return 1

