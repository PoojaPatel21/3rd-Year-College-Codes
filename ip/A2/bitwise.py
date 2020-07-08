#bitwise operations on images 
import cv2  
import numpy as np

img1 = cv2.imread('chess2.png')
img2 = cv2.imread('chess1.png')
img1 = cv2.resize(img1,(500,500))
img2 = cv2.resize(img2,(500,500)) 
n = 1
while n == 1:
    a = int(input("Enter 1 ,2 ,3 ,4 for bitwise or , xor ,and and nor rerspectively:"))
    if(a==1):
        bitor = cv2.bitwise_or(img1,img2)
        cv2.imshow('bitwise_or',bitor)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a==2):
        bitxor = cv2.bitwise_xor(img1,img2)
        cv2.imshow('bitwise_xor',bitxor)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a==3):
        bitand = cv2.bitwise_and(img1,img2)
        cv2.imshow('bitwise_and',bitand)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a==4):
        bitnor = cv2.bitwise_not(img1,img2)
        cv2.imshow('bitwise_not',bitnor)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    else:
        print("Enter Valid Input 1,2,3,4")
    n=int(input("Enter 1 to continue:"))
