from tkinter import *
from tkinter import ttk
from PIL import ImageFont, Image, ImageDraw
from tkinter import font
import os
from tkinter.colorchooser import askcolor
from PIL import ImageTk
import shutil
from MainWindow.Controls.Text_Box import text_box

class Font_And_Color(Toplevel):


    def __init__(self, parent = None, generic_text = False):
        super().__init__(parent)

        self.label_bg= '#2d2d32'
        self.btn_background = '#007acc'
        self.Entry_bg = '#2e3a3b'
        self.ffg = '#ffffff'
        self.generic_text = generic_text
        self.parent = parent


        self.geometry('400x450')
        self.config(bg= self.label_bg)
        self.minsize(width= 400, height= 450)
        self.protocol("WM_DELETE_WINDOW",self.close)
        self.font_list()
        self.font_and_color()
        self.textbox = None
        self.text = ''
        self.color = '#000000'



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
        Text_Input_Frame = LabelFrame(self, width= 380, height= 70, bg= self.label_bg, fg= self.ffg, relief= 'flat')
        Text_Input_Frame.grid(row= 1, column= 0)

        single_line_text_label = Label(Text_Input_Frame, text= 'sentence',bg= self.label_bg , fg= self.ffg)
        self.single_line_text_Entry = Entry(Text_Input_Frame, width= 50, bg= self.Entry_bg, fg= self.ffg , insertbackground= 'white')
        Multi_line_text_Button = Button(Text_Input_Frame, width= 5, height= 3, text= 'Text',bg= self.btn_background, fg= self.ffg ,command= self.getText)

        single_line_text_label.grid(row= 0, column= 0, padx= x_pad , pady= y_pad)
        self.single_line_text_Entry.grid(row= 1, column= 0, padx= x_pad, pady= y_pad)
        Multi_line_text_Button.grid(row= 0, column= 1, rowspan= 2, columnspan= 1, padx= x_pad)
    

    def getText(self):
        
        
        if(self.textbox is None or not self.textbox.winfo_exists()):
            
            self.textbox = text_box(self)
            if(self.text != ''):
                self.textbox.box.insert(1.0, self.text)
    
    
    def Starting_index(self):
        index_Frame = LabelFrame(self, width= 380, height= 30, bg= self.label_bg, fg= self.ffg, relief= 'flat')
        index_Frame.grid(row= 1, column= 0)

        x_pad = 8
        y_pad = 2
        self.is_primary = IntVar()
        self.is_primary.set(0)

        
        self.make_primary = Checkbutton(index_Frame, text= 'Set primary list', variable= self.is_primary, onvalue= 1, offvalue= 0, bg= self.label_bg , fg= self.ffg, selectcolor= self.label_bg, activebackground= self.label_bg, activeforeground= self.btn_background)
        self.make_primary.grid(row= 0, column= 0, rowspan= 1 , columnspan= 5, sticky= 'W')

        text_label = Label(index_Frame, text= "Index of Entry in Spread Sheet", bg= self.label_bg, fg= self.ffg)
        text_label.grid(row=1, column=0)

        row_label = Label(index_Frame , text= 'Row' , bg= self.label_bg, fg= self.ffg)
        row_label.grid(row=1, column= 1, padx= x_pad, pady= y_pad)

        self.row_Entry = Entry(index_Frame , width= 5 , bg= self.Entry_bg, fg= self.ffg, insertbackground= 'white' )
        self.row_Entry.grid(row=1, column= 2, padx= x_pad, pady= y_pad)

        column_label = Label(index_Frame , text= 'column' , bg= self.label_bg, fg= self.ffg)
        column_label.grid(row=1, column= 3, padx= x_pad, pady= y_pad)

        self.column_Entry = Entry(index_Frame , width= 5 , bg= self.Entry_bg, fg= self.ffg , insertbackground= 'white')
        self.column_Entry.grid(row=1, column= 4, padx= x_pad, pady= y_pad)





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
        

        font_frame = Frame(self, width= 350, bg= self.label_bg)
        font_frame.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)

        font_box_label = Label(font_frame, text= 'Select a Font', bg= self.label_bg, fg= self.ffg)
        font_box_label.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)
        self.font_box = ttk.Combobox(font_frame, values= self.font_list , width= 35)
        self.font_box.set("arial.ttf")
        self.font_box.grid(row= 1, column= 0, padx= x_pad, pady= y_pad)


        font_size_label = Label(font_frame, text= 'size', bg= self.label_bg, fg= self.ffg)
        font_size_label.grid(row= 0, column= 1 , padx= x_pad, pady= y_pad)

        self.font_size = Entry(font_frame , width= 5 , bg= self.Entry_bg, fg= self.ffg, insertbackground= 'white' )
        self.font_size.insert(0,'15')
        self.font_size.grid(row= 1, column= 1, padx= x_pad, pady= y_pad)



        color_btn = Button(font_frame,text= 'color', width= 8, height= 3,  bg= self.btn_background, fg= self.ffg ,command= self.set_color)
        color_btn.grid(column= 2, row= 0, rowspan= 2, columnspan= 1, padx= x_pad, pady= y_pad, sticky= 'N')

    def font_preview(self):

        preview_Frame= LabelFrame(self, relief= 'flat', width= 380, height= 250, bg= self.label_bg, fg= self.ffg)
        preview_Frame.pack_propagate(0)
        preview_Frame.grid(row= 2, column= 0)

        self.preview_label = Label(preview_Frame , image= None, anchor= 'ne', bg= self.label_bg, fg= self.ffg)
        self.preview_label.pack(expand= 1)
    
    def text_preview(self):
        family = self.font_box.get()
        size = int(self.font_size.get())
        self.master.set_font((family, size, self.color))

        if(self.generic_text == True):
            
            self.text_list = self.master.Get_Text_List( int(self.row_Entry.get()) , int(self.column_Entry.get()) )



        

        print(self.font_size.get())
        print(self.font_box.get())
        print(self.color)

        __font = ImageFont.truetype(font= (self.font_folder + '/' + family), size= size )

        img = Image.open('bgimg.jpg')

        I1 = ImageDraw.ImageDraw(img)
        I1.text(xy= (50, 50), text='Sample Text', fill= self.color, font= __font)

        self.photo = ImageTk.PhotoImage(img)
        self.preview_label.config(image= self.photo)
        



    
    def main_but(self):
        x_pad = 5
        y_pad = 2
        but_width = 11
        but_height = 3
        btn_frame = Frame(self, width= 390, height= 40, border= 1, bg= self.label_bg)
        btn_frame.grid(row= 3, column= 0)

        preview = Button(btn_frame, text= 'preview', width= but_width, height= but_height, bg= self.btn_background, fg= self.ffg, command= self.text_preview)
        preview.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)

        select_position = Button(btn_frame, text= 'select_position', width= but_width, height= but_height , bg= self.btn_background, fg= self.ffg , command= lambda: self.master.master.preview_frame.Create_Rectangle())
        select_position.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)

        apply = Button(btn_frame, text= 'apply', width= but_width, height= but_height , bg= self.btn_background, fg= self.ffg ,   command= self.apply_font)
        apply.grid(row= 0, column= 2, padx= x_pad, pady= y_pad)
        
        Done = Button(btn_frame, text= 'Done', width= but_width, height= but_height , bg= '#129d00', fg= self.ffg  , command= self.Done)
        Done.grid(row= 0, column= 3, padx= x_pad, pady= y_pad)

    

    def apply_font(self):

        

        if(self.generic_text == False):
            if(self.text == ''):
                self.master.Generate_1_image( self.single_line_text_Entry.get())
            else:
                self.master.Generate_1_image(self.text)
        else:
            self.master.Generate_1_image(self.text_list[0])

    def Done(self):

        shutil.copy('Background.jpg', 'PlainImage/')
        if(self.generic_text == True):
            self.master.make_position_list()
            self.master.make_Entry_list(self.text_list)
            self.master.make_font_style_list(self.font_box.get())
            self.master.make_font_size_list(self.font_size.get())
            self.master.make_font_color_list(self.color)
            print(self.is_primary.get())

            if(self.is_primary.get() == 1):
                self.master.set_primary_list(self.text_list)
        
        else:
            shutil.copy('Background.jpg', 'PreOutput/' )
            

            
            
        
        
        self.master.Temp_Folder = 'PlainImage/Background.jpg'

        self.close()
        



        

    
