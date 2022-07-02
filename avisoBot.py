from asyncio import constants
import requests
from setuptools import Require
from webScraping import  precioaActual 
from webScraping import  precioDeseado 

def telegram_bot_sendtext(bot_message):

    bot_token  = '5542670420:AAHlrK0ID2SzKVkqgSiPgv8nKgS2UBg-xHI'

    bot_chatID = '2049350472'

    enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(enviar_text)

    return response.json()


if precioaActual < precioDeseado:
    test = telegram_bot_sendtext(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en:  {'$'+str(precioaActual)}\nEnlace: https://computacion.mercadolibre.com.ar/computacion/procesador")
  
else:
    test = telegram_bot_sendtext(f" ¡El precio sigue muy alto! Esta en:  {'$'+str(precioaActual)}")


#constants puppeteer = Require('puppeteer-extra')
   
#await page.goto('https://www.youtube.com/watch?v=bKqqZi1HFjw&t=1s')
