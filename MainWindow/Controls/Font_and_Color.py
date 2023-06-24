from tkinter import *
from tkinter import ttk
from PIL import ImageFont, Image, ImageDraw
from tkinter import font
import os
from tkinter.colorchooser import askcolor
from PIL import ImageTk
import shutil

class Font_And_Color(Toplevel):

    def __init__(self, parent = None, generic_text = False):
        super().__init__(parent)
        self.generic_text = generic_text
        self.parent = parent
        self.geometry('400x450')
        self.minsize(width= 400, height= 450)
        self.protocol("WM_DELETE_WINDOW",self.close)
        self.font_list()
        self.font_and_color()

        if(generic_text == False):
            self.Text_Input()
        else:
            self.Starting_index()
        
        print(self.generic_text)


        self.font_preview()
        self.main_but()


        
    def Text_Input(self):

        x_pad = 5
        y_pad = 5
        Text_Input_Frame = LabelFrame(self, width= 380, height= 70)
        Text_Input_Frame.grid()

        single_line_text_label = Label(Text_Input_Frame, text= 'sentence')
        self.single_line_text_Entry = Entry(Text_Input_Frame, width= 50)
        Multi_line_text_Button = Button(Text_Input_Frame, width= 5, height= 3, text= 'Text')

        single_line_text_label.grid(row= 0, column= 0, padx= x_pad , pady= y_pad)
        self.single_line_text_Entry.grid(row= 1, column= 0, padx= x_pad, pady= y_pad)
        Multi_line_text_Button.grid(row= 0, column= 1, rowspan= 2, columnspan= 1, padx= x_pad)
    
    
    def Starting_index(self):
        index_Frame = LabelFrame(self, width= 380, height= 30)
        index_Frame.grid()

        x_pad = 8
        y_pad = 2

        text_label = Label(index_Frame, text= "Index of Entry in Spread Sheet")
        text_label.grid(row= 0, column= 0)

        row_label = Label(index_Frame , text= 'Row')
        row_label.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)

        self.row_Entry = Entry(index_Frame , width= 5)
        self.row_Entry.grid(row= 0, column= 2, padx= x_pad, pady= y_pad)

        column_label = Label(index_Frame , text= 'column')
        column_label.grid(row= 0, column= 3, padx= x_pad, pady= y_pad)

        self.column_Entry = Entry(index_Frame , width= 5)
        self.column_Entry.grid(row= 0, column= 4, padx= x_pad, pady= y_pad)





    def set_color(self):
        self.color = askcolor()[1]
        print(self.color)

    def start(self):
        self.mainloop()


    def close(self):
        self.destroy()
        self = None

    def font_list(self):
        self.font_folder = 'Font'
        fonts = os.listdir(self.font_folder)
        self.font_list = fonts
    
    def font_and_color(self):
        x_pad = 10
        y_pad = 3
        

        font_frame = Frame(self, width= 350)
        font_frame.grid(padx= x_pad, pady= y_pad)

        font_box_label = Label(font_frame, text= 'Select a Font')
        font_box_label.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)
        self.font_box = ttk.Combobox(font_frame, values= self.font_list , width= 35)
        self.font_box.set("select and option")
        self.font_box.grid(row= 1, column= 0, padx= x_pad, pady= y_pad)


        font_size_label = Label(font_frame, text= 'size')
        font_size_label.grid(row= 0, column= 1 , padx= x_pad, pady= y_pad)

        self.font_size = Entry(font_frame , width= 5)
        self.font_size.grid(row= 1, column= 1, padx= x_pad, pady= y_pad)



        color_btn = Button(font_frame,text= 'color', width= 8, height= 3, command= self.set_color)
        color_btn.grid(column= 2, row= 0, rowspan= 2, columnspan= 1, padx= x_pad, pady= y_pad, sticky= 'N')

    def font_preview(self):
        preview_Frame= Frame(self)
        preview_Frame.grid( )

        self.preview_label = Label(preview_Frame)
        self.preview_label.grid()
    
    def text_preview(self):
        family = self.font_box.get()
        size = int(self.font_size.get())
        self.master.set_font((family, size, self.color))

        if(self.generic_text == True):
            self.master.Set_Row_and_colunmn( int(self.row_Entry.get()), int(self.column_Entry.get()))
            self.master.Get_Name_List()
        

        print(self.font_size.get())
        print(self.font_box.get())
        print(self.color)

        __font = ImageFont.truetype(font= (self.font_folder + '/' + family), size= size )

        img = Image.open('bgimg.jpg')

        I1 = ImageDraw.ImageDraw(img)
        I1.text(xy= (50, 50), text='Hello World', fill= self.color, font= __font)

        self.photo = ImageTk.PhotoImage(img)
        self.preview_label.config(image= self.photo)
        



    
    def main_but(self):
        x_pad = 5
        y_pad = 2
        but_width = 11
        but_height = 3
        btn_frame = Frame(self, width= 390, height= 40, border= 1)
        btn_frame.grid()

        preview = Button(btn_frame, text= 'preview', width= but_width, height= but_height, command= self.text_preview)
        preview.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)

        select_position = Button(btn_frame, text= 'select_position', width= but_width, height= but_height, command= lambda: self.master.master.preview_frame.Create_Rectangle())
        select_position.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)

        apply = Button(btn_frame, text= 'apply', width= but_width, height= but_height, command= self.apply_font)
        apply.grid(row= 0, column= 2, padx= x_pad, pady= y_pad)
        
        Done = Button(btn_frame, text= 'Done', width= but_width, height= but_height , command= self.Done)
        Done.grid(row= 0, column= 3, padx= x_pad, pady= y_pad)

    

    def apply_font(self):
        if(self.generic_text == False):
            self.master.Generate_1_image( self.single_line_text_Entry.get())
        else:
            self.master.Generate_1_image()

    def Done(self):

        

        
        if(self.generic_text == True):
            
            self.master.Generate_All()
        else:
             shutil.copy('Background.jpg', 'PlainImage/')
        
        self.master.Temp_Folder = 'PlainImage/Background.jpg'

        self.close()
        



        

    
