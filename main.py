from Modules import GetCordinates

import input

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from cv2 import imread
from cv2 import imshow
from cv2 import imwrite


#Path of Cerfificate , Font and OutputFolder
certificate_path, font_path, output_folder = input.get_paths()

top_left_x, top_left_y, bottom_right_x, bottom_right_y = GetCordinates.Position(certificate_path)

name_list = input.Get_Name_List()

red, green , blue = input.get_color()




MyFont = ImageFont.truetype( font_path, 70)



for name in name_list:
    img = Image.open(certificate_path)
    I1 = ImageDraw.ImageDraw(img)
    I1.text((top_left_x, bottom_right_y), name, (red, green, blue), font= MyFont)
    img.save(output_folder + '/' + name + '.jpg')


print('Program Complete')

#Program Completer
