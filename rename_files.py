#rename a lot of files at once for TV shows 

import os
import sys
from tkinter import BOTTOM, Button, Entry, Frame, Label, StringVar, Tk, ttk

def rename_files(directory,name,file_extension,total_episodes,scheme,starting_ep,season_number):
    episode = starting_ep
    season = 1
    for filename in os.listdir(directory):
        if season_number < 10:
            season = "0" + str(season_number)
        else:
            season = str(season_number)
        EP = str(episode)
        source = directory + filename
        if total_episodes >= 10 and not (total_episodes > 100):
            if episode <= 9:
                EP = "0" + EP
        elif total_episodes >= 100 and not (total_episodes > 1000):
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
        match scheme:
            case "<Name> E#":
                destination = directory + name + " E" + EP + file_extension
            case "<Name> S#E#":
                destination = directory + name + " S" + str(season) + "E" + EP + file_extension
        os.rename(source, destination)
        episode += 1

def gui():
    e_list = []
    base = Tk()
    base.geometry("200x400")
    frame = Frame(base)
    frame.pack()
    dir_label_text = "Path to Folder:"
    dir_entry_text = ""
    name_label_text = "Name of Show"
    name_entry_text = ""
    ext_label_text = "File Extension"
    ext_entry_text = ".mkv"
    total_label_text = "Total Number of Episodes"
    total_entry_text = ""
    season_label_text = "Season Number:"
    season_entry_text = "1"
    starting_label_text = "Starting Episode Number:"
    starting_entry_text = "1"
    label_entry_pack(dir_label_text,dir_entry_text,frame,e_list)
    label_entry_pack(name_label_text,name_entry_text,frame,e_list)
    label_entry_pack(ext_label_text,ext_entry_text,frame,e_list)
    label_entry_pack(total_label_text,total_entry_text,frame,e_list)
    scheme_list = ["<Name> E#","<Name> S#E#"]
    scheme_choice = ttk.Combobox(frame, values = scheme_list, width=26, justify= "center")
    scheme_choice.set("Select Naming Scheme")
    scheme_choice.pack(pady = 10)
    bottom_frame = Frame(base)
    bottom_frame.pack(side=BOTTOM)
    label_entry_pack(starting_label_text,starting_entry_text,frame,e_list)
    label_entry_pack(season_label_text,season_entry_text,frame,e_list)
    run_button = Button(bottom_frame, text = "Rename Files!", command=lambda:run_all(e_list[0],e_list[1],e_list[2],e_list[3], 
    scheme_choice,e_list[4],e_list[5]), font = ("Impact 15"))
    run_button.pack(pady=5)
    base.title("Batch Rename")
    base.mainloop()

def label_entry_pack(label_desc, entry_text, frame, entry_list:list):
    text = StringVar()
    text.set(label_desc)
    label = Label(frame, textvariable=text)
    label.pack()
    entry = Entry(frame, width = 30,bd=2,)
    entry.insert(0,entry_text)
    entry.pack(padx=5,pady=5)
    entry_list.append(entry)

def run_all(dir:Entry,name:Entry,ext:Entry,total:Entry,scheme:ttk.Combobox,starting:Entry,season:Entry):
    directory = dir.get() + "\\"
    os.chdir(directory)
    rename_files(directory,name.get(),ext.get(),int(total.get()),scheme.get(),int(starting.get()),int(season.get()))

def refresh(self):
    self.destroy()
    self.__init__()

if __name__ == "__main__":
    gui()