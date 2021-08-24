# ---------------------------------------------------Healthy Programmer------------------------------------------------------------------
from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        Stopper_typer = input()
        if Stopper_typer == stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

watertime2 = time()
watertime = 45*60 #45 minutes

eyetime2 = time()
eyetime = 30*60 #30 minutes

exertime2 = time()
exertime = 60*60 #1 hour

while True:
    if time() - watertime2 > watertime:
        print("Water Drinking time. Enter 'drank' to stop the Alarm")
        musicloop("D://water.mp3", "drank","Drank")
        log("Water drinking at")
        watertime2 = time()
    if time() - eyetime2 > eyetime:
        print("Eye Exercise time. Enter 'done' to stop the Alarm")
        musicloop("D://eye.mp3", "done")
        log("Eye exercise at")
        eyetime2 = time()
    if time() - exertime2 > exertime:
        print("Exercise time. Enter 'done' to stop the Alarm")
        musicloop("D://exercise.mp3", "done")
        log("Exercise at")
        exertime2 = time() 