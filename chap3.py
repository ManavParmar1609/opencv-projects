import cv2
import numpy as np

img=cv2.imread("cp2077/messi.jpg")
print(img.shape)

imgResize=cv2.resize(img,(600,600))  # width first then height
print(imgResize.shape)

imgCropped=img[50:900,50:650] # height first then width

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Cropped Resize",imgCropped)





cv2.waitKey(0)