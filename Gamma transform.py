import numpy as np
import cv2

img = cv2.imread(r'C:\Users\18801\Desktop\1.png', 0)
new_img = np.power(img, 5.0)
cv2.normalize(new_img, new_img, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('new_img', new_img)
cv2.imwrite(r'C:\Users\18801\Desktop\new_img.png', new_img)
cv2.waitKey(0)
