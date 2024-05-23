import requests
from bs4 import BeautifulSoup as bs

def Ceviri(text):
    
    text = text.strip()
    text = text.replace(" ","-")
    ceviri = ""
    
    url = "https://dictionary.cambridge.org/tr/sözlük/ingilizce"
    url = f"{url}/{text}" 
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    
    try:

        page = requests.get(url, headers= header)
        
    except:

        return "Error: Connection Failed"
    
    soup = bs(page.text, "html.parser")
    translation = soup.find_all("div", {"class":"ddef_h"})
    i = 1
    
    if page.status_code == 200:   

        for result in translation:

            ceviri = ceviri + str(i) + ". "  
            ceviri = ceviri + result.text + "\n"
            i = i + 1

        i = 1
        return ceviri 
    
    else:

        return 1
