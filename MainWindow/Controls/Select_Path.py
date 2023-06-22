from tkinter import *
from tkinter import filedialog
import os

class Path_Selection(Frame):

    def __init__(self, parent ):
        Frame.__init__(self, parent)
        super().__init__(parent)

        certificate_label = Label(self, text= "Select Certificate" )
        certificate_Input = Entry(self, width= 55)
        certificate_button = Button(self, text= "Get Template", width= 15, command= lambda : self.AskPath( "image", "*.jpg", certificate_Input))

        

        certificate_Input.grid(row= 1, columnspan= 2 , padx= 5, pady= 5)
        certificate_label.grid(row= 0, column= 0, padx= 2,pady= 2, sticky= 'W' )
        certificate_button.grid(row= 0, column= 1, padx= 3, pady= 2, sticky= 'E')



        Excel_label = Label(self, text= "Select Excel Sheet", )
        Excel_Input = Entry(self, width= 55 )
        Excel_button = Button(self, text= "Get Sheet" , width= 15 , command= lambda : self.AskPath( "Excel Spreadsheet", "*.xlsx", Excel_Input))

        Excel_label.grid(row= 4, column= 0, padx= 2, pady= 2, sticky= 'W' )
        Excel_button.grid(row= 4, column= 1, padx= 3, pady= 2 , sticky= 'E')
        Excel_Input.grid(row= 5, columnspan= 2, padx= 5, pady= 5)

        output_label = Label(self, text= "Select Output Folder" )
        output_Input = Entry(self, width= 55 )
        output_button = Button(self, text= "Get Folder" , width= 15, command= lambda: self.AskFolder( output_Input) )

        output_label.grid(row= 6, column= 0, padx= 2, pady= 2, sticky= 'W' )
        output_button.grid(row=6, column= 1, padx= 3, pady= 2 , sticky= 'E')
        output_Input.grid(row= 7, columnspan= 2, padx= 5, pady= 5)

        self.certificate = certificate_Input.get()
        self.excel = Excel_Input.get()
        self.output = output_Input.get()

    def AskPath(self, name , Extention, Entry_Box):
        File_Path = filedialog.askopenfilename( initialdir=os.getcwd(), title= ("Select " + name), defaultextension= Extention, filetypes= ((name, Extention), ("All Files", "*.*")))
        Entry_Box.insert(0, File_Path)

        if name == 'image':
            self.master.set_certificate(File_Path)
        else:
            self.master.set_Excel(File_Path)

        return File_Path
    

    def AskFolder(self, Output_Input):
        Folder_Path = filedialog.askdirectory(initialdir=os.getcwd(), title="Output Folder")
        Output_Input.insert(0, Folder_Path)
        self.master.set_output(Folder_Path)
        return Folder_Path 
    
    
    def start(self):
        self.mainloop()