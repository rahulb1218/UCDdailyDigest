import imp
import pytextnow as pytn
import os
from tercero import getTerceroLunch
from cuarto import getCuartoLunch
from segundo import getSegundoLunch
client = pytn.Client("rbudhiraja", sid_cookie = "SID_COOKIE", csrf_url = "CSRF_URL")

for filename in os.listdir("profiles"):
   with open(os.path.join("profiles", filename), 'r') as f:
        text = f.read()
        text = text.split(" ")
        if "3" in text and "a" in text:
            menu = getTerceroLunch()
            client.send_sms(text[0], "Lunch at Tercero DC today includes: ")
            client.send_sms(text[0], menu)
        if "3" in text and "b" in text:
            menu = getSegundoLunch()
            client.send_sms(text[0], "Lunch at Segundo DC today includes: ")
            client.send_sms(text[0], menu)
        if "3" in text and "c" in text:
            menu = getCuartoLunch()
            client.send_sms(text[0], "Lunch at Cuarto DC today includes: ")
            client.send_sms(text[0], menu)