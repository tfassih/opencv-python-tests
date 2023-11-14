import cv2
import random
# -1 == cv2.IMREAD_COLOR //no transparency/alpha
# 0 == cv2.IMREAD_GRAYSCALE //no color
# 1 == cv2.IMREAD_UNCHANGED //load all data
img = cv2.imread('assets/image.jpg', -1)

# modify pixels
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
# copy/paste part of image to elsewhere on image
newImage = img[300:500, 100:200]
img[300:500, 200:300] = newImage

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# (rows, columns, channels[BGR(0,0,0) -> 0-255])
print(img)
