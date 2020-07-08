import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
i='a'

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)
    cv2.imwrite('gausha'+i+'.tiff',frame)
    i=i+'a'
    # Press Q on keyboard to  exit
    if cv2.waitKey(500) & 0xFF == ord('q'):
      break
  else:
    print('Not working')

  # Break the loop
 # else:
  #  break

i='a'
j=0
while j<8:
  image=cv2.imread('gausha'+i+'.tiff',0)
  cv2.imshow('pic',image)
  cv2.waitKey(500)
  j=j+1
  i=i+'a'

cv2.destroyAllWindows()
