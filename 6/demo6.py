import cv2
import random
import numpy as np

img = cv2.imread('assets/Chess_Board.png')
img = cv2.resize(img, (0, 0), fx=.50, fy=.50)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.intp(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda g: int(g), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)


cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()