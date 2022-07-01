import cv2
import numpy as np

img = cv2.imread(r'C:\Users\18801\Desktop\1.png', 0)
new_img = 1.0 * (np.log(1.0 + img))
# 上式运算完存在大于255的灰度级，需要将范围限制在0-255
Processed_img = cv2.normalize(new_img, new_img, 0, 255, cv2. NORM_MINMAX)
cv2.imshow('img', img)
cv2.imshow('Processed_img', Processed_img)
cv2.imwrite(r'C:\Users\18801\Desktop\Processed image.png', Processed_img)
cv2.waitKey(0)
