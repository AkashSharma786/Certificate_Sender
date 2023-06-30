from tkinter import *
from tkinter.font import Font
import smtplib
from email.message import EmailMessage
import imghdr
import os


class EmailEditor(Toplevel):

    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.geometry('750x550')
        self.config(bg= '#2d2d32')

        self.label_bg= '#2d2d32'
        self.btn_background = '#007acc'
        self.Entry_bg = '#2e3a3b'
        self.ffg = '#ffffff'
        self.default_email = 'techpyrates@gmail.com'
        self.default_password = 'mjxixpmqzmnnzsru'
        self.use_default = IntVar()
        self.use_default.set(1)


        self.CreateInputFrame()
        self.CreateTextBox()
        self.Editorbutton()




    def start(self):
        self.mainloop()
    

    def CreateInputFrame(self):



        self.__font = Font(family='arial', size= 11, weight='normal')
        x_pad = 0
        y_pad = 15
        entry_width = 35

        
        self.r = StringVar()
        self.r.set('.pdf')
        input = LabelFrame(self,  padx= 5,  pady= 2 , border= 0, bg= self.label_bg, width= 150, height= 200, font= self.__font)
        input.grid(row= 0, column= 0)

        text_label = Label(input, text= "Index of Entry in Spread Sheet", bg= self.label_bg, fg= self.ffg , font= self.__font)
        text_label.grid(row= 0, column= 0, rowspan= 1, columnspan= 4, sticky= 'W')

        row_label = Label(input , text= 'Row' , bg= self.label_bg, fg= self.ffg , font= self.__font)
        row_label.grid(row= 1, column= 0,  pady= y_pad , sticky= 'W' )

        self.row_Entry = Entry(input , width= 5 , bg= self.Entry_bg, fg= self.ffg, insertbackground= 'white', font= self.__font )
        self.row_Entry.grid(row= 1, column=1, padx= x_pad, pady= y_pad , sticky= 'W' )

        column_label = Label(input , text= 'column' , bg= self.label_bg, fg= self.ffg , font= self.__font)
        column_label.grid(row= 1, column= 2,  pady= y_pad , sticky= 'W' )

        self.column_Entry = Entry(input , width= 5 , bg= self.Entry_bg, fg= self.ffg , insertbackground= 'white' , font= self.__font)
        self.column_Entry.grid(row= 1, column= 3, padx= x_pad, pady= y_pad , sticky= 'W' )




        radio1 = Radiobutton(input, text= 'Attach PDF', variable= self.r , value= '.pdf' , fg= self.ffg, bg= self.label_bg, activebackground= self.label_bg, selectcolor= self.label_bg, activeforeground= self.btn_background , font= self.__font)
        radio2 = Radiobutton(input, text= 'Attach Image', variable= self.r , value= '.jpg' ,fg= self.ffg , bg= self.label_bg, selectcolor= self.label_bg, activebackground= self.label_bg, activeforeground= self.btn_background , font= self.__font)

        

        radio1.grid(row= 2, column= 0, rowspan= 1, columnspan= 2, padx= x_pad, pady= y_pad , sticky= 'W' )
        radio2.grid(row= 2, column= 2, rowspan= 1, columnspan= 2, padx= x_pad, pady= y_pad , sticky= 'W' )
        


        sender_Label = LabelFrame(input, text= "Enter Senders Email",  width= 150, height= 20, font= self.__font , bg= self.label_bg , fg= self.ffg , relief= 'flat')
        sender_Label.grid(row= 3, column= 0, rowspan= 1, columnspan= 4, padx= x_pad, pady= y_pad, sticky= 'W' )

        self.sender_Email = Entry(sender_Label , width= entry_width, font= self.__font, state= 'disabled', bg= self.Entry_bg, fg= self.ffg, insertbackground= 'white', disabledbackground= self.label_bg)
        self.sender_Email.grid(row= 0, column= 0  , rowspan= 1, columnspan= 4, padx= x_pad, pady= y_pad , sticky= 'W'  )




        sender_password_label = LabelFrame(input, text= "Enter Senders Password" ,  width= 150, height= 20 ,  font= self.__font , bg= self.label_bg , fg= self.ffg,  relief= 'flat')
        sender_password_label.grid(row= 4, column= 0 , rowspan= 1, columnspan= 4 , padx= x_pad, pady= y_pad , sticky= 'W' )

        
        self.sender_password_Entry = Entry(sender_password_label, width= entry_width,state= 'disabled', font= self.__font , bg= self.Entry_bg, fg= self.ffg , insertbackground= 'white', disabledbackground= self.label_bg)
        self.sender_password_Entry.grid(row= 0, column= 0 , rowspan= 1, columnspan= 4, padx= x_pad, pady= y_pad , sticky= 'W' )

        default_email_checkbox = Checkbutton(input,command= self.DisableEntry , text= 'Use system email (techpyrates@gmail.com)',variable= self.use_default, onvalue= 1, offvalue= 0,  fg= self.ffg, bg= self.label_bg, activebackground= self.label_bg, selectcolor= self.label_bg)

        


        
        

        
        
        default_email_checkbox.grid(row= 5, column= 0 , rowspan= 1, columnspan= 4, pady= 2 , sticky= 'W' )

    def DisableEntry(self):
        if(self.use_default.get() == 1):
            self.sender_Email.config(state= 'disabled')
            self.sender_password_Entry.config(state= 'disabled')
        else:
            self.sender_Email.config(state= 'normal')
            self.sender_password_Entry.config(state= 'normal')

        
    def CreateTextBox(self):
        x_pad  = 2
        y_pad = 2

        entry_width = 53



        self.Editor = Frame(self, padx= x_pad, pady= y_pad , width= 450, height= 545 , bg= self.label_bg)
        self.Editor.grid(row= 0, column=1, rowspan= 2, columnspan= 1, padx= x_pad, pady= y_pad)

        Subject_label = Label(self.Editor, text=  "Subject" , font= self.__font , bg= self.label_bg , fg= self.ffg)
        self.Subject_Entry = Entry(self.Editor ,  width= entry_width ,font= self.__font , bg= self.Entry_bg, fg= self.ffg , insertbackground= 'white')

        Subject_label.grid(row= 0, column= 0 , padx= x_pad, pady= y_pad, sticky= 'W')
        self.Subject_Entry.grid(row= 1, column= 0, padx= x_pad, pady= y_pad , sticky= 'W')

        text_box_frame = LabelFrame(self.Editor, width= 442, height= 500 , bg = self.label_bg, fg= self.ffg, relief= 'flat')
        text_box_frame.grid(row= 2, column= 0)

        self.text_box = Text(text_box_frame, background= self.Entry_bg, fg= self.ffg, font= self.__font, insertbackground= 'white')
        
        self.text_box.place(relwidth= 0.98, relheight= 0.98)

    def Editorbutton(self):
        btn_width = 8
        x_pad = 2
        y_pad = 2
        self.Editor_button = Frame(self, width= 150, height= 20, padx= x_pad, pady= y_pad , bg= self.label_bg)
        self.Editor_button.grid(row= 1, column= 0,padx= x_pad, pady= y_pad )

        Save_Draft = Button(self.Editor_button, text= "Save Draft",padx= x_pad, pady= y_pad, width= btn_width ,command= self.Get_text, bg= self.btn_background, fg= self.ffg)
        Send_Mail = Button(self.Editor_button, text= "Send Email",padx= x_pad, pady= y_pad, width= btn_width, command= self.SendEmail , bg= '#129d00', fg= self.ffg)
        

        Save_Draft.grid(row= 0, column= 0,padx= x_pad, pady= y_pad)
        Send_Mail.grid(row= 0, column= 1,padx= x_pad, pady= y_pad)
        

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
        name_list = self.master.primary_list

        email_list = self.master.Get_Text_List(int(self.row_Entry.get()), int(self.column_Entry.get()))
        
        attach_ment_folder = self.master.output

        print(name_list, email_list, attach_ment_folder)

        if(self.use_default.get() == 1):
            self.user_email = self.default_email
            self.user_password = self.default_password
        else:
            self.user_email = self.sender_Email.get()
            self.user_password = self.sender_password_Entry.get()


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
        self.destroy()

        








  








    