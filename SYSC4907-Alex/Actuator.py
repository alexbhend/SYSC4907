import RPi.GPIO as IO
import time, sys

SOLENOID_VALVE = 23 ## Enter pin number here

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(SOLENOID_VALVE, IO.OUT)

while True:
        IO.output(SOLENOID_VALVE, True)
        print("Opening valve")
        time.sleep(1)
        IO.output(SOLENOID_VALVE, False)
        print("Closing valve")
        time.sleep(5)
"""
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
        IO.cleanup()
        sys.exit()
"""
