import cv2

# 读取图像
png = cv2.imread(r"C:\Users\18801\Desktop\1.png", 0)
# 反转变换
reverse_png = 255 - png
# 显示读取图像
cv2.imshow('src_png', png)
# 显示处理图像
cv2.imshow('reverse_png', reverse_png)
cv2.imwrite(r"C:\Users\18801\Desktop\reverse_png.png", reverse_png)
cv2.waitKey(0)
