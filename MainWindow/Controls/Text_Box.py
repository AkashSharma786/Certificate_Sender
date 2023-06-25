from tkinter import *

class text_box(Toplevel):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent

        self.geometry('500x500')


        self.Text_box_frame = LabelFrame(self, text="Enter Text Here" , width= 450, height= 450)
        self.Text_box_frame.pack()

        self.box = Text(self.Text_box_frame, wrap= 'word', width= 400, height= 400)
        

        self.box.place(x= 2, y=2, relwidth= 0.98, relheight= 0.98)



        self.but = Button(self, text= 'Done', command= self.Done)

        self.but.pack(padx= 5, pady= 5)

    
    def Done(self):
        self.master.text = self.box.get(1.0, END)
        self.destroy()


    
    def start(self):
        self.mainloop()
