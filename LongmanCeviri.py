import requests
from bs4 import BeautifulSoup as bs

def Ceviri(text):
    
    text = text.replace(" ","-")

    ceviri = ""
    url = "https://www.ldoceonline.com/dictionary"
    url = f"{url}/{text}" 
    
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    page = requests.get(url, headers= header)
    soup = bs(page.text, "html.parser")
    translation = soup.find_all('span', {'class':'DEF'})
    signpost = soup.find_all('span', {'class': 'SIGNPOST'})
    i = 1

    if page.status_code == 200:   
        
        for result in translation:
            
            ceviri = ceviri + str(i) + ". "  

            try:

                ceviri = ceviri + "[" + signpost[i-1].text + "] " 

            except:

                None

            ceviri = ceviri + result.text + "\n"
            i = i + 1

        i = 1
        longman_translated = ceviri
        return ceviri 

    else:
        
        return 1

