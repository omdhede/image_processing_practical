import cv2 as cv

img = cv.imread('P_2/MedianBlur/img.jpeg')
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

medianBlur = cv.medianBlur(img, 5)

cv.imshow('blurred img', medianBlur)
cv.waitKey(0)
cv.destroyAllWindows()