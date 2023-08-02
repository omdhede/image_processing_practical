import cv2

# import numpy as np

try: 
    # image import
    img = cv2.imread("resizing\img.jpeg")
    
    #display original image
    cv2.imshow('Original', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #resizing original img
    (height, width) = img.shape[:2]
    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
    
    #writing original img to result.jpg
    cv2.imwrite('result.jpg', res)
    window_name = 'res'
    
    #display result img
    cv2.imshow(window_name, res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # #rotating the resized image
    



    # # Cropping Image
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # # Print type of the image
    # print(type(img))

    # # Print the dimensions of the image
    # print('Dimensions of the image', img.shape)

    # # Cropping the original image
    # crop = img[80:580, 160:900]
    # cv2.imshow('Original', img)
    # cv2.imshow('Crop', crop)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    
except IOError:
    print('GGs')