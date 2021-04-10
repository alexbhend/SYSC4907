from ThingSpeak import thingspeak_post
import time

count = 0

while count < 25:
    print("Sent newJob message at: " + str(time.time()))
    thingspeak_post("123", "newJob", "", "", "", "14:00:00-18:00:00")
    time.sleep(16)
    print("Sent removeJob message at: " + str(time.time()))
    thingspeak_post("123", "deleteJob", "", "", "", "14:00:00-18:00:00")
    count += 1
    time.sleep(16)