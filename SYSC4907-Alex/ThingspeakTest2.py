from ThingSpeak import thingspeak_post
import time

print("Sent end message at: " + str(time.time()))
thingspeak_post("1234", "actuateNow", "", "", "False", "")