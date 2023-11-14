import cv2

# -1 == cv2.IMREAD_COLOR //no transparency/alpha
# 0 == cv2.IMREAD_GRAYSCALE //no color
# 1 == cv2.IMREAD_UNCHANGED //load all data
img = cv2.imread('assets/image.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('newImage.jpg', img)
cv2.imshow('ImageDemo1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

