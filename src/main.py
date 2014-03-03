import pythoncom
from urllib.request import urlopen
from win32com.shell import shell, shellcon
from time import sleep
from os import environ
import tkinter.messagebox as messagebox

pathtoimg = "{0}\\bg.jpg".format(environ['TEMP'])  #The file bg.jpg in the temp folder

settings = open("{0}\\livewebimagedesktop\\settings.txt".format(environ['APPDATA']),'r')  #Settings file

lines = []
count = 0
for line in settings:
    lines.append(line)

imgurl = lines[0]
delay = float(lines[1])
print(lines[2].lower() == 'true')
should_autodetect = lines[2].lower() == 'true'
print(should_autodetect)
print(type(should_autodetect))


def getfilesize():
    opened = urlopen(imgurl)
    if "Content-Length" in opened.headers:
        size = int(opened.headers["Content-Length"])
    else:
        size = len (opened.read ());
        print("dl")
    return size


if should_autodetect:
    print("Auto")
    fsize = getfilesize()
    initialised = True
    while 1: #Forever
        if getfilesize() != fsize or initialised: #Make sure it enters the if for the first time.
            print("Updated")
            print(getfilesize())
            img = open(pathtoimg, 'wb')           #Open/Create image
            img.write(urlopen(imgurl).read())  #Get web image and overwrite
            img.close()
            iad = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None,
                  pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
            iad.SetWallpaper(pathtoimg, 0)  #Set wallpaper
            iad.ApplyChanges(shellcon.AD_APPLY_ALL)
            fsize = getfilesize()
        else:
            pass
        sleep(5)
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
        sleep(delay) #Wait (seconds)
