import cv2
import numpy as np
#Read First Image
imgBGR=cv2.imread('download.jpeg')
#Read Second Image
imgRGB=cv2.imread('download.jpeg')
 
#cv2.imshow('bgr',imgBGR)
#cv2.imshow('rgb',imgRGB)
#concatanate image Horizontally
img_concate_Hori=np.concatenate((imgBGR,imgRGB),axis=1)
cv2.imshow('concatenated_Hori',img_concate_Hori)
cv2.waitKey(0)
cv2.destroyAllWindows()
