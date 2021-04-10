from ThingSpeak import thingspeak_post
import time

print("Sent newJob1 message at: " + str(time.time()))
thingspeak_post("1234", "newJob", "", "", "", "16:00:00-18:00:00")
time.sleep(16)
print("Sent newJob2 message at: " + str(time.time()))
thingspeak_post("1234", "newJob", "", "", "", "17:00:00-18:00:00")
time.sleep(16)
print("Sent removeJob message at: " + str(time.time()))
thingspeak_post("1234", "removeJob", "", "", "", "16:00:00-18:00:00")