import cv2

img = cv2.imread(r'C:\Users\18801\Desktop/1.png', 0)
equ = cv2.equalizeHist(img)
cv2.imshow('img', equ)
cv2.imwrite(r'C:\Users\18801\Desktop\Processed image.png', equ)
cv2.waitKey(0)
