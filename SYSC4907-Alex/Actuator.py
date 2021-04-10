import RPi.GPIO as IO
import time, sys
from datetime import datetime
from ThingSpeak import thingspeak_post
from ThingSpeak import thingspeak_read
import threading

IO.setwarnings(False)
IO.setmode(IO.BCM)

## Class definition for an Actuator thread
class ActuatorThread(threading.Thread):

## Init method for the thread
    def __init__(self, userID, pinID):
        threading.Thread.__init__(self)
        self.userID = int(userID)
        self.pinID = pinID

## Run method for the thread
    def run(self):
        jobs = []
        print("Started running valve on pin: " + str(self.pinID) + "\n")
        while True:
            data = thingspeak_read()
            tsUserID = (data["field1"])
            if((int(tsUserID) == self.userID) and (data["field2"] == "newJob")):
                job = data["field6"]
                if(checkIfJob(job, jobs)):
                    jobs.append(job)
                    print("New job received: ", job)
                    print(jobs)
            if((int(tsUserID) == self.userID) and (data["field2"] == "deleteJob")):
                job = data["field6"]
                if(not checkIfJob(job, jobs)):
                    jobs.remove(job)
                    print("Job: " + str(job) + " deleted successfully!")
                    print(jobs)
            if((int(tsUserID) == self.userID) and (data["field2"] == "actuateNow") and (data["field5"] == "True")):
                print("Opening valve: ", self.pinID)
                actuateNow(self.pinID)
            handleJobs(jobs, self.pinID)

## Function to handle the jobs inputted by the user and open/close valves accordingly
def handleJobs(jobs, valveNum):
    now = datetime.now()
    curr_time = now.strftime("%H:%M:%S")

    for job in jobs:
        start_time = job.split("-")[0]
        end_time = job.split("-")[1]
        if(checkTimes(start_time, end_time, curr_time)):
            print("Started: " + str(time.time()))
            IO.output(valveNum, IO.HIGH)
            print("Doing job: ", job)
        else:
            IO.output(valveNum, IO.LOW)
            print("Stopped: " + str(time.time()))

## Function to open/close the valve immediately
def actuateNow(valveNum):
    while True:
        data = thingspeak_read()
        openClose = data["field5"]
        if(openClose == "False"):
            IO.output(valveNum, IO.LOW)
            print("Closed at :" + str(time.time()))
            print("Closing valve: ", valveNum)
            break
        else:
            IO.output(valveNum, IO.HIGH)
            print("Opened at :" + str(time.time()))


## Function to check if the valve should be open or not depending on the user's settings    
def checkTimes(startTime, endTime, curTime):
    start_hrs = int(startTime.split(":")[0])
    start_mins = int(startTime.split(":")[1])
    start_secs = int(startTime.split(":")[2].strip("\n"))
    start_in_secs = start_hrs*3600 + start_mins*60 + start_secs

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

## Function to see if the job is already present in the list returns True if job not already present, False if already present
def checkIfJob(job, jobs):
    for j in jobs:
        if(j == job):
            return False
    return True

## Set up phase upon starting the program
print("------------------------------SET UP------------------------------")

userID = input("What is your user ID?: ")
threads = []
moreValves = True

## Determine how many valves are in use and set up GPIO for the valves along with the threads
while (moreValves):
    checkMore = input("Do you have more valves to input? (1 for yes, 0 for no): ")
    if(checkMore == 1):
        valvePin = input("Which GPIO pin was used for the valve?: ")
        IO.setup(valvePin, IO.OUT, initial = IO.LOW)
        newthread = ActuatorThread(userID, valvePin)
        newthread.start()
        threads.append(newthread)
        moreValves = True
    else:
        moreValves = False

for t in threads:
    t.join()
