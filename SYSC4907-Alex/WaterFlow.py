import RPi.GPIO as IO
import time, sys

FLOW_SENSOR = # Enter GPIO BCM number here
IO.setmode(GPIO.BCM)
IO.setup(FLOW_SENSOR, IO.IN, pull_up_down = IO.PUD_UP)

def measureFlow(channel):
    count += 1

IO.add_event_detect(FLOW_SENSOR, IO.FALLING, callback = measureFlow)

except KeyboardInterrupt:
    print("Keyboard interrupt detected")
    IO.cleanup()
    sys.exit()
    