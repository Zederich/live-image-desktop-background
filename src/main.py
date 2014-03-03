#Live web image as desktop program
#Executes the program based on the settings and changes the background.
#Developed by Zederich (github.com/Zederich)
#The software is released into the public domain.
#For more information see LICENCE in the repository under <https://github.com/Zederich/live-image-desktop-background>

import pythoncom
from urllib.request import urlopen
from win32com.shell import shell, shellcon
from time import sleep
from os import environ
import tkinter.messagebox as messagebox #Won't work with from x import y outside of IDLE.

pathtoimg = "{0}\\bg.jpg".format(environ['TEMP'])  #The file bg.jpg in the temp folder

settings = open("{0}\\livewebimagedesktop\\settings.txt".format(environ['APPDATA']),'r')  #Settings file

#Read settings.txt line by line, faster than f.readline()
lines = []
count = 0
for line in settings:
    lines.append(line)

imgurl = lines[0]
delay = float(lines[1])
should_autodetect = lines[2].lower() == 'true' #Set autodetect to boolean True if string "true" in settings.txt


#Get filesize of the image
def getfilesize():
    opened = urlopen(imgurl)
    if "Content-Length" in opened.headers: #If content header available
        size = int(opened.headers["Content-Length"])
    else: #If no header available
        size = len (opened.read ());
    return size


if should_autodetect: #"true" on line 3 of settings.txt
    initialised = True #FIrst time looping, after program started
    while 1: #Forever
        if getfilesize() != fsize or initialised: #Make sure it enters the if for the first time.
            img = open(pathtoimg, 'wb')           #Open/Create image
            img.write(urlopen(imgurl).read())  #Get web image and overwrite
            img.close()
            iad = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None,
                  pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
            iad.SetWallpaper(pathtoimg, 0)  #Set wallpaper
            iad.ApplyChanges(shellcon.AD_APPLY_ALL)
            fsize = getfilesize() #set fsize so it can be compared to getfilesize() later.
        else:
            pass
        sleep(5) #Only checks for update every 5 seconds.
        if initialised: #Prevent the variable being changed every cycle.
            initialised = False
        else:
            pass

else:
    while 1: #Forever
        img = open(pathtoimg, 'wb')           #Open/Create image
        img.write(urlopen(imgurl).read())  #Get web image and overwrite
        img.close()
        iad = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None,
              pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
        iad.SetWallpaper(pathtoimg, 0)  #Set wallpaper
        iad.ApplyChanges(shellcon.AD_APPLY_ALL)
        sleep(delay)
