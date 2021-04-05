from ThingSpeak import thingspeak_post
import time


#thingspeak_post("123", "actuateNow", "", "", "False", "")
print("Sent start message at: " + str(time.time()))
thingspeak_post("1234", "actuateNow", "", "", "True", "")
time.sleep(5)
print("Sent end message at: " + str(time.time()))
thingspeak_post("1234", "actuateNow", "", "", "False", "")