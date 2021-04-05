from ThingSpeak import thingspeak_post
import time


print("Sent start message at: " + str(time.time()))
thingspeak_post("1234", "actuateNow", "", "", "True", "")