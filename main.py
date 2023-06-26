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
        self.geometry('1000x630')
        self.maxsize(width= 1000, height= 630)
        self.minsize(width= 1000, height= 630)
        self.config(bg= '#2d2d30')
        control_frame = Control_Pane(self)
        preview_frame = Preview_Frame(self)
        preview_frame.config(bg= '#ffffff')
        x_pad = 10
        y_pad = 10

        
        
        

        control_frame.grid(row= 0, column= 0, padx= x_pad, pady= y_pad, sticky= N)
        preview_frame.grid(row= 0, column= 1, padx= x_pad, pady= y_pad)

        self.control_frame = control_frame
        self.preview_frame = preview_frame

        
    







app = ParentWindow()
app.mainloop()



