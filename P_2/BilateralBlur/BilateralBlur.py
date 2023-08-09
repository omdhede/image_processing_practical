import cv2 as cv

img = cv.imread('P_2/BilateralBlur/img.jpeg')
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

bilateralBlurring = cv.bilateralFilter(img, 9, 75, 75)

cv.imshow('blurred img', bilateralBlurring)
cv.waitKey(0)
cv.destroyAllWindows()