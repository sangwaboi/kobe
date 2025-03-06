import cv2
import numpy as np

image = cv2.imread('contour1.jpg')
image = cv2.resize(image, None,fx=0.9,fy=0.9)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)

ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

contours,hierarchy = cv2.findContours(binary,mode = cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
print("length of Contours {}".format(len(contours)))
print(contours)

image_copy = image.copy()
image_copy = cv2.drawContours(image_copy,contours,-1,(0,255,0), thickness = 2, lineType=cv2.LINE_AA)

cv2.imshow("GREYscale Image",gray)
cv2.imshow("Draw Contours",image_copy)
cv2.imshow("Binary Image",binary)

cv2.waitKey(0)
cv2.destroyAllWindows()





