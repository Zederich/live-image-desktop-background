import pythoncom
from urllib import request
from win32com.shell import shell, shellcon
from time import sleep
from os import environ

pathtoimg = environ['TEMP']+"\\bg.jpg"  #The file bg.jpg in the temp folder

print(pathtoimg)

settings = open(environ['APPDATA']+"\\livewebimagedesktop\\settings.txt")  #Settings file

lines = []
count = 0
for line in settings:
    count += 1  
    lines.append(line)

imgurl = lines[0]
delay = float(lines[1])
print(delay)

def get_image():
    f = open(pathtoimg, 'wb')           #Open/Create image
    f.write(request.urlopen(imgurl).read())  #Get web image and overwrite
    f.close()

while 1: #Forever
    get_image()
    iad = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None,
          pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
    iad.SetWallpaper(pathtoimg, 0)  #Set wallpaper
    iad.ApplyChanges(shellcon.AD_APPLY_ALL)
    sleep(delay) #Wait (seconds)
