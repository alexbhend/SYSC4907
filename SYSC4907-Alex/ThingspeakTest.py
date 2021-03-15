from ThingSpeak import thingspeak_post
import time

count = 1

while True:
    if(count%2 == 0):
        thingspeak_post("123", "actuateNow", "", "", "False", "")
        count += 1
    else:
        thingspeak_post("123", "actuateNow", "", "", "True", "")
        count += 1
    time.sleep(10)
