from tkinter import filedialog
import os

def AskPath():
    File_Path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select excel file")
    return File_Path
def AskFolder():
    Folder_Path = filedialog.askdirectory(initialdir=os.getcwd(), title="Select excel file")
    return Folder_Path

