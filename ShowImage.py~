import numpy as np
import cv2

img = cv2.imread('redShirt.png')
b,g,r = cv2.split(img)
img2 = cv2.merge((b,g,r))


(h,w) = img2.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270,1.0)
rotated = cv2.warpAffine(img, M,(w,h))
cv2.imshow('Rotated', rotated)
cv2.waitKey(10000)
cv2.destroyAllWindows()
