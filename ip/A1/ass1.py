import cv2 as cv
img1=cv.imread('download.jpeg', 0)
cv.imshow('Image',img1)
cv.waitKey(10000)
img2=cv.imread('download.tiff')
cv.imshow('Image2',img2)
cv.waitKey(10000)
cv.destroyAllWindow()
