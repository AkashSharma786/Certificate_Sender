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
        
        self.label_bg= '#2d2d32'
        self.btn_background = '#007acc'
        self.Entry_bg = '#2e3a3b'
        self.ffg = '#ffffff'

        
        self.geometry('400x400')
        self.config(bg= self.label_bg )

        x_pad = 10
        y_pad = 5

        png_path_frame = LabelFrame(self, text= 'Select PNG Image', bg= self.label_bg , fg= self.ffg, relief= 'flat')
        png_path_frame.grid( row = 0, column= 0, padx= x_pad)

        path_input = Entry(png_path_frame, width= 45, bg= self.Entry_bg, fg= self.ffg)
        path_input.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)

        path_input_btn = Button(png_path_frame, text= 'Get Logo', bg= self.btn_background, fg= self.ffg, command= lambda : self.AskPath('image', '*.png', path_input))
        path_input_btn.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)



        png_frame = LabelFrame(self,  width= 300, height= 300, bg= self.label_bg, fg= self.ffg, relief= 'flat')
        png_frame.grid(row= 1, column= 0)
        png_frame.pack_propagate(0)

        self.png_label = Label(png_frame, bg= self.label_bg, fg= self.ffg)
        self.png_label.pack(expand= 1)


        btn_frame = Frame(self, bg= self.label_bg)
        btn_frame.grid(padx= x_pad , pady= y_pad)

        but_width = 13

        Position = Button(btn_frame, text= 'Position', bg= self.btn_background, fg= self.ffg, width= but_width,  command= self.master.master.preview_frame.Create_Rectangle)
        Position.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)

        Apply = Button(btn_frame, text= 'Apply' , bg= self.btn_background, fg= self.ffg , width= but_width,  command= lambda: self.master.paste_png(self.File_Path))
        Apply.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)

        Done = Button(btn_frame, text= 'Done' , bg= '#129d00', fg= self.ffg , width= but_width,  command= self.Done)
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
        shutil.copy('Background.jpg', 'PreOutput/')
        self.master.Temp_Folder = 'PlainImage/Background.jpg'


        self.destroy()







