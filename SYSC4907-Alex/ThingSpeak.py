import urllib
import httplib
import time
import json

CHANNEL_ID = "1160881"

READ_KEY = "473GSMPC4BD4R44T"
WRITE_KEY = "POEWLXNFCKIFB7ZX"

WRITE_URL = "https://api.thingspeak.com/update?api_key="
HEADER = "&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}"

READ_URL = "https://api.thingspeak.com/channels/1160881/feeds.json?api_key="
READ_FOOTER = "&results=2"

def thingspeak_post(userID, type, Litres, KWhrs, Actuate, timeslot):
    params = urllib.urlencode(
        {
            "field1": userID,
            "field2": type,
            "field3": Litres,
            "field4": KWhrs,
            "field5": Actuate,
            "field6": timeslot,
            "key": WRITE_KEY
            }
        )
    headers = {
            "Content-typZZe": "application/x-www-form-urlencoded",
            "Accept": "text/plain",
        }
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        print(data)
    except:
        print("connection failed")

def thingspeak_read():
    try:
        conn = urllib.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (CHANNEL_ID, READ_KEY))
        response = conn.read()
        data = json.loads(response)
        return data
    except:
        print(conn.getresponse().status)
        print("data not retrieved")
