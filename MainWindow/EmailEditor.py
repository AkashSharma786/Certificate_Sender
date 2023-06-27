from tkinter import *
from tkinter.font import Font
import smtplib
from email.message import EmailMessage
import imghdr
import os


class EmailEditor(Toplevel):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.geometry('600x650')
        self.config(bg= '#2d2d32')

        self.label_bg= '#2d2d32'
        self.btn_background = '#007acc'
        self.Entry_bg = '#2e3a3b'
        self.ffg = '#ffffff'


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
        input = LabelFrame(self,  padx= 2,  pady= 2 , border= 0, bg= self.label_bg)
        input.pack(padx= 2, pady= 2)

        radio1 = Radiobutton(input, text= 'Attach PDF', variable= self.r , value= '.pdf' , fg= self.ffg, bg= self.label_bg, activebackground= self.label_bg, selectcolor= self.label_bg, activeforeground= self.btn_background)
        radio2 = Radiobutton(input, text= 'Attach Image', variable= self.r , value= '.jpg' ,fg= self.ffg , bg= self.label_bg, selectcolor= self.label_bg, activebackground= self.label_bg, activeforeground= self.btn_background)

        radio1.grid(row= 0, column= 0)
        radio2.grid(row= 0, column= 1)


        sender_Label = Label(input, text= "Enter Senders Email", border= 0,width= 20 , font= self.__font , bg= self.label_bg , fg= self.ffg)
        sender_password_label = Label(input, text= "Enter Senders Password" , border= 0, width= 20, font= self.__font , bg= self.label_bg , fg= self.ffg)
        Subject_label = Label(input, text=  "Subject" , border= 0, width= 60, font= self.__font, anchor= 'w' , bg= self.label_bg , fg= self.ffg)

        self.sender_Email = Entry(input , width= entry_width, font= self.__font, bg= self.Entry_bg, fg= self.ffg, insertbackground= 'white')
        self.sender_password_Entry = Entry(input , width= entry_width, font= self.__font , bg= self.Entry_bg, fg= self.ffg , insertbackground= 'white')
        self.Subject_Entry = Entry(input ,  width= 2*entry_width + 1,font= self.__font , bg= self.Entry_bg, fg= self.ffg , insertbackground= 'white')



        sender_Label.grid(row= 1, column= 0, padx= x_pad, pady= y_pad)
        self.sender_Email.grid(row= 2, column= 0 , padx= x_pad, pady= y_pad)

        sender_password_label.grid(row= 1, column= 1 , padx= x_pad, pady= y_pad)
        self.sender_password_Entry.grid(row= 2, column= 1, padx= x_pad, pady= y_pad)

        Subject_label.grid(row= 3, columnspan= 2 , padx= x_pad, pady= y_pad)
        self.Subject_Entry.grid(row= 4, columnspan=2, padx= x_pad, pady= y_pad)
        
    def CreateTextBox(self):

        self.Editor = Frame(self, padx= 2, pady= 2,width= 590, height= 480, bg= self.label_bg)
        self.Editor.pack(padx= 2, pady= 2)

        self.text_box = Text(self.Editor, width= 400, height= 480, background= self.Entry_bg, fg= self.ffg, font= self.__font, insertbackground= 'white')
        
        self.text_box.place(relwidth= 0.98, relheight= 0.98, x=5, y= 5, in_= self.Editor)

    def Editorbutton(self):
        btn_width = 10
        x_pad = 10
        self.Editor_button = Frame(self, width= 590, height= 90, padx= 2, pady= 2 , bg= self.label_bg)
        self.Editor_button.pack(padx= 2, pady= 2 )

        Save_Draft = Button(self.Editor_button, text= "Save Draft",padx= 2, pady=2, width= btn_width ,command= self.Get_text, bg= self.btn_background, fg= self.ffg)
        Send_Mail = Button(self.Editor_button, text= "Send Email",padx= 2, pady=2, width= btn_width, command= self.SendEmail , bg= '#129d00', fg= self.ffg)
        Exit = Button(self.Editor_button, text= "Exit" ,padx= 2, pady=2, width= btn_width,  command= self.destroy , bg= '#c34318', fg= self.ffg)


        Save_Draft.grid(row= 0, column= 0,padx= x_pad, pady=2)
        Send_Mail.grid(row= 0, column= 1,padx= x_pad, pady=2)
        Exit.grid(row= 0, column= 2,padx= x_pad, pady=2)

    def Get_text(self):

        self.user_email = self.sender_Email.get()
        self.user_password = self.sender_password_Entry.get()
        self.subject = self.Subject_Entry.get()
        self.email_body = self.text_box.get(1.0, END)

        draft_text = open('Draft.txt', 'w')

        draft_str = self.subject +'\n' + self.email_body

        draft_text.write(draft_str)

        draft_text.close()



        
    
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

            file_path = self.master.output+ '/' + name_list[i] + self.r.get()

            

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

        self.master.response.config( text = 'Mail Sent')

        








  








    