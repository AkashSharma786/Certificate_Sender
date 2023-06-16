import cv2
from os import remove


def drawRectangle(event, x, y, flags, params):
    global left_x, left_y, right_x, right_y, drawRect, mini_image
    
    
    if event == cv2.EVENT_LBUTTONDOWN:  # Check left mouse button click.
        drawRect = True
        left_x, left_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # Check left mouse button movement.
        if drawRect == True:
            mini_image = cv2.imread('test.jpg')
            cv2.rectangle(mini_image, (left_x, left_y), (x, y), (0, 0, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:  # Check left mouse button release.
        drawRect = False
        right_x, right_y = x, y

        # For selecting rectangle from top->bottom and bottom->top
        left_x, right_x = sorted([left_x, right_x])
        left_y, right_y = sorted([left_y, right_y])


def Position( Img_Path):
    global mini_image 
    mini_image = get_mini_image(Img_Path)
    cv2.namedWindow("NTC", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("NTC", 600, 600)
    cv2.setMouseCallback("NTC", drawRectangle)
    
    while True:
        cv2.imshow("NTC", mini_image)
        key = cv2.waitKey(1)    # Checking key pressed in the keyboard.
        if key == 13:   # Enter key is pressed.
            break
    cv2.destroyWindow("NTC")
    remove('test.jpg')
    
    return (left_x *4 , left_y *4, right_x *4 , right_y*4)


def get_mini_image( Img_Path):
    image = cv2.imread(Img_Path)
    
    image_file_extension = Img_Path.split(".")[-1]

    height, width, channels = image.shape
    mini_image = cv2.resize(
        image, (width//4, height//4))
    cv2.imwrite("test.{}".format(image_file_extension), mini_image)
    
    return mini_image
