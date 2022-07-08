import os
from tkinter import *
from tkinter import filedialog  # to be able to open the file
import tkinter.messagebox  # to create pop up messages
from pygame import mixer  # music

# We only want one element from pygame since pygame is such a big pkg, we just want the mixer
# which is responsible for audio clips to play and stop the music,use volume, etc.

root = Tk()
# This Tk function is creating a window, storing this window inside a root variable.


menubar = Menu(root)
# Created the menubar. Tkinter already knows you are trying to create a menubar by the root.
root.config(menu=menubar)
# This does two functions, keeps the menubar at the top and
# also to get the menubar ready to receive these submenus(file,edit,view,navigate etc)
# We must give it a parameter 'menu=menubar' or it will not understand what we are talking about


subMenu = Menu(menubar, tearoff=0)



# Creating a submenu. Tkinter understands a submenu by the menubar parameter
# Adding 'tearoff' to the parameter removes the tear off dots that originally came when clicking 'file'


def browse_file():
    global filename  # It declares a global variable lets you access anywhere in the python code
    filename = filedialog.askopenfilename()
    # This 'filedialog.askopenfilename()' opens up the file dialog window


menubar.add_cascade(label="File", menu=subMenu)
# Cascade is another term for dropdown menu.
# Adding 'add_cascade'inside the menubar creates the 'file', 'edit',etc. inside the menubar
subMenu.add_command(label="Open", command=browse_file)  # created a function to browse files
subMenu.add_command(label="Exit", command=root.destroy)


# This creates the stuff inside the submenu(drop down list) 'add_command'.
# adding 'add_command' inside the subMenu and including 'label="New Project"'creates this content inside the submenu.
# Adding the 'command = root.destroy'. What this does is it goes to the root window and destroys everything after
# 'exit is pressed' which means the program will exit and close.
def about_us():
    tkinter.messagebox.showinfo('About Melody', 'this is a music player built using Python Tkinter by Maki')
    # The def creates the about_us function and then we added the 'messagebox' from tkinter
    # which will create and 'showinfo' Which will show a big 'I' in the pop up along with what
    # we had typed in the parameter. 'Our title' whill show as the title of the menu bar and the info in the parameter
    # will be listed in the info. If you type 'showerror' instead, you will get a big red X along with the info. And
    # showwarning will give you a big yellow exclamation in the pop up
    # pop up box and 'this is the information that we want' inside the pop up.


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)
# We added a function labeled 'About Us' in the subMenu, add_command


mixer.init()
# Must initialize mixer or it will not work

# root.geometry('300x300')
# Made the GUI window bigger to see the title

root.title("Melody")
# Created a title on GUI

root.iconbitmap(r'guitar_wFo_icon.ico.')
# Created a GUI Icon

text = Label(root, text='Music to my ears')
# Created a Label widget

text.pack(pady=10) # We used a pack layout manager. This gives space between the label-'Lets make some noise!'and the buttons
# Must pack the text or it will not show in the window (like packing stuff in a luggage)


# Creating a photo widget, play image

# labelphoto = Label(root, image=photo)
# Using the label to act as a container for the photoimage
# labelphoto.pack()

def play_music():  # Created a play function to play the music
    try: # When the play button is pressed, this "try" function is saying, "hey python check if this 'paused'variable is initialized or not"
        # and if this variable is NOT initialized,then it goes to the "except" 'NameError' variable and proceed with the functions and keep playing the music.
        # But, if the pause variable IS initialized,it goes to the "def pause_music" and executes the condition there and "else" condition and proceed with the functions when music is unpaused.
        paused
    except NameError: # If not initialized then executes the code under except condition but if pause is declared, it will not execute the NameError below.
        try:
            mixer.music.load('journey.wav')  # To load the file. **Add 'filename' w/o the single quotes in the parameter to be able to open the filedialog when compliling final project.
            mixer.music.play()  # To play the file
            statusbar['text'] = "Playing Music" + ' - ' + os.path.basename('journey.wav') # This variable will make the statusbar text this info. **add 'filename' w/o single quotes back in parameter when compliling final project.
        except:
            tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')
            print("Error")
    else: # If initialized then it goes to the else condition
        mixer.music.unpause()
        statusbar['text'] = "Music Resume"

# We added 'try' and catch so if there is some kind of error, 'except' will print 'error' on the python screen instead
# of showing all the red errors. And by using the 'messagebox.showerror', a popup will show what states in the parameter.
# As the title in the popup 'File not found' with the pop up message.

def stop_music():  # Created a stop function to stop the music
    mixer.music.stop()  # To stop the file
    statusbar['text'] = "Music Stopped"

def pause_music(): # When the music is paused, python will go here and initializes the pause variable as it is True it will
                   # pause the music
    global paused
    paused = True #Created a booleon variable
    mixer.music.pause()
    statusbar['text'] = "Music Paused"

def rewind_music():
    play_music()
    statusbar['text'] = "Music Rewinded"

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # We used a class called mixer in Pygame to be able to play music in our Python code.
    # set volume of mixer takes value only from 0 to 1 that is why we must divide by 100 ex: 54/100= 0.54
    # What the 'def set_vol(val)' is going to do is convert the string to an integer 'volume = int(val) / 100 and then
    # it will divide it by 100

muted = False # Created a variable with a boolean value of False

def mute_music():
    global muted # We declared the False value as global so we can use the False value under the mute_music function
    if muted: # When the unmute button is pressed, it will go here and it will apply all below
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(40)
        muted = FALSE
    else: # When the muteBtn is pressed, it will go here and apply all below
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto) # This changes the volumeBtn to muteBtn when pressed
        scale.set(0) # This will make the volume to 0 when mute is pressed
        muted = TRUE


# This executes a function when a button is clicked. "Hey!"...so
# whenever a button is clicked, it goes to this parameter (see below,'command') and
# afterwards, it finds the function and prints the statement

middleframe = Frame(root)
middleframe.pack(pady=30,padx=30) # Gives the x axis space on the left and right and y axis top and bottom of the GUI frame


playPhoto = PhotoImage(file='images/play2.png') # Converted an 'image' into a button
playBtn = Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0,column=0, padx=10)
# playBtn.pack(side=LEFT, padx=10) # Gives space between the buttons
# Must pack btn or it will not show on window


stopPhoto = PhotoImage(file='images/stop2.png')
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0,column=1, padx=10)
# stopBtn.pack(side=LEFT, padx=10)

pausePhoto = PhotoImage(file='images/pause.png')
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0,column=2, padx=10)
# pauseBtn.pack(side=LEFT, padx=10)


# Bottom Frame for volume, rewind, mute etc.
bottomframe = Frame(root)
bottomframe.pack(pady=10)

rewindPhoto = PhotoImage(file='images/rewind.png')
rewindBtn = Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0,column=0)

# Below toggles the buttons from mute to volume
mutePhoto = PhotoImage(file='images/mute.png')
volumePhoto = PhotoImage(file='images/volume.png')
volumeBtn = Button(bottomframe, image=volumePhoto, command=mute_music) # This executes a command mute_music
volumeBtn.grid(row=0, column=1)



scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(40) # implement the default value of scale when music player starts
mixer.music.set_volume(0.2)
scale.grid(row=0,column=2) # pady gives space the y axis below the buttons
# Created a volume control with a  scale widget the parameter scaled starting value from 0 and end at 100
# Created orientation to make the scale widget horizontal
# The 'command' function  sends data from the volume chosen by the widget to the 'def set_vol(val) function (see above)
# then what the 'def set_vol(val)' is going to do is convert the string to an integer 'volume = int(val) / 100 and then
# it will divide it by 100

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
# Created a statusbar on the bottom of the window. Gives the status of the function
# the 'relief = SUNKEN' gives the text a sunken view


root.mainloop()
# The function of the mainloop engages the window in a infinite loop, every frame is getting refreshed.
