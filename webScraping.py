from bs4 import BeautifulSoup
import requests
import time
import webbrowser

#precioDeseado = int(input("¿Cual es su precio deseado?: "))
#print("Accediendo a la web..")
#time.sleep(2)
#print("Verificando el precio..")
#time.sleep(2)
#print("Aguarde por favor...")
#time.sleep(1)

precioDeseado = 50

url = requests.get("https://computacion.mercadolibre.com.ar/computacion/procesador")
soup = BeautifulSoup(url.content, "html.parser")#parsear la pagina web para acceder  a los elementos 
resultado = soup.find('span', {'class':'price-tag-fraction'})#pide dos cosas: nombre de la etiqueta y la clase donde se encuentra el precio
#para encontrar la clase del precio clicl derecho inspeccionar y encontraras al seleccionar el elemento de nombre te da etiqueta y nombre clase se hace lo mismo con los datos que queramos  

precioaActual_text = resultado.text
precioaActual = float (precioaActual_text)


#precioDeseado = precioDeseado

if precioaActual < precioDeseado:
    print(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en:  {'$'+str(precioaActual)} ")
    #print(" ")
    #i = input('¿Quieres accerder a la web?: ')
    #if i == 'y':
        #pag = 'https://computacion.mercadolibre.com.ar/computacion/procesador'
        #webbrowser.open_new_tab(pag)
else:
    print("El precio sigue demasiado alto")
    print(precioaActual)