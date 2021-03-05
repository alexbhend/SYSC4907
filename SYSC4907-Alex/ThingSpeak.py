import requests
import urllib
import time
import json

READ_KEY = "473GSMPC4BD4R44T"
WRITE_KEY = "POEWLXNFCKIFB7ZX"

WRITE_URL = "https://api.thingspeak.com/update?api_key="
HEADER = "&field1={}&field2={}&field3={}&field4={}&field5={}"

READ_URL = "https://api.thingspeak.com/channels/1160881/feeds.json?api_key="
READ_FOOTER = "&results=2"

def thingspeak_post(userID, type, Litres, KWhrs, Actuate):
    header = HEADER.format(userID, type, Litres, KWhrs, Actuate)
    NEW_URL = WRITE_URL+WRITE_KEY+header
    try:
        reply = urllib.request.urlopen(NEW_URL)
        response = reply.getresponse()
        print(response.status, response.reason)
        data = response.read()
        print(data)
    except:
        print("connection failed")

def thingspeak_read():
    NEW_URL = READ_URL+READ_KEY+READ_FOOTER
    try:
        conn = requests.get(NEW_URL).json()
        userID = conn["field1"]
        type = conn["field2"]
        Litres = conn["field3"]
        KWhrs = conn["field4"]
        Actuate = conn["field5"]
        print("userID: " + userID + "    type: " + type + " Litres: " + Litres + "   KWhrs: " + KWhrs + "    Actuate: " + Actuate)
    except:
        print(conn.getresponse().status)
        print("data not retrieved")


thingspeak_read()

