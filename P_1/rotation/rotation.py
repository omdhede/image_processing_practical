import cv2


try:
    res = cv2.imread("rotation/img.jpeg")
    (rows, cols) = res.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res2 = cv2.warpAffine(res, M, (cols, rows))
    
    #creating a new image for display
    cv2.imwrite('result.jpg', res2)
    window_name = 'res2'
    
    # #display window
    cv2.imshow(window_name, res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except IOError:
    print('GGs')