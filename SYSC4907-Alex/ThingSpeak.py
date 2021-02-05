import httplib
import urllib
import time

def thingspeak_post(Litres, key):

        params = urllib.urlencode({'field1':Litres, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
       
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (response.status, response.reason)
            data = response.read()
            print(data)
            conn.close()
        except:
            print ("connection failed")