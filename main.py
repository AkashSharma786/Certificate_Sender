from tkinter import *
from tkinter.font import Font
from tkinter import font
from MainWindow.ControlPane import Control_Pane
from MainWindow.Preview_frame import Preview_Frame
#fonts = list(font.families())







class ParentWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gui App")
        self.geometry('1000x650')
        control_frame = Control_Pane(self)
        preview_frame = Preview_Frame(self)

        control_frame.grid(row= 0, column= 0, padx= 2, pady= 2)
        preview_frame.grid(row= 0, column= 1, padx= 2, pady= 2)

        self.control_frame = control_frame
        self.preview_frame = preview_frame
    
    def check_clicked(self):
        print('Button Clicked')






app = ParentWindow()
app.mainloop()



