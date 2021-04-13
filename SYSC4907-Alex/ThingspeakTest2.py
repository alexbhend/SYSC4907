from ThingSpeak import thingspeak_post
import time

print("Sent newJob1 message at: " + str(time.time()))
thingspeak_post("111", "newJob", "", "", "", "17:50:00-17:50:30")
