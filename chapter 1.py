import cv2

print("Package Imported")

img = cv2.imread("venv/57-576420_baby-moana-wallpaper-hd.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)