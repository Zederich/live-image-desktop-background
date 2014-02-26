import pythoncom
from urllib import request
from win32com.shell import shell, shellcon
from time import sleep
from os import environ

pathtoimg = environ['TEMP']+"\\bg.jpg"  #The file bg.jpg in the temp folder


def get_image():
    f = open(pathtoimg, 'wb')           #Open/Create image
    f.write(request.urlopen('http://lorempixel.com/sports/1900/1080/').read())  #Get web image and overwrite
    f.close()

while 1: #Forever
    get_image()
    iad = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None,
          pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
    iad.SetWallpaper(pathtoimg, 0)  #Set wallpaper
    iad.ApplyChanges(shellcon.AD_APPLY_ALL)
    sleep(60) #Wait (seconds)
