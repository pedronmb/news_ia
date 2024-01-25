import requests 
import mysql.connector
from bs4 import BeautifulSoup

# Obtengo las noticias del sitio infobae.
url = 'https://www.infobae.com/'
page = requests.get(url)
# parseo el html de la pagina
soup = BeautifulSoup(page.content, 'html.parser')

titulos = soup.find_all('h2')

# Configuración de la conexión a la base de datos
config = {
    'user': 'phpmyadmin',
    'password': 'password',
    'host': 'localhost',
    'database': 'news',
    'raise_on_warnings': True
}

# Establecer la conexión
conexion = mysql.connector.connect(**config)
 # Crear un objeto cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# imprimir todos los titulos en pantalla

    #print(titulo.parent.get('href'))
    #titulohead = titulohead.find('a')
    #print(titulo.find_parent('a'))
    
    



try:

    for titulo in titulos:
        titulohead = titulo.find_parent('a')
        #obtener el texto de href de cada titulo
        if titulo.parent.get('href') is not None:
            print(titulo.parent.get('href'))
            #print('-------------------')
            contenido = titulo.parent.get('href')
            elementos = contenido.split('/')
            categoria = elementos[1]
            #print(len(elementos))
            # Consulta SQL para buscar un registro con los mismos valores
            sql_select = "SELECT * FROM articles WHERE url = '" + contenido + "'"

            # Ejecutar la consulta de búsqueda
            cursor.execute(sql_select)

            # Recuperar el primer resultado (si hay alguno)
            resultado = cursor.fetchone()

            if resultado:
                print("El registro ya existe. No se realizará la inserción.")
            else:
                # Consulta SQL para insertar un nuevo registro
                sql_insert = "INSERT INTO articles (url,category) VALUES ('" + contenido + "','" + categoria + "')"


                # Ejecutar la consulta de inserción
                cursor.execute(sql_insert)

                # Confirmar la transacción
                conexion.commit()

                print("Registro insertado correctamente.")

except mysql.connector.Error as err:
    print("Error: {}".format(err))

finally:
    # Cerrar el cursor y la conexión
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")
    
