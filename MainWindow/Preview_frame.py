from tkinter import *
from PIL import Image, ImageTk

class Preview_Frame(Frame):

    def __init__(self, parent ):
        Frame.__init__(self, parent)
        super().__init__(parent)
        self.config(bg= '#000000')

        
        self.Wrap = LabelFrame(self, width= 600, height= 600 )
        self.Wrap.grid()
        self.Img_Canva = Canvas(self.Wrap, width= 600, height=  600, bg= '#1e1e1e')
        self.Img_Canva.grid()

        self.new_width = 600
        self.new_height = 600
        
        

       
      
    
    def start(self):
        self.mainloop()
    
    def RenderImage(self, image):
        img = Image.open(image)
        width, height = img.size
        max_size = max(width, height)
        if max_size > 600:
            self.new_width = int(round(width * 600 / max_size))
            self.new_height = int(round(height * 600 / max_size))
            print(width, height)
            print(self.new_width, self.new_height)
            img = img.resize((self.new_width, self.new_height), Image.ANTIALIAS)
        
        photo = ImageTk.PhotoImage(img)
        self.Img_Canva.create_image(0, 0, image=photo, anchor="nw")
        self.Img_Canva.image = photo  # Save a reference to the image to prevent garbage collection

    def Create_Rectangle(self):
        self.rectangle = None
        self.Img_Canva.bind('<Button-1>', self.start_Rectangle)
        self.Img_Canva.bind('<B1-Motion>', self.update_Rectangle)
        self.Img_Canva.bind('<ButtonRelease-1>', self.get_coordinate)
        
    def start_Rectangle(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rectangle = self.Img_Canva.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y)

        print("start")
    
    def update_Rectangle(self, event):

        self.Img_Canva.coords(self.rectangle, self.start_x, self.start_y, event.x, event.y)
        print('Dragging')
    
    def get_coordinate(self, event):
        coords = self.Img_Canva.coords(self.rectangle)
        x1 = int(coords[0])
        y1 = int(coords[1])
        x2 = int(coords[2])
        y2 = int(coords[3])

        self.master.control_frame.set_coordinate((x1, y1, x2, y2), self.new_width, self.new_height)

        self.Img_Canva.unbind('<Button-1>')
        self.Img_Canva.delete(self.rectangle)
        
        
   


        


        
