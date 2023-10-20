import requests
from bs4 import BeautifulSoup

text = input('-->')

payload = {'text':text, 'op': 'translate'}
r = requests.get('https://translate.google.com/?sl=auto&tl=tr',params=payload)

if r.status_code ==200:
    soup = BeautifulSoup(r.text, 'html.parser')
    target_div = soup.find('div', class_='usGWQd')
    
    if target_div:
        div_content = target_div.text
        print("AAA"+div_content)
    else:
        print("BB.")
else:
    print("CC")