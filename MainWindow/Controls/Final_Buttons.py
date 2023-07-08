from tkinter import *
from MainWindow.EmailEditor import EmailEditor
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import os
from PIL import Image
import img2pdf
import shutil

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

        Generate = Button(f_btn, text= 'Generate' , width= 13,  bg= btn_background , fg=  btn_fg,  command= lambda: self.Generate())
        save = Button(f_btn, text= 'Save Template ', width= 13, bg= btn_background, fg= btn_fg, command= self.save_template)
        Send = Button(f_btn, text= 'Send Email' , width= 13, bg= '#129d00' , fg=  btn_fg,  command= self.EmailWindow)


        Generate.grid(row=0, column= 0 , padx= 4, pady= 4)
        save.grid(row= 0, column=1, padx=4, pady=4)
        Send.grid(row=0, column= 2 , padx= 4, pady= 4)

    def EmailWindow(self):
        global email_window

        if email_window is None or not email_window.winfo_exists():
            email_window = EmailEditor(self.parent)
        else:
            print('Window Not created')


    def save_template(self):
        print("save Template Clicked")
        files = os.listdir('./PreOutput')
        if(files == []):
            messagebox.showerror("Error", "Nothing To Save")
        else:

            Template_folder = os.path.dirname(self.master.certificate)
            
            print(Template_folder)
            save_as_path = asksaveasfile(mode= 'w', initialfile= 'Untitled', initialdir= Template_folder, defaultextension= '*.jpg', filetypes= [("Image File", "*.jpg")])
            
            shutil.copy('PreOutput/Background.jpg', save_as_path.name)


    def Generate(self):
        self.master.Generate_All()
        self.Convert_PDF()
    
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