import requests
from bs4 import BeautifulSoup as bs

url = "https://dictionary.cambridge.org/tr/sözlük/ingilizce/"
text = input("-->")   

url = f"{url}/{text}" 
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

page = requests.get(url, headers= header)
soup = bs(page.text, "html.parser")
translation = soup.find_all('div', {'class':'ddef_h'})


if page.status_code == 200:   
    
    print(page.url)
    
    for result in translation:
    
        print(result.text)

else:
    print("Failure")