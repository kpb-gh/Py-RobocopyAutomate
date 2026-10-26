#SimpleRobocopyScript
#Originally designed to back up savefiles for videogames, but can back up any files that are expected to change often.
#Copies entire directory it is pointed to. Please use with care.
#Uses robocopy (designed for Windows)
from subprocess import call
from time import sleep, time, ctime
from sys import argv

delay = None #Time between each backup. Use large numbers for lots of files.
path = None  #path of files that need backing up go here.
dest = None  #path of folder the files are sent to. Must contain "LATEST" and "SECONDARY" folders.
ArgErrCheck()

if (path == None or dest == None):
    print("Error!")
    exit()

copy_command_1 = f"robocopy {dest}/LATEST {dest}/SECONDARY".split(" ")
copy_command_2 = f"robocopy {path} {dest}/LATEST".split(" ")

def Main(time):
    while True:
        call(copy_command_1)
        call(copy_command_2)
        print("BACKUP COMPLETE")
        Wait(time)

def Wait(x = 600):
    sleep(x)
    print(f"BACKUP START - {ctime(time())}")
    
def ArgErrCheck():
    #delay
    try:
        delay = int_TryParse(argv[1])
        if delay == None:
            delay = SafeIntInput("Enter delay between backups: ")
    except (IndexError):
        delay = SafeIntInput("Enter delay between backups: ")
    try: 
        path = argv[2]
    except (IndexError):
        path = input("Full path to files that need backing up: ")
    try:
        dest = argv[3]
    except (IndexError):
        dest = input("Full path to location of backups (MUST include LATEST and SECONDARY subfolders): ")

def SafeIntInput(msg="Input integer: "):
    x = None
    while (x == None):
        x = int_TryParse(input(msg))

def int_TryParse(string):
    try:
        return int(string)
    except ValueError:
        return None

Main(delay)
