Live image as Desktop Background
================================

This small program will download an image from a given URI and set it as the windows desktop background. It is written in [Python][1] and requires the [pywin32][2] module. More features will be added, allowing you to customize what source to get the images from. At the moment it gets random images from lorempixel.com (CC-BY-SA) to demonstrate the feature.
The source code is freely available and in the Public Domain ([Unlicence][3]). At the moment it allows you to change to change the settings using the GUI program, or the settings.txt folder in your `Appdata\Roaming\livewebimagedesktop` folder.
###Planned Features
**Very Near Future**

 1. Add a config file in APPDATA, which allows the user to set path and refresh time of image. This will allow programs to be frozen/compiled, as the source no longer must be changed. It gets the URL and refresh time from the settings.txt file.    ✓✓✓ completed!
 2. Add a simple GUI Application which writes to the config file. This will feature a few buttons for options such as refresh time and URI, making the software easier for non-technical users. ✓✓✓ complete! Automatically checks if URL is valid, correct numbers where entered, etc. The url is checked by seeing if `http://` is in the entered text, and if it contains at least one dot. ![enter image description here][4] 
 *This is what the GUI looks like at the moment.*
 
 3. Get the autostart functioning. On files frozen with cx_Freeze, when i have a shortcut in my Autostart folder, I get an error at system startup.

 
###Other Features

 1. I want to implement a feature that checks the refresh rate and time of the images, and automatically adjusts it. At the moment, if I set the program to refresh the image every five minutes, and the image from the web updates every five minutes, depending on the offset it could take up to ten minutes for a change to be seen. If it updates more frequently, that would take up unnecessary memory and bandwidth.
 2. Optimize this program more. It takes up ~8000K of memeory at the moment, which isn't much, but could be less.

I am open to any suggestions for other features.

Technical Details
-----------------
 The program works using a very simple method.
 

 1. At startup the program opens the file `bg.jpg` in the TEMP folder
    - If this file does not exist, it will be created.
 2. `urlopen` will retrieve the image from the specified URI.
 3. This image will be written to the file we opened/created `bg.jpg`.
 4. This image is set as the desktop background
 5. After after a specified amount of time (1 min. in my program), steps 1-4 will be repeated, re-fetching the image, overwriting it and setting as the desktop background.

Contributing
--------------
You can send me suggestions for this project easily via email (<zederich0@gmail.com>).


  [1]: http://www.python.org/downloads/
  [2]: http://sourceforge.net/projects/pywin32/files/pywin32/
  [3]: http://unlicense.org/
  [4]: http://abload.de/img/gui-screenshotojr6l.gif