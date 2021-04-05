from ThingSpeak import thingspeak_post
import time


#thingspeak_post("123", "actuateNow", "", "", "False", "")
print("Sent message at: " + str(time.time()))
thingspeak_post("1234", "actuateNow", "", "", "True", "")
