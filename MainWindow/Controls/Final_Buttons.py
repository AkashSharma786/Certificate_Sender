from tkinter import *
from MainWindow.EmailEditor import EmailEditor
import os
from PIL import Image
import img2pdf

class Final_Buttons( Frame ):

    global email_window
    email_window = None

    def __init__(self, parent ):
        Frame.__init__(self, parent)
        
        super().__init__(parent)
        self.parent = parent

        
        self.config(bg= '#2d2d32')
        btn_background = '#007acc'

        btn_fg = '#ffffff'
        


    
        f_btn = LabelFrame(self, width= 340, height= 200, pady=5, bg= '#2d2d32', relief= 'flat')
        f_btn.grid(row= 0, column= 0,pady=5, padx= 5)

        Store = Button(f_btn, text= 'Convert_pdf' , width= 21,  bg= btn_background , fg=  btn_fg,  command= lambda: self.Convert_PDF())
        Send = Button(f_btn, text= 'Send Email' , width= 21, bg= '#129d00' , fg=  btn_fg,  command= self.EmailWindow)


        Store.grid(row=0, column= 0 , padx= 4, pady= 4)
        Send.grid(row=0, column= 1 , padx= 4, pady= 4)

    def EmailWindow(self):
        global email_window

        if email_window is None or not email_window.winfo_exists():
            email_window = EmailEditor(self.parent)
        else:
            print('Window Not created')
    
    def Convert_PDF(self):
        output = self.master.output
        

        Image_list = os.listdir(output)

        for image in Image_list:
            if(image[-1] == 'g'):

                print(image)
                img_path = output + '/' +image
                pdf_path = output+ '/' + image[:-4]+ '.pdf'
                print(pdf_path)

                

                img = Image.open(img_path)
                pdf_bytes = img2pdf.convert(img.filename)

                file = open(pdf_path, 'wb')
                file.write(pdf_bytes)
                img.close()
                file.close()








        

        















   

    def start(self):
        self.mainloop()