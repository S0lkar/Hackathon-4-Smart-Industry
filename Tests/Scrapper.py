
# Librería para acceder a webs
# pip install urllib3
from urllib.request import urlopen
print('\n\n')


# URL de prueba
url = 'https://www.repsol.com/es/conocenos/que-hacemos/index.cshtml'


page = urlopen(url)
print('\n\n')
html_bytes = page.read()
html = html_bytes.decode("utf-8")

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

print(title)

# ------------------------------------------------------------
# pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

lista_de_textos = soup.get_text().split('\n')

textaco = ''
for x in lista_de_textos:
    l = x.split(' ')
    #print(' '.join(l), str(len(l)))
    
    if len(l) > 10:
        textaco += ' '.join(l) + '\n'

print('"""')
print(textaco)
print('"""')


f = open('Info.txt', 'w')
f.write(textaco)
f.close()

print('\n\n')


import re

print(re.match('.*Te ofrecemos.*', textaco))