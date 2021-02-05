import RPi.GPIO as IO
import time, sys
from ThingSpeak import thingspeak_post

# Can measure flow rate from 1-30 L/min
# Each pulse is about 2.25 mL or about 450 pulses / Litre
# Pulse freq. (Hz) / 7.5 is flow rate in L/min
# Want to take flow rate readings every 5 seconds
# 5V to Vcc (Red wire), GND to GND (Black wire)
# Sensor data (Yellow wire) to 4.7K to Pi pin to 10K to GND

global count
count = 0

key = "POEWLXNFCKIFB7ZX"

FLOW_SENSOR = 14 # Enter GPIO BCM number here
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(FLOW_SENSOR, IO.IN, pull_up_down = IO.PUD_UP)

def measureFlow(channel):
    global count
    count += 1

IO.add_event_detect(FLOW_SENSOR, IO.FALLING, callback = measureFlow)

while True:
    AinL = round((float(count)/float(450)), 3)    # AinL is total water usage in litres
    print(str(AinL) + " L \n")
    thingspeak_post(AinL, key)
    time.sleep(5) # Update every 5 s

    try:
        None
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
        IO.cleanup()
        sys.exit()
    