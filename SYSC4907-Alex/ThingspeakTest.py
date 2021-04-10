from ThingSpeak import thingspeak_post
import time


print("Sent start message at: " + str(time.time()))
thingspeak_post("123", "newJob", "", "", "", "14:00-18:00")