import cv2
import random
import numpy as np

# device or video file
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # diagonal line across frame
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # reverse of above
    img = cv2.line(frame, (0, height), (width, 0), (0, 255, 0), 5)
    # rectangle, 2nd arg is position, third is radius, last is -1 for thickness to fill
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    # circle
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'FUCK', (200, height - 10), font, 4, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()