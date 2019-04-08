import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np 
import cv2

def greenScreen(image,backgroundImage,alignment):
    '''
    Will detect and change the "Green Screen" background to a desired background image.
    :param str image: The original image with green screen
    :param str backgroundImage: The background image that will replace the green screen
    :param str alignment: The orientation of the image. (horizontal or vertical) 
    
    '''
   
    #Making sure both images are Vertical
    if alignment == "horizontal":
        if(image.shape[0] > image.shape[1]):
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    if alignment == "vertical":
        if(image.shape[0] < image.shape[1]):
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    
    # resize the image
    backgrounImage_Resized = cv2.resize(backgroundImage, (image.shape[1], image.shape[0]))
                
   #define color boundaries/treshold (lower and upper limits)
    lower_green = np.array([0,100,0])
    upper_green = np.array([100, 255, 130]) 
    
    #Setting up the rainge of green we are gonna change
    mask = cv2.inRange(image,lower_green, upper_green)

    #Copy of image that is going to have the mask
    masked_image = np.copy(image)
    
    #Turn black everything that is white on the mask
    masked_image[mask != 0] = [0,0,0]

    bgr_img = backgrounImage_Resized.copy()
    
    #Set everythign that is black on the mask, as black on the background image
    bgr_img[mask == 0] = [0,0,0]
    
    #Merge both images
    final_image = bgr_img + masked_image
    
    #Show the final picture
    plt.imshow(final_image)
    plt.show()
    
   
if __name__ == "__main__":
    print("This program will allow you to change the \ngreen screen of an image to a desired background.")
    background = r"C:\Users\lexdy\Desktop\ProblemSolvingProject\Images\background.jpg"#"Paste the full path of the desired background."
    image = r"C:\Users\lexdy\Desktop\ProblemSolvingProject\Images\car.jpg" #"Paste the full path of the image with green screen."

    backgroundImage = mpimg.imread(background)
    image = mpimg.imread(image)

    greenScreen(image = image ,backgroundImage = backgroundImage, alignment = 'horizontal')