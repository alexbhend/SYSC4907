from ThingSpeak import thingspeak_post
import time

count = 0

while count < 10:
    thingspeak_post("12345", "actuateNow", "", "", "True", "")
    time.sleep(16)
    thingspeak_post("12345", "actuateNow", "", "", "False", "")
    count += 1
    time.sleep(16)