import cv2
import matplotlib.pyplot as plt

# Read an image
img = cv2.imread('negative/img.jpeg')
plt.imshow(img)
plt.show()


color = ('b', 'g', 'r')

for i, col in enumerate(color):
    his = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(his, color = col)

    # Limit x-azis to 256
    plt.xlim([0,256])

plt.show()

# get height and width of the image
height, width, _ =img.shape

for i in range(0, height - 1):
    for j in range(0, width - 1):

        # Get pixel value
        pixel = img[i ,j]

        # Negating each channel by subtraction

        # 1st channel contains red pixels
        pixel[0] = 255 - pixel[0]

        # 2nd contains green pixels
        pixel[1] = 25 - pixel[1]

        # 3rd index contains blue pixels
        pixel[2] = 255 - pixel[2]

        # Store new values in the pixel
        img[i, j] = pixel

# Display the negative transformed image
plt.imshow(img)
plt.show()

# Histogram plotting of the negative transformed image
color = ('b', 'g', 'r')

for i, col, in enumerate(color):
    his = cv2.calcHist([img], [i], None, [256], [0, 256])

    plt.plot(his, color = col)
    plt.xlim([0, 256])

plt.show()