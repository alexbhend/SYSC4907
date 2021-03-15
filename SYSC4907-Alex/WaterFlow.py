import RPi.GPIO as IO
import time, sys
from ThingSpeak import thingspeak_post
from ThingSpeak import thingspeak_read
import threading

# Can measure flow rate from 1-30 L/min
# Each pulse is about 2.25 mL or about 450 pulses / Litre
# Pulse freq. (Hz) / 7.5 is flow rate in L/min
# Want to take flow rate readings every 5 seconds
# 5V to Vcc (Red wire), GND to GND (Black wire)
# Sensor data (Yellow wire) to 4.7K to Pi pin to 10K to GND

IO.setwarnings(False)
IO.setmode(IO.BCM)

class WaterflowThread(threading.Thread):
    def __init__(self, userID, flowPin):
        threading.Thread.__init__(self)
        self.userID = userID
        self.flowPin = int(flowPin)
    
    def run(self):
        print("Started running water meter for user: ", self.userID)

        count = 0
        litreInPulses = 450
        inactivitySecs = 4
        waterEventTime = time.time() + inactivitySecs
        flowMeter = IO.input(self.flowPin)

        while True:
            #try:
                waterFlow = IO.input(self.flowPin)
                if (waterFlow != flowMeter):
                    count += 1
                    flowMeter = waterFlow
                    waterEventTime = time.time() + inactivitySecs
                else:
                    if(time.time() > waterEventTime):
                        thingspeak_post(self.userID, "waterUpdate", round((float(count)/float(litreInPulses)), 3), "", "", "")
                        waterEventTime = time.time() + inactivitySecs
                        count = 0
            #except KeyboardInterrupt:
                #print("Keyboard interrupt detected")
                #IO.cleanup()
                #sys.exit()

## Set up phase upon starting the program
print("------------------------------SET UP------------------------------")

threads = []
userID = input("What is your user ID?: ")
flowPin = input("Which GPIO pin was used for the flow sensor?: ")
IO.setup(int(flowPin), IO.IN, pull_up_down = IO.PUD_UP)
newthread = WaterflowThread(userID, flowPin)
newthread.start()
threads.append(newthread)

for t in threads:
    t.join()
