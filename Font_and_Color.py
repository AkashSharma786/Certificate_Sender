
import tkinter as tk
from tkinter import font

class Font_And_Color(tk.Frame):


       

      
    def ChangeFont(self, red, green , blue, font_name, font_weight, font_size ):
        if(font_size == ''):
            font_size = '12'
        
        r = hex(int(red))[2:]  
        g = hex(int(green))[2:]  
        b = hex(int(blue))[2:]

        if(len(r) == 1 ):
            r= '0'+r
        if(len(g) == 1 ):
            g= '0'+ g
        if(len(b) == 1 ):
            b= '0'+ b

        color = '#' + r + g + b

        self.Welcome.config(font=(font_name, int(font_size), font_weight), fg=color)

        self.master.set_font((color, font_name, font_size, font_weight))
        
        
        return (color, font_name, font_size, font_weight)
        

        

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        super().__init__(parent)
        
        global Font_preview


        font_and_color = tk.LabelFrame(self, width= 340, height= 200, pady= 5)
        font_and_color.grid( padx= 5, pady= 5)

        Font_Selection = tk.LabelFrame(font_and_color,height=  50, width= 338, pady=3)
        Font_preview = tk.LabelFrame(font_and_color, height= 80, width= 338, pady= 3)
        Color_Selection = tk.LabelFrame(font_and_color, height= 110, width= 338, pady= 3)


        Font_Selection.grid(row = 0, column = 0, padx = 2, pady = 2, sticky= 'EW')
        Font_preview.grid(column= 0, row= 1, pady=2, padx= 2)
        Color_Selection.grid(row= 2, column= 0, pady=2, padx= 2)

        Welcome = tk.Label(Font_preview, text= "Hello World!")
        Welcome.grid()
        self.Welcome = Welcome


        global fonts
        fonts = list(font.families())
        FONT = tk.StringVar()
        FONT.set(fonts[0])

        weg = tk.StringVar()
        weg.set('normal')

       

        font_label = tk.Label(Font_Selection, text= "Select Font", width= 25)
        sizeLabel = tk.Label(Font_Selection, text= "Size" , width= 5 )
        weight = tk.Label(Font_Selection, text= "Weight", width= 5)
        font_Name  = tk.OptionMenu(Font_Selection,FONT,  *fonts )
        font_size  = tk.Entry(Font_Selection, width= 8  )
        font_weight  = tk.OptionMenu(Font_Selection,weg,'normal', 'bold' )
        
        
        font_label.grid(row= 0, column= 0,sticky= 'W' , padx= 2)
        sizeLabel.grid(row= 0, column= 1, padx= 2)
        weight.grid(row= 0, column= 2, sticky= 'E',padx= 2)
        font_Name.grid(row=1, column= 0, sticky= 'EW', padx= 2)
        font_size.grid(row=1, column=1, padx= 2)
        font_weight.grid(row=1, column= 2, sticky= 'ES', padx=2)



        
        
        Red = tk.Scale(Color_Selection, orient= 'horizontal', from_= 0, to= 255, cursor= 'dot' , length= 330, showvalue= 0 , width= 10, troughcolor= 'red')
        Green = tk.Scale(Color_Selection, orient= 'horizontal', from_= 0, to= 255, cursor= 'dot' , length= 330, showvalue= 0  , width= 10, troughcolor= 'green')
        Blue = tk.Scale(Color_Selection, orient= 'horizontal', from_= 0, to= 255, cursor= 'dot' , length= 330 , showvalue= 0 , width= 10, troughcolor= 'blue')
        getPreview = tk.Button(Color_Selection, text= "Show PreView", command= lambda: self.ChangeFont(Red.get(), Green.get(), Blue.get(), FONT.get(), weg.get() , font_size.get()))

        self.font_style = self.ChangeFont(Red.get(), Green.get(), Blue.get(), FONT.get(), weg.get() , font_size.get())
        

        
        Red.grid(row= 1, column= 0)
        Green.grid(row= 2, column= 0)
        Blue.grid(row= 3,column=  0)
        getPreview.grid(row= 4, column= 0)



    def start(self):
        self.mainloop()