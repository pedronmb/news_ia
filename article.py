import requests 
from bs4 import BeautifulSoup
import curl


# Obtengo las noticias del sitio infobae.
url = 'https://www.infobae.com//politica/2023/12/14/patricia-bullrich-explico-como-sera-el-protocolo-antipiquetes-van-a-intervenir-todas-las-fuerzas-federales/'
page = requests.get(url)
#realizar el request con la libreria curl de python

# parseo el html de la pagina
soup = BeautifulSoup(page.content, 'html.parser')

titulos = soup.find_all('p')

header = soup.find('h1', class_='article-headline')

articulo = '<h1>' + header.text + '</h1><p>'
print(header.text)
print('//////////////////////')
# imprimir todos los titulos en pantalla
flag = False
for titulo in titulos:
    if flag == True:
        articulo = articulo + titulo.text + ' '
    
    flag = True
    #print(titulo.text)
     #titulohead = titulohead.find('a')
     #print(titulo.find_parent('a'))
    #print('\n')

articulo = articulo + '</p>'
print(articulo)