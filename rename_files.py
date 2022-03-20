#rename a lot of files at once, specifically in this case anime episodes

import os
from tkinter import BOTTOM, Button, Entry, Frame, Label, StringVar, Tk, ttk

DIRECTORY = ""
NAME = ""
FILE_EXTENSION = ".mkv"
TOTAL_EPISODES = 0
NAMING_SCHEME = ""

def rename_files(directory,name,file_extension,total_episodes):
    episode = 1
    for filename in os.listdir(directory):
        EP = str(episode)
        source = directory + filename
        if total_episodes > 10 and not (total_episodes > 100):
            if episode <= 9:
                EP = "0" + EP
        elif total_episodes > 100 and not (total_episodes > 1000):
            if episode <= 9:
                EP = "00" + EP
            elif episode <= 99:
                EP = "0" + EP
        elif total_episodes > 1000:
            if episode <= 9:
                EP = "000" + EP
            elif episode <= 99:
                EP = "00" + EP
            elif episode <= 999:
                EP = "0" + EP
        destination = directory + name + " Episode " + EP + file_extension
        os.rename(source, destination)
        episode += 1

def gui():
    base = Tk()
    base.geometry("300x400")
    frame = Frame(base)
    frame.pack()
    dir_text = StringVar()
    dir_text.set("Enter the path to the folder containing the files:")
    dir_label = Label(frame, textvariable = dir_text)
    dir_label.pack()
    dir_entry = Entry(frame, width = 45,bd=2,)
    dir_entry.insert(0,"path to folder")
    dir_entry.pack(padx=5,pady=5)
    name_text = StringVar()
    name_text.set("Enter the name of the show:")
    name_label = Label(frame, textvariable = name_text)
    name_label.pack()
    name_entry = Entry(frame, width = 45,bd=2,)
    name_entry.insert(0,"name of show")
    name_entry.pack(padx=5,pady=5)
    ext_text = StringVar()
    ext_text.set("Enter the extension that the files use:")
    ext_label = Label(frame, textvariable = ext_text)
    ext_label.pack()
    ext_entry = Entry(frame, width = 45,bd=2,)
    ext_entry.insert(0,".mkv")
    ext_entry.pack(padx=5,pady=5)
    total_text = StringVar()
    total_text.set("Enter the total number of episodes:")
    total_label = Label(frame, textvariable = total_text)
    total_label.pack()
    total_entry = Entry(frame, width = 45,bd=2,)
    total_entry.insert(0,"total number of episodes")
    total_entry.pack(padx=5,pady=5)
    scheme_list = ["<Name> Episode #" , "<Name> Season # Episode #", "<Name> E#","<Name> S#E#"]
    scheme_chooser = ttk.Combobox(frame, values = scheme_list, width=42)
    scheme_chooser.set("Select the naming scheme you want to use")
    scheme_chooser.pack(pady = 10)
    bottom_frame = Frame(base)
    bottom_frame.pack(side=BOTTOM)
    run_button = Button(bottom_frame, text = "Rename Files!", command=lambda:run_all(dir_entry,name_entry,ext_entry,total_entry), 
    font = ("Impact 15"))
    run_button.pack(pady=5)
    base.title("Batch Rename")
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

def set_naming(combo:ttk.Combobox):
    global NAMING_SCHEME
    NAMING_SCHEME = combo.get()

def run_all(dir:Entry,name:Entry,ext:Entry,total:Entry,scheme:ttk.Combobox):
    set_dir(dir)
    set_name(name)
    set_ext(ext)
    set_total(total)
    set_naming(scheme)
    rename_files(DIRECTORY,NAME,FILE_EXTENSION,TOTAL_EPISODES)

if __name__ == "__main__":
    gui()