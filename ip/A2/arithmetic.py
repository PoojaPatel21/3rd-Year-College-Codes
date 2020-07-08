#arithmetic operations on images
import cv2  
import numpy as np

img1 = cv2.imread('chess2.png')
img2 = cv2.imread('chess1.png')
img1 = cv2.resize(img1,(500,500))
img2 = cv2.resize(img2,(500,500))
n = 1
while n == 1:
    a = int(input("Enter 1 ,2 ,3 ,4 for Addition , Subtraction , Multiplication and Division respectively:"))
    if(a==1):
        sum1 = cv2.add(img1,img2)
        cv2.imshow('add',sum1)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a==2):
        diff = cv2.subtract(img1,img2)
        cv2.imshow('sub',diff)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a==3):
        mult = cv2.multiply(img1,img2)
        cv2.imshow('Multi',mult)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    elif(a==4):
        div = cv2.divide(img1,img2)
        cv2.imshow('Div',div)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    else:
        print("Enter Valid Input 1,2,3,4")
    n=int(input("Enter 1 to continue:"))