import cv2 as cv

img = cv.imread('P_2/Averaging/img.jpeg')
cv.imshow('blurred img', img)
cv.waitKey(0)
cv.destroyAllWindows()

blur = cv.blur(img, (10,10))

cv.imshow('blurred img', blur)
cv.waitKey(0)
cv.destroyAllWindows()