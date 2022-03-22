#rename a lot of files at once, specifically in this case anime episodes

import os
from tkinter import BOTTOM, Button, Entry, Frame, Label, StringVar, Tk, ttk

def rename_files(directory,name,file_extension,total_episodes,ep_per_season,scheme):
    episode = 1
    season = 1
    for filename in os.listdir(directory):
        if episode > ep_per_season:
            season += 1
            episode = 1
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
        match scheme:
            case "<Name> Episode #":
                destination = directory + name + " Episode " + EP + file_extension
            case "<Name> Season # Episode #":
                destination = directory + name + " Season " + str(season) + " Episode " + EP + file_extension
            case "<Name> E#":
                destination = directory + name + " E" + EP + file_extension
            case "<Name> S#E#":
                destination = directory + name + " S" + str(season) + "E" + EP + file_extension
        os.rename(source, destination)
        episode += 1

def gui():
    e_list = []
    base = Tk()
    base.geometry("300x370")
    frame = Frame(base)
    frame.pack()
    dir_label_text = "Enter the path to the folder containing the files:"
    dir_entry_text = "path to folder"
    name_label_text = "Enter the name of the show:"
    name_entry_text = "name of show"
    ext_label_text = "Enter the extension that the files use:"
    ext_entry_text = ".mkv"
    total_label_text = "Enter the total number of episodes:"
    total_entry_text = "total number of episodes"
    season_label_text = "Enter how many episodes there are per season:\n(leave this option at 9999 if it is not needed)"
    season_entry_text = "9999"
    label_entry_pack(dir_label_text,dir_entry_text,frame,e_list)
    label_entry_pack(name_label_text,name_entry_text,frame,e_list)
    label_entry_pack(ext_label_text,ext_entry_text,frame,e_list)
    label_entry_pack(total_label_text,total_entry_text,frame,e_list)
    scheme_list = ["<Name> Episode #" , "<Name> Season # Episode #", "<Name> E#","<Name> S#E#"]
    scheme_choice = ttk.Combobox(frame, values = scheme_list, width=42)
    scheme_choice.set("Select the naming scheme you want to use")
    scheme_choice.pack(pady = 10)
    label_entry_pack(season_label_text,season_entry_text,frame,e_list)
    bottom_frame = Frame(base)
    bottom_frame.pack(side=BOTTOM)
    run_button = Button(bottom_frame, text = "Rename Files!", command=lambda:run_all(e_list[0],e_list[1],e_list[2],e_list[3],e_list[4], 
    scheme_choice), font = ("Impact 15"))
    run_button.pack(pady=5)
    base.title("Batch Rename")
    base.mainloop()

def label_entry_pack(label_desc, entry_text, frame, entry_list:list):
    text = StringVar()
    text.set(label_desc)
    label = Label(frame, textvariable=text)
    label.pack()
    entry = Entry(frame, width = 45,bd=2,)
    entry.insert(0,entry_text)
    entry.pack(padx=5,pady=5)
    entry_list.append(entry)

def run_all(dir:Entry,name:Entry,ext:Entry,total:Entry,season:Entry,scheme:ttk.Combobox):
    directory = dir.get() + "\\"
    os.chdir(directory)
    rename_files(directory,name.get(),ext.get(),int(total.get()),int(season.get()),scheme.get())

if __name__ == "__main__":
    gui()