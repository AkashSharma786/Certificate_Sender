from tkinter import *
from MainWindow.EmailEditor import EmailEditor

class Final_Buttons( Frame ):

    global email_window
    email_window = None

    def __init__(self, parent ):
        Frame.__init__(self, parent)
        
        super().__init__(parent)
        self.parent = parent
        


    
        f_btn = LabelFrame(self, width= 340, height= 200, pady= 5)
        f_btn.grid(row= 0, column= 0, padx= 5, pady= 5)

        select_position = Button(f_btn, text= 'SelectPosition' , padx= 4, pady= 4, width= 21, command= lambda: self.master.master.preview_frame.Create_Rectangle()) 
        Img_preview = Button(f_btn, text= 'Preview' , padx= 4, pady= 4 , width= 21, command= lambda: self.master.Generate_1_image())
        Store = Button(f_btn, text= 'Store' , padx= 4, pady= 4 , width= 21, command= lambda: self.master.Generate_All())
        Send = Button(f_btn, text= 'Send Email' , padx= 4, pady= 4 , width= 21, command= self.EmailWindow)

        select_position.grid(row= 0, column= 0 , padx= 4, pady= 4)
        Img_preview.grid(row=0, column= 1 , padx= 4, pady= 4)
        Store.grid(row=1, column= 0 , padx= 4, pady= 4)
        Send.grid(row=1, column= 1 , padx= 4, pady= 4)

    def EmailWindow(self):
        global email_window

        if(email_window == None):
            email_window = EmailEditor(self.parent)
        else:
            print('Window Not created')






   

    def start(self):
        self.mainloop()