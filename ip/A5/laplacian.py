#built in code for laplacian edge detection / 2nd order derivative 
import cv2
image2 = cv2.imread('img1.jpg',0)

#Apply Guassian Blur
blur = cv2.GaussianBlur(image2,(3,3),0)

new_image = cv2.Laplacian(blur,cv2.CV_64F)
new_image2 = new_image/new_image.max()
cv2.imshow('Laplacian',new_image2)
cv2.waitKey(1000)
cv2.destroyAllWindows()

