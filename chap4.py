import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[200:300,100:300]=255,0,0
#img[:]=255,0,0    (to print the color blue using index)

#cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# width first and then height

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# use cv2.FILLED to fill the rectangle

cv2.circle(img,(400,50),30,(255,255,0),5)

cv2.putText(img,"OPEN CV",(300,300),cv2.FONT_ITALIC,0.7,(0,150,0),3)

cv2.imshow("Image",img)



cv2.waitKey(0)