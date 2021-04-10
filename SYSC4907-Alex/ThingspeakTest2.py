from ThingSpeak import thingspeak_post
import time

print("Sent newJob1 message at: " + str(time.time()))
thingspeak_post("123", "newJob", "", "", "", "14:00:00-15:37:00")
time.sleep(16)
print("Sent deleteJob message at: " + str(time.time()))
thingspeak_post("123", "deleteJob", "", "", "", "14:00:00-15:37:00")