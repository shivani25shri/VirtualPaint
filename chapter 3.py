import cv2
import numpy as np

img = cv2.imread("venv/57-576420_baby-moana-wallpaper-hd.jpg")
print(img.shape)
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)
#cv2.imshow("imgResize", img)
imgCropped = img[46:119, 352:495]
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)