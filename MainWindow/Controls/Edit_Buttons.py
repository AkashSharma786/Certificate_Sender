from tkinter import *
from MainWindow.Controls.Font_and_Color import Font_And_Color

class EditButtons(Frame):
    global edit_window
    edit_window = None

    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent

        x_pad = 20
        y_pad = 5

        self.add_text = Button(self, text= 'Add Text', command= self.text_edit_window)
        self.add_name = Button(self, text = 'add Name', command= self.name_edit_window)
        self.add_png = Button(self, text= 'Add Png')
        
        self.add_text.grid(row= 0, column= 0, padx= x_pad, pady= y_pad)
        self.add_png.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)
        self.add_name.grid(row= 0, column= 2, padx= x_pad, pady= y_pad)
    
    def text_edit_window(self):
        global edit_window

        if edit_window is None or not edit_window.winfo_exists() :
            edit_window = Font_And_Color( self.parent, generic_text= False) 
        

    def name_edit_window(self):
        global edit_window

        if edit_window is None or not edit_window.winfo_exists():
            edit_window = Font_And_Color( self.parent, generic_text= True)
        

    
    def start(self):
        self.mainloop()


