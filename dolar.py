# script para obtener el valor del dolar en pesos argentinos del sitio dolarhoy.com y guardarlo en base de datos mysql

# Obtengo el valor del dolar en pesos argentinos del sitio dolarhoy.com 

import requests 
from bs4 import BeautifulSoup
from datetime import datetime

# Obtengo el valor del dolar en pesos argentinos del sitio dolarhoy.com
url = 'https://www.dolarhoy.com/'
page = requests.get(url)
# parseo el html de la pagina
soup = BeautifulSoup(page.content, 'html.parser')

# busco la etiqueta a para ubicar e tipoo e cotizacion buscada dolar oficial
dolarofi = soup.find('a', href='/cotizaciondolaroficial')
dolarofi = dolarofi.find_parent('div') # busco el padre de la etiqueta a
dolarofiv = dolarofi.find('div', class_='venta') # busco la etiqueta div con la clase venta
dolarofiv = dolarofiv.find('div', class_='val') # busco la etiqueta div con la clase val

dolarofic = dolarofi.find('div', class_='compra')
dolarofic = dolarofic.find('div', class_='val')

# busco la etiqueta a para ubicar e tipoo e cotizacion buscada dolar bolsa
dolarbol = soup.find('a', href='/cotizaciondolarbolsa')
dolarbol = dolarbol.find_parent('div') # busco el padre de la etiqueta a
dolarbolv = dolarbol.find('div', class_='venta') # busco la etiqueta div con la clase venta
dolarbolv = dolarbolv.find('div', class_='val') # busco la etiqueta div con la clase val

dolarbolc = dolarbol.find('div', class_='compra')
dolarbolc = dolarbolc.find('div', class_='val')

# busco la etiqueta a para ubicar e tipoo e cotizacion buscada dolar contado con liqui
dolarccl = soup.find('a', href='/cotizaciondolarcontadoconliqui')
dolarccl = dolarccl.find_parent('div') # busco el padre de la etiqueta a
dolarcclv = dolarccl.find('div', class_='venta') # busco la etiqueta div con la clase venta
dolarcclv = dolarcclv.find('div', class_='val') # busco la etiqueta div con la clase val

dolarcclc = dolarccl.find('div', class_='compra')
dolarcclc = dolarcclc.find('div', class_='val')

# busco la etiqueta a para ubicar e tipoo e cotizacion buscada dolar cripto
dolarcri = soup.find(string='Dólar cripto') # busco la linea que contiene el texto Dolar cripto
dolarcri = dolarcri.find_parent('div') # busco el padre de la etiqueta a
dolarcriv = dolarcri.find('div', class_='venta') # busco la etiqueta div con la clase venta
dolarcriv = dolarcriv.find('div', class_='val') # busco la etiqueta div con la clase val

dolarcric = dolarcri.find('div', class_='compra')
dolarcric = dolarcric.find('div', class_='val')

# busco la etiqueta a para ubicar e tipoo e cotizacion buscada dolar blue
dolarblu = soup.find('a', href='/cotizaciondolarblue')
dolarblu = dolarblu.find_parent('div') # busco el padre de la etiqueta a
dolarbluv = dolarblu.find('div', class_='venta') # busco la etiqueta div con la clase venta
dolarbluv = dolarbluv.find('div', class_='val') # busco la etiqueta div con la clase val

dolarbluc = dolarblu.find('div', class_='compra')
dolarbluc = dolarbluc.find('div', class_='val')

# mostrar el valor del dolar
print('Dolar Oficial: ')
print(dolarofic.text + ' ' + dolarofiv.text)
print('Dolar Bolsa: ')
print(dolarbolc.text + ' ' + dolarbolv.text)
print('Dolar Contado con Liquidaion: ')
print(dolarcclc.text + ' ' + dolarcclv.text)
print('Dolar Cripto: ')
print(dolarcric.text + ' ' + dolarcriv.text)
print('Dolar Blue: ')
print(dolarbluc.text + ' ' + dolarbluv.text)


# Conecto a la base de datos
