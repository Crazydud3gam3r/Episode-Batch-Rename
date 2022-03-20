#rename a lot of files at once, specifically in this case anime episodes

from msilib.schema import Directory
import os
from tkinter import BOTTOM, Button, Entry, Frame, Tk, font
from tokenize import String

DIRECTORY = ""
NAME = ""
FILE_EXTENSION = ".mkv"
TOTAL_EPISODES = 0

def rename_files(directory,name,file_extension,total_episodes):
    episode = 1
    for filename in os.listdir(directory):
        EP = str(episode)
        source = directory + filename
        if total_episodes > 10 and not (total_episodes > 100):
            if episode <= 9:
                EP = "0" + episode
        elif total_episodes > 100 and not (total_episodes > 1000):
            if episode <= 9:
                EP = "00" + episode
            elif episode <= 99:
                EP = "0" + episode
        elif total_episodes > 1000:
            if episode <= 9:
                EP = "000" + episode
            elif episode <= 99:
                EP = "00" + episode
            elif episode <= 999:
                EP = "0" + episode
        destination = directory + name + " Episode " + EP + file_extension
        os.rename(source, destination)
        episode += 1

def gui():
    base = Tk()
    base.geometry("300x300")
    frame = Frame(base)
    frame.pack()
    dir_entry = Entry(frame, width = 45,bd=2,)
    dir_entry.insert(0,"path to folder")
    dir_entry.pack(padx=5,pady=5)
    name_entry = Entry(frame, width = 45,bd=2,)
    name_entry.insert(0,"name of show")
    name_entry.pack(padx=5,pady=5)
    bottom_frame = Frame(base)
    bottom_frame.pack(side=BOTTOM)
    run_button = Button(bottom_frame, text = "Rename Files!", command=lambda:run_all(dir_entry,), 
    font = ("Impact 15"))
    run_button.pack(pady=5)
    base.title("Batch Rename Episode Files")
    base.mainloop()

def set_dir(entry:Entry):
    global DIRECTORY
    DIRECTORY = entry.get() + "\\"
    os.chdir(DIRECTORY)
    
def set_name(entry:Entry):
    global NAME
    NAME = entry.get()

def set_ext(entry:Entry):
    global FILE_EXTENSION
    FILE_EXTENSION = entry.get()

def set_total(entry:Entry):
    global TOTAL_EPISODES
    TOTAL_EPISODES = int(entry.get())

def run_all(dir:Entry,name:Entry,ext:Entry,total:Entry):
    set_dir(dir)
    set_name(name)
    set_ext(ext)
    set_total(total)
    rename_files(DIRECTORY,NAME,FILE_EXTENSION,TOTAL_EPISODES)


if __name__ == "__main__":
    gui()