from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import os
from tkinter import filedialog
import shutil

class AddPng(Toplevel):

    def __init__(self, parent = None):
        super().__init__(parent)
        if(parent != None):
            self.parent = parent
        
        self.geometry('400x400')

        x_pad = 10
        y_pad = 5

        png_path_frame = LabelFrame(self, text= 'Select PNG Image', )
        png_path_frame.grid(padx= x_pad)

        path_input = Entry(png_path_frame, width= 45)
        path_input.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)

        path_input_btn = Button(png_path_frame, text= 'Get Pnge', command= lambda : self.AskPath('image', '*.png', path_input))
        path_input_btn.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)



        png_frame = LabelFrame(self)
        png_frame.grid()

        self.png_label = Label(png_frame, )
        self.png_label.grid(row = 0, column= 0)


        btn_frame = Frame(self)
        btn_frame.grid(padx= x_pad , pady= y_pad)

        Position = Button(btn_frame, text= 'Position', command= self.master.master.preview_frame.Create_Rectangle)
        Position.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)

        Apply = Button(btn_frame, text= 'Apply', command= lambda: self.master.paste_png(self.File_Path))
        Apply.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)

        Done = Button(btn_frame, text= 'Done', command= self.Done)
        Done.grid(row= 0, column= 2, padx= x_pad, pady= y_pad)




    def AskPath(self, name , Extention, Entry_Box):
        File_Path = filedialog.askopenfilename( initialdir=os.getcwd(), title= ("Select " + name), defaultextension= Extention, filetypes= ((name, Extention), ("All Files", "*.*")))
        Entry_Box.insert(0, File_Path)
        self.File_Path = File_Path

        img = Image.open(File_Path)

        width , height = img.size
        print(width, height)

        max_size = max(width, height)


 
        width = int((width*300) / max_size)
        height = int((height * 300)/max_size)
        print(width, height)

        img = img.resize((width, height))
        print(img.size)

        self.photo = ImageTk.PhotoImage(img)

        self.png_label.config(image= self.photo)



        return File_Path
        
    def start(self):
        self.mainloop()
    
    def Done(self):

        shutil.copy('Background.jpg', 'PlainImage/')
        self.master.TempFolder = 'PlainImage/Background.jpg'


        self.destroy()







