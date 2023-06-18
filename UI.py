from tkinter import *

root = Tk()
root.title('Tech Pirates')

main_frame = LabelFrame(root, padx= 10, pady= 10, bg= '#a19664' )
main_frame.pack()




control_frame = LabelFrame (main_frame, width= 350, height= 650, bg= '#d8c989')
preview_frame = LabelFrame(main_frame, width= 600, height= 571,bg= '#d8c989')

control_frame.grid(row= 0, column= 0, padx= 10, pady= 10, sticky= 'S')
preview_frame.grid(row= 0, column=1 , padx= 10, pady= 10, sticky= 'S')






path_selection = LabelFrame(control_frame, width= 340, height= 300, pady= 5)
Font_and_Color = LabelFrame(control_frame, width= 340, height= 200)
Final_Buttons = LabelFrame(control_frame, width= 340, height= 110)


path_selection.grid(row= 0, column= 0, padx= 5, pady= 5)
Font_and_Color.grid(row= 1, column= 0, padx= 5, pady= 5)
Final_Buttons.grid(row= 3, column= 0, padx= 5, pady= 5)





#Input Fields

certificate_label = Label(path_selection, text= "Select Certificate" )
certificate_Input = Entry(path_selection, width= 55)
certificate_button = Button(path_selection, text= "Get Template", width= 15)

certificate_label.grid(row= 0, column= 0, padx= 2,pady= 2, sticky= 'W' )
certificate_button.grid(row= 0, column= 1, padx= 3, pady= 2, sticky= 'E')
certificate_Input.grid(row= 1, columnspan= 2 , padx= 5, pady= 5)




font_label = Label(path_selection, text= "Select Font")
font_Input = Entry(path_selection, width= 55)
font_button = Button(path_selection, text= "Get Font" , width= 15)

font_label.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'W' )
font_button.grid(row= 2, column= 1, padx= 3, pady= 2 , sticky= 'E')
font_Input.grid(row=3, columnspan= 2, padx= 5, pady= 5)




output_label = Label(path_selection, text= "Select Output Folder" )
output_Input = Entry(path_selection, width= 55)
output_button = Button(path_selection, text= "Get Folder" , width= 15)

output_label.grid(row= 4, column= 0, padx= 2, pady= 2, sticky= 'W' )
output_button.grid(row=4, column= 1, padx= 3, pady= 2 , sticky= 'E')
output_Input.grid(row= 5, columnspan= 2, padx= 5, pady= 5)


Excel_label = Label(path_selection, text= "Select Excel Sheet", )
Excel_Input = Entry(path_selection, width= 55)
Excel_button = Button(path_selection, text= "Get Sheet" , width= 15)

Excel_label.grid(row= 6, column= 0, padx= 2, pady= 2, sticky= 'W' )
Excel_button.grid(row= 6, column= 1, padx= 3, pady= 2 , sticky= 'E')
Excel_Input.grid(row= 7, columnspan= 2, padx= 5, pady= 5)

Font_preview = LabelFrame(Font_and_Color, height= 70, width= 338, pady= 3)
Color_Selection = LabelFrame(Font_and_Color, height= 110, width= 338, pady= 3)

Font_preview.grid(column= 0, row= 0, pady=2, padx= 2)
Color_Selection.grid(row= 1, column= 0, pady=2, padx= 2)

Red = Scale(Color_Selection, orient= 'horizontal', from_= 0, to= 255, cursor= 'dot' , label= 'Red', length= 330, showvalue= 0 , width= 10)
Green = Scale(Color_Selection, orient= 'horizontal', from_= 0, to= 255, cursor= 'dot' , label= 'Green', length= 330, showvalue= 0  , width= 10)
Blue = Scale(Color_Selection, orient= 'horizontal', from_= 0, to= 255, cursor= 'dot' , label= 'Blue', length= 330 , showvalue= 0 , width= 10)

Red.grid(row= 0, column= 0)
Green.grid(row= 1, column= 0)
Blue.grid(row= 2 ,column=  0)

select_position = Button(Final_Buttons, text= 'SelectPosition' , padx= 4, pady= 4, width= 21 )
Img_preview = Button(Final_Buttons, text= 'Preview' , padx= 4, pady= 4 , width= 21)
Store = Button(Final_Buttons, text= 'Store' , padx= 4, pady= 4 , width= 21)
Send = Button(Final_Buttons, text= 'Send Email' , padx= 4, pady= 4 , width= 21)

select_position.grid(row= 0, column= 0 , padx= 4, pady= 4)
Img_preview.grid(row=0, column= 1 , padx= 4, pady= 4)
Store.grid(row=1, column= 0 , padx= 4, pady= 4)
Send.grid(row=1, column= 1 , padx= 4, pady= 4)









mainloop()