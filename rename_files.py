#rename a lot of files at once, specifically in this case anime episodes

from msilib.schema import Directory
import os
from tkinter import BOTTOM, Button, Entry, Frame, Tk, font
from tokenize import String

DIRECTORY = ""
ANIME_NAME = ""
FILE_EXTENSION = ".mkv"
TOTAL_EPISODES = 0

def rename_files(folder,anime,extension,total_episodes):
    episode = 1
    for filename in os.listdir(folder):
        EP = str(episode)
        source = folder + filename
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
        destination = folder + anime + " Episode " + EP + extension
        os.rename(source, destination)
        episode += 1

def gui():
    base = Tk()
    base.geometry("300x300")
    frame = Frame(base)
    frame.pack()
    folder_entry = Entry(frame, width = 20)
    folder_entry.insert(0,"file directory")
    folder_entry.pack(padx=5,pady=5)
    dir_button = Button(frame, text = "set directory", command=lambda:set_dir(folder_entry))
    dir_button.pack(padx=5,pady=5)
    bottom_frame = Frame(base)
    bottom_frame.pack(side=BOTTOM)
    run_button = Button(bottom_frame, text = "Rename Files!", command=lambda:rename_files(DIRECTORY,ANIME_NAME,FILE_EXTENSION,TOTAL_EPISODES), 
    font = ("Impact 15"))
    run_button.pack()
    base.title("Batch Rename Episode Files")
    base.mainloop()

def set_dir(entry:Entry):
    DIRECTORY = "C:\\Users\\capta\\Downloads"
    os.chdir(DIRECTORY)
    


if __name__ == "__main__":
    gui()