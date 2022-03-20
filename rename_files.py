#rename a lot of files at once, specifically in this case anime episodes

from asyncio.windows_events import NULL
import os
from tkinter import *

DIRECTORY = r"\\"
ANIME_NAME = ""
FILE_EXTENSION = ".mkv"
TOTAL_EPISODES = 0

def rename_files(folder,anime,extension,total_episodes):
    episode = 1
    os.chdir(folder)
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
    base.geometry("500x500")
    frame = Frame(base)
    frame.pack()

    
    button = Button(frame, text = "Rename Files!", command = rename_files(NULL,NULL,NULL,NULL))
    base.title("Batch Rename Episode Files")
    base.mainloop()



if __name__ == "__main__":
    gui()