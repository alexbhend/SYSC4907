import RPi.GPIO as IO
import time, sys

SOLENOID_VALVE = ## Enter pin number here

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(SOLENOID_VALVE, IO.OUT, initial = IO.LOW)

try:
    while True:
        IO.output(SOLENOID_VALVE, IO.HIGH)
        sleep(1)
        IO.output(SOLENOID_VALVE, IO.LOW)
        sleep(5)

except KeyboardInterrupt:
    print("Keyboard interrupt detected")
    IO.cleanup()
    sys.exit()

