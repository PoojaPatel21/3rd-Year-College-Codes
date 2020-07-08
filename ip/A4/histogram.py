import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#original image
img = cv.imread('img2.jpeg',0)
cv.imshow("Original" ,img)
cv.waitKey(1000)

#graph of original image
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

#Equalised image
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
cv.imshow("Equalized",img2)
cv.waitKey(1000)

#gragh of equalised image
hist1,bins1 = np.histogram(img2.flatten(),256,[0,256])
cdf1 = hist.cumsum()
cdf_normalized1 = cdf1 * float(hist.max()) / cdf1.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

