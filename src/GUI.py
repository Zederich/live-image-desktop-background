#GUI for live web image as desktop program
#Edits the settings
#Developed by Zederich (github.com/Zederich)
#The software is released into the public domain.
#For more information see LICENCE in the repository under <https://github.com/Zederich/live-image-desktop-background>

from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font
from os import environ
import tkinter.messagebox as messagebox #Won't work with from import outside of IDLE.

root = Tk()

#Window Settings
root.wm_title("Settings - Live Image Desktop")
root.geometry("466x125")
root.resizable(0,0)


#Get original settings (for reset)
orig_settings = open("{0}\\livewebimagedesktop\\settings.txt".format(environ['APPDATA']),'r' )
to_write = orig_settings.read()
orig_settings.close()

#Will revert settings to how it was before program executed
def to_orig():
    settings = open("{0}\\livewebimagedesktop\\settings.txt".format(environ['APPDATA']),'w')  #Settings file
    settings.write(to_write)
    settings.close()
    messagebox.showinfo("Successfully Reset","The delay and time have been reset to:\n\n{0}".format(to_write))

#Disables delay field if button checked, disables otherwise
def toggle_delay():
    if should_auto.get() == "True":
        delay.configure(state="disabled")
    else:
        delay.configure(state="normal")

#Will save the entries into settings.txt. If shouldquit is true, the window will be closed afterwards
def save_new(shouldquit):
    print(should_auto.get())
    new_url = str(url.get()) #Get input for the URL.
    new_delay = delay.get()  #Get input for "delay"
    if "http://" in new_url and "." in new_url: #Some tests to make sure URL is valid.
        if new_delay.isnumeric():   #Check that the value for "delay" is a number
            if  1 <= float(new_delay) <= 36000:  #Check size of delay
                settings = open("{0}\\livewebimagedesktop\\settings.txt".format(environ['APPDATA']),'w')
                settings.write( "{0}\n{1}\n{2}".format(new_url,new_delay, should_auto.get()) )  #Wite new input values to file, including "True" if checkbox selected.
                settings.close()
                messagebox.showinfo("Done!","your changes have been saved. You will now need to restart the Live-Web-Image Program for the changes to take effect.")
                if shouldquit:  #Close window
                    root.destroy()
                else:
                    pass
            else:
                messagebox.showwarning("Number out of Range","The number you entered is too large/small. It must be between 1 and 36000.")
        else:
            messagebox.showwarning("Not a number","You entry for the delay is not a number.")
    else:
        messagebox.showwarning("Invalid URL","You have not entered a valid URL for the image.")

#Save and close window
def save_new_cls():
    save_new(True)

#Save but keep window open
def save_new_open():
    save_new(False)


#Labels under options
Label(root, text="URL of image").grid(row=1, padx=7, pady=0, columnspan=2)
Label(root, text="Delay (seconds)").grid(row=1, column=2, columnspan=2, padx=7, pady=0)

#Variable for checkbutton
should_auto = StringVar()

url = Entry(root, width = 24, font=("Verdana", 13))
delay = Spinbox(root, from_=5, to=3600, width=5, increment=5, font=("Verdana", 13))
autodetect = Checkbutton(root, text="Autodetect", var=should_auto, onvalue = "True", offvalue = "False", command=toggle_delay)

url.grid(row=0, column=0, padx=7, pady=5, columnspan=2, sticky=W)
delay.grid(row=0, column=3, padx=7, pady=5, sticky=W)
autodetect.grid(row=0, column=2, padx=7, pady=5, sticky=W)

#OK, Apply, and Reset Buttons
ok_btn = Button(text="OK!",width=20, command=save_new_cls).grid(row=2, column=0, sticky=SW, padx=6, pady=22, ipady=5)
apply_btn = Button(text="Apply", width=20, command=save_new_open).grid(row=2, column=1, sticky=SW, padx=4, pady=22, ipady=5)
reset_btn = Button(text="Reset", width=11,command=to_orig).grid(row=2, column=2, columnspan=2, sticky=SW, padx=6, pady=22, ipady=5)


root.mainloop()
