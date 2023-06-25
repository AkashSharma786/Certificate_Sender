from tkinter import *
from MainWindow.Controls.Select_Path import Path_Selection
from MainWindow.Controls.Edit_Buttons import EditButtons
from MainWindow.Controls.Final_Buttons import *
import openpyxl 
from PIL import Image, ImageTk, ImageDraw , ImageFont
from tkinter import font




class Control_Pane(Frame):

    def __init__(self, parent = None ):
        Frame.__init__(self, parent)
        super().__init__(parent)



        Edit_button = EditButtons(self)
        path_selection = Path_Selection(self)
        final_but = Final_Buttons(self)


        path_selection.grid(row= 0, column= 0)
        Edit_button.grid(row= 1, column= 0)
        final_but.grid(row=2, column= 0)

        self.Edit_button = Edit_button
        self.path_selection = path_selection
        self.final_but = final_but
    
    def set_certificate(self, certificate = None):
        self.certificate = certificate
        self.Temp_Folder = certificate
        
        self.master.preview_frame.RenderImage(certificate)

        print(certificate)
    def Set_Row_and_colunmn(self, row, column):
        self.sheet_row = row
        self.sheet_column = column


    def Get_Name_List(self):
        
        path = self.Excel
        name_list = []
        email_list = []

        work_book = openpyxl.load_workbook(path)
        sheet = work_book.active


        for i in range(self.sheet_row, sheet.max_row + 1 , 1):
            name = sheet.cell(column = self.sheet_column,  row = i  ).value
            email = sheet.cell(column = self.sheet_column +1, row = i).value
            name_list.append(name)
            email_list.append(email)
        
        self.NameList = name_list
        self.email_list = email_list
        
        return (name_list, email_list)

    def set_Excel(self, Excel):
        self.Excel = Excel
        
        print(self.NameList, self.email_list)
        
    
    def set_output(self, output):
        self.output = output
        
        

    def set_font(self, __font__):
        self._font = __font__
        
    
    def set_coordinate(self, coordinate, small_width , small_height ):

        self.coordinate = coordinate
        self.small_width = small_width
        self.small_height = small_height
        


        print(coordinate)
    

    def paste_png(self, file_path):

        print(self.Temp_Folder)
        image1 = Image.open(self.Temp_Folder)
        image2 = Image.open(file_path)

        
        width , height = image1.size
        self.ratio = width/self.small_width

        x1 = int(self.coordinate[0]*self.ratio)
        y1 = int(self.coordinate[1]*self.ratio)
        x2 = int(self.coordinate[2]*self.ratio)
        y2 = int(self.coordinate[3]*self.ratio)

        box_width = x2 -x1
        box_height = y2 -y1

        img2_width , img2_height = image2.size

        max_size = max(img2_width, img2_height)

        img2_ratio = img2_width/ img2_height

        new_img_max = int(min(box_width, box_height)*img2_ratio)

        img2_width = int(img2_width * new_img_max /max_size)
        img2_height = int(img2_height * new_img_max /max_size)

        print(box_width, box_height)
        print(img2_width, img2_height)

        image2 = image2.resize((img2_width, img2_height))

        image1 = image1.convert('RGBA')
        image2 = image2.convert('RGBA')

        image1.paste(image2,(x1, y1), image2)
        image1 = image1.convert('RGB')



   
   
        

        image1.save('Background.jpg')


        self.master.preview_frame.RenderImage('Background.jpg')
        

    def Generate_1_image(self, text = None):
        print(self.Temp_Folder)
        print(self.Temp_Folder)
        print(self.Excel)
        print(self.output)
        print(self._font)
        self.Font_folder = 'Font'
        
        sys_family = self._font[0]
        sys_size = int(self._font[1])
        color = self._font[2]
        img = Image.open(self.Temp_Folder)


        width , height = img.size

        self.ratio = width/self.small_width
        

        x1, y1, x2, y2 = self.coordinate

        abcissa = x1 * self.ratio
        ordinate = y1 * self.ratio
        self.abcissa = abcissa

        self.ordinate = ordinate
        print(self.ratio)
        print(abcissa, ordinate)

        __font = ImageFont.truetype(font= (self.Font_folder + '/'+ sys_family) , size= int(sys_size * self.ratio))
        
        print("One Image Generated")
        
        if(text == None):
            text = "Student Name"

        draw = ImageDraw.Draw(img)
        draw.text((abcissa, self.ordinate),text= text,fill= self._font[2],  font=__font, align= 'center'  )

        

        

        img.save('Background.jpg')


        self.master.preview_frame.RenderImage('Background.jpg')

    def Generate_All(self):

        sys_size = int(self._font[1])
        __font = ImageFont.truetype(font= self.Font_folder + '/' + self._font[0] , size= int(sys_size*self.ratio))
        
        for name in self.NameList:
            img = Image.open(self.Temp_Folder)
            I1 = ImageDraw.Draw(img)
            I1.text((self.abcissa, self.ordinate), text= name ,fill= self._font[2], font= __font)

            img.save(self.output+ '/' + name + '.jpg')
        
        



    
    def start(self):
        self.mainloop()








