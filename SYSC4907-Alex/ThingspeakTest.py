from ThingSpeak import thingspeak_post
import time

thingspeak_post("123", "actuateNow", "", "", "True", "")

time.sleep(5)

thingspeak_post("123", "actuateNow", "", "", "False", "")