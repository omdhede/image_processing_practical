import cv2 as cv

img = cv.imread('P_2/Averaging/img.jpeg')
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

gaussianblur = cv.GaussianBlur(img, (7,7), 0)

cv.imshow('blurred img', gaussianblur)
cv.waitKey(0)
cv.destroyAllWindows()