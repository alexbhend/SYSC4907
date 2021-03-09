import RPi.GPIO as IO
import time, sys
from datetime import datetime
from ThingSpeak import thingspeak_post, thingspeak_read
import threading

IO.setwarnings(False)
IO.setmode(IO.BCM)

## Class definition for an Actuator thread
class ActuatorThread(threading.Thread):

## Init method for the thread
    def __init__(self, userID, pinID):
        threading.Thread.__init__(self)
        self.userID = userID
        self.pinID = pinID

## Run method for the thread
    def run(self):
        jobs = []
        print("Started running valve on pin:", self.pinID)
        while True:
            try:
                data = thingspeak_read()
                if((data["field1"] == self.userID) and (data["field2"] == "newJob")):
                    job = data["field6"]
                    jobs.append(job)
                if((data["field1"] == self.userID) and (data["field2"] == "deleteJob")):
                    for job in jobs:
                        if(job == data["field6"]):
                            jobs.remove(job)
                handleJobs(jobs, self.pinID)
            except KeyboardInterrupt:
                print("Keyboard interrupt detected")
                IO.cleanup()
                sys.exit()

## Function to handle the jobs inputted by the user
def handleJobs(jobs, valveNum):
    now = datetime.now()
    curr_time = now.strftime("%H:%M:%S")

    for job in jobs:
        start_time = job.split("-")[0]
        end_time = job.split("-")[1]
        if(checkTimes()):
            IO.output(valveNum, IO.HIGH)
        else:
            IO.output(valveNum, IO.LOW)

## Function to check if the valve should be open or not depending on the user's settings    
def checkTimes(startTime, endTime, curTime):
    start_hrs = int(startTime.split(":")[0])
    start_mins = int(startTime.split(":")[1])
    start_secs = int(startTime.split(":")[2].strip("\n"))
    start_in_secs = start_hrs*3600 + start_mins*60 _ start_secs

    end_hrs = int(endTime.split(":")[0])
    end_mins = int(endTime.split(":")[1])
    end_secs = int(endTime.split(":")[2].strip("\n"))
    end_in_secs = end_hrs*3600 + end_mins*60 + end_secs

    cur_hrs = int(curTime.split(":")[0])
    cur_mins = int(curTime.split(":")[1])
    cur_secs = int(curTime.split(":")[2].strip("\n"))
    cur_in_secs = cur_hrs*3600 + cur_mins*60 + cur_secs

    if((start_in_secs == cur_in_secs) or ((start_in_secs < cur_in_secs) and (end_in_secs > cur_in_secs))):
        return True
    else:
        return False

## Set up phase upon starting the program
print("------------------------------SET UP------------------------------")

userID = input("What is your user ID?: ")
threads = []
moreValves = True

## Determine how many valves are in use and set up GPIO for the valves along with the threads
while (moreValves):
    checkMore = input("Do you have more valves to input? (y/n): ")
    if(checkMore == "y"):
        valvePin = input("Which GPIO pin was used for the first valve?: ")
        IO.setup(valvePin, IO.OUT, initial = IO.LOW)
        newthread = ActuatorThread(userID, valvePin)
        newthread.start()
        threads.append(newthread)
        valve.join()
        moreValves = True
    else:
        moreValves = False
