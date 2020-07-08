import cv2
import numpy as np
from PIL import ImageEnhance  
# Open the image.
n = 1
while n:
    a = int(input("1.Log Transform \n2.Gamma Transform \n3.Negation \n4.Constrast Sharpening"))
    if(a == 2):
        img = cv2.imread('image.jpg')
        # Trying 4 gamma values.
        for gamma in [0.01, 0.05, 1.2, 2.2]:
            # Apply gamma correction.
            gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
   # Save edited images.
            cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
            cv2.imshow('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
    elif(a == 1):
        # Open the image.
        img = cv2.imread('image.jpg')
        # Apply log transform.
        c = 255/(np.log(1 + np.max(img)))
        log_transformed = c * np.log(1 + img)  
        # Specify the data type.
        log_transformed = np.array(log_transformed, dtype = np.uint8)
        # Save the output.
        cv2.imwrite('log_transformed.jpg', log_transformed)
        cv2.imshow('log_transformed.jpg', log_transformed)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a==3):
        img1 = cv2.imread('image.jpg')
        negation = cv2.bitwise_not(img1,img1)
        cv2.imshow('bitwise_not',negation)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a == 4):
        # Read the image
        img1 = cv2.imread('image.jpg',0)
        # Create zeros array to store the stretched image
        minmax_img = np.zeros((img1.shape[0],img1.shape[1]),dtype = 'uint8')
 
        # Loop over the image and apply Min-Max formulae
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                minmax_img[i,j] = 255*(img1[i,j]-np.min(img1))/(np.max(img1)-np.min(img1))
 
        # Displat the stretched image
        cv2.imwrite('contrast_streching',minmax_img)
        cv2.imshow('Minmax',minmax_img)
        cv2.waitKey(1000)
    elif( a == 5):
        im = Image.open('image.jpg')
        #Display image  
        im.show()
        enh = ImageEnhance.Contrast(im)  
        enh.enhance(1.8).show("30% more contrast")    
    n = int(input("Enter 1 to continue:"))    
