from tkinter import *
from tkinter.font import Font
import smtplib
from email.message import EmailMessage
import imghdr


class EmailEditor(Toplevel):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.geometry('600x650')
        

        self.CreateInputFrame()
        self.CreateTextBox()
        self.Editorbutton()

    





        





    def start(self):
        self.mainloop()
    

    def CreateInputFrame(self):

        self.__font = Font(family='arial', size= 11, weight='normal')
        x_pad = 5
        y_pad = 2
        entry_width = 35

        
        self.r = StringVar()
        self.r.set('.pdf')
        input = Frame(self,  padx= 2,  pady= 2 , border= 0)
        input.pack(padx= 2, pady= 2)

        radio1 = Radiobutton(input, text= 'Attach PDF', variable= self.r , value= '.pdf' )
        radio2 = Radiobutton(input, text= 'Attach Image', variable= self.r , value= '.jpg' )

        radio1.grid(row= 0, column= 0)
        radio2.grid(row= 0, column= 1)


        sender_Label = Label(input, text= "Enter Senders Email", border= 0,width= 20 , font= self.__font)
        sender_password_label = Label(input, text= "Enter Senders Password" , border= 0, width= 20, font= self.__font)
        Subject_label = Label(input, text=  "Subject" , border= 0, width= 60, font= self.__font, anchor= 'w')

        self.sender_Email = Entry(input , border= 0,width= entry_width, font= self.__font, )
        self.sender_password_Entry = Entry(input , border= 0,width= entry_width, font= self.__font)
        self.Subject_Entry = Entry(input , border= 0, width= 2*entry_width,font= self.__font)



        sender_Label.grid(row= 1, column= 0, padx= x_pad, pady= y_pad)
        self.sender_Email.grid(row= 2, column= 0 , padx= x_pad, pady= y_pad)

        sender_password_label.grid(row= 1, column= 1 , padx= x_pad, pady= y_pad)
        self.sender_password_Entry.grid(row= 2, column= 1, padx= x_pad, pady= y_pad)

        Subject_label.grid(row= 3, columnspan= 2 , padx= x_pad, pady= y_pad)
        self.Subject_Entry.grid(row= 4, columnspan=2, padx= x_pad, pady= y_pad)
        
    def CreateTextBox(self):

        self.Editor = Frame(self, padx= 2, pady= 2,width= 590, height= 480, bg= '#dddddd')
        self.Editor.pack(padx= 2, pady= 2)

        self.text_box = Text(self.Editor, width= 400, height= 480, background= '#555555', fg= '#dddddd', font= self.__font)
        
        self.text_box.place(relwidth= 0.98, relheight= 0.98, x=5, y= 5, in_= self.Editor)

    def Editorbutton(self):
        self.Editor_button = Frame(self, width= 590, height= 90, padx= 2, pady= 2 ,)
        self.Editor_button.pack(padx= 2, pady= 2 )

        Save_Draft = Button(self.Editor_button, text= "Save Draft",padx= 2, pady=2, command= self.Get_text)
        Send_Mail = Button(self.Editor_button, text= "Send Email",padx= 2, pady=2, command= self.SendEmail)
        Exit = Button(self.Editor_button, text= "Exit" ,padx= 2, pady=2, command= self.destroy)


        Save_Draft.grid(row= 0, column= 0,padx= 2, pady=2)
        Send_Mail.grid(row= 0, column= 1,padx= 2, pady=2)
        Exit.grid(row= 0, column= 2,padx= 2, pady=2)

    def Get_text(self):
        self.user_email = self.sender_Email.get()
        self.user_password = self.sender_password_Entry.get()
        self.subject = self.Subject_Entry.get()
        self.email_body = self.text_box.get(1.0, END)

        
    
    def SendEmail(self):
        self.Get_text()
        name_list = self.master.NameList
        email_list = self.master.email_list
        attach_ment_folder = self.master.output

        print(name_list, email_list, attach_ment_folder)

        print(self.user_email, self.user_password, self.subject, self.email_body )





        for i in range(0,len(name_list), 1):
            en = EmailMessage()
            en['from'] = self.user_email
            en['to'] = email_list[i]
            en['subject'] = self.subject
            en.set_content(self.email_body)

            file_path = 'Output' + '/' + name_list[i] + self.r.get()

            with open(file_path, mode= 'rb') as attach_file_path:
                data = attach_file_path.read()
                if(self.r.get() == '.pdf'):
                    en.add_attachment(data, maintype = 'PDF', subtype = 'pdf', filename = name_list[i]+ '.pdf')
                else:
                    en.add_attachment(data , maintype = 'image', subtype = 'jpeg', filename = name_list[i] + '.jpg') 

            try:
                with  smtplib.SMTP_SSL('smtp.gmail.com',465)  as server:   
                
                    server.login(self.user_email, self.user_password)
                    server.send_message(en)
            except:
                pass

        print("message Sent")








  








    