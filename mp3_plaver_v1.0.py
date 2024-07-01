import os
from tkinter import *
from tkinter import filedialog
from pygame import *

mixer.init()

def play():
    mixer.music.load(list_of_songs.get(ACTIVE))
    mixer.music.play()

def stop():
    mixer.music.stop()
    list_of_songs.selection_clear(ACTIVE)

global paused
paused = False
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True

def back():
    next = list_of_songs.curselection()
    next = next[0] - 1
    song = list_of_songs.get(next)

    mixer.music.load(song)
    mixer.music.play()

    list_of_songs.selection_clear(0, END)
    list_of_songs.activate(next)
    list_of_songs.selection_set(next, last=None)
def forward():
    next = list_of_songs.curselection()
    next = next[0] + 1
    song = list_of_songs.get(next)

    mixer.music.load(song)
    mixer.music.play()

    list_of_songs.selection_clear(0,END)
    list_of_songs.activate(next)
    list_of_songs.selection_set(next,last=None)
def select_folder():
    filepath = filedialog.askdirectory()
    if filepath:
        os.chdir(filepath)
        songs = os.listdir(filepath)
    for song in songs:
        if song.endswith(".mp3"):
            list_of_songs.insert(END, song)

def select_song():
    pass

window = Tk()
window.title("MP3 Player")
window.config(background="grey")

mp3_menu = Menu(window)
window.config(menu=mp3_menu)

add_song_menu = Menu(mp3_menu,tearoff=False)
mp3_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Select Folder", command=select_folder)
add_song_menu.add_command(label="Select Song", command=select_song)


top_frame = Frame(window,background="grey")
top_frame.grid(row=0,column=0)

bottom_frame = Frame(window)
bottom_frame.grid(row=1,column=0)

list_of_songs = Listbox(top_frame,bg="black",fg="green",width=40, selectbackground="white", selectforeground="black")
list_of_songs.grid(row=1,columnspan=2,padx=20,pady=20)

back_button = Button(bottom_frame,text="Back",command=back)
back_button.grid(row=0,column=0)

play_button = Button(bottom_frame,text="Play",command=play)
play_button.grid(row=0,column=1)

pause_button = Button(bottom_frame,text="Pause",command=lambda:pause(paused))
pause_button.grid(row=0,column=2)

stop_button = Button(bottom_frame, text="Stop",command=stop)
stop_button.grid(row=0,column=3)

forward_button = Button(bottom_frame,text="Forward",command=forward)
forward_button.grid(row=0,column=4)

window.mainloop()
