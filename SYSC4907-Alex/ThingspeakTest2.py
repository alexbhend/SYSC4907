from ThingSpeak import thingspeak_post
import time

print("Sent newJob1 message at: " + str(time.time()))
thingspeak_post("123", "newJob", "", "", "", "16:00:00-18:00:00")
time.sleep(16)
print("Sent newJob2 message at: " + str(time.time()))
thingspeak_post("123", "newJob", "", "", "", "17:00:00-18:00:00")
time.sleep(16)
print("Sent deleteJob message at: " + str(time.time()))
thingspeak_post("123", "deleteJob", "", "", "", "16:00:00-18:00:00")