#SimpleRobocopyScript
#Originally designed to back up savefiles for videogames, but can back up any files that are expected to change often.
#Copies entire directory it is pointed to. Please use with care.
#Uses robocopy (designed for Windows)
from subprocess import call
from time import sleep, time, ctime

delay = 600 #Time between each backup. Use large numbers for lots of files.
path = f"REPLACE_ME" #path of files that need backing up go here.
dest = f"REPLACE_ME" #path of folder the files are sent to. Must contain "LATEST" and "SECONDARY" folders.
copy_command_1 = ["robocopy",f"{dest}/LATEST",f"{dest}/SECONDARY"]
copy_command_2 = ["robocopy",path,f"{dest}/LATEST"]

def Main(time):
    while True:
        call(copy_command_1)
        call(copy_command_2)
        print("BACKUP COMPLETE")
        Wait(time)

def Wait(x = 600):
    sleep(x)
    print(f"BACKUP START - {ctime(time())}")

Main(10)
