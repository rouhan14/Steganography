import cv2 as cv
import numpy as np

img = cv.imread('Image_01.bmp')

x = img.shape[1]
y = img.shape[0]

table = {}
stages = 0  # Moved the stages variable outside the loop

for i in range(x):
    for j in range(y):
        
        if (i >= 1 and j >=1 and i <= (x-1) and j <= (y-1)):
            
            if (img[i][j][0] != 0 or img[i][j][1] != 0 or img[i][j][2] != 0):
                
                if (img[i-1][j][0] != 0 or img[i-1][j][1] != 0 or img[i-1][j][2] != 0):
                    img[i][j] = img[i-1][j]
                elif (img[i][j-1][0] != 0 or img[i][j-1][1] != 0 or img[i][j-1][2] != 0):
                    img[i][j] = img[i][j-1]
                elif (img[i-1][j-1][0] != 0 or img[i-1][j-1][1] != 0 or img[i-1][j-1][2] != 0):
                    img[i][j] = img[i-1][j-1]
                elif (img[i-1][j+1][0] != 0 or img[i-1][j+1][1] != 0 or img[i-1][j+1][2] != 0):
                    img[i][j] = img[i-1][j-1]
                else:   # If the values have not been assigned. Assign the values to the table and over here.
                    # Assigning a new plane
                    stages += 1
                    table[f'{stages}'] = [np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)]  # Assigned random colors
                    img[i][j] = table[f'{stages}']  # Assign color from table

# Implementing the second pass for 8-bit connectivity
for i in range(x):
    for j in range(y):
        if (i >= 1 and j >=1 and i <= (x-1) and j <= (y-1)):
            if (img[i][j][0] != 0 or img[i][j][1] != 0 or img[i][j][2] != 0):
                min_label = img[i][j]
                if (img[i-1][j][0] != 0 or img[i-1][j][1] != 0 or img[i-1][j][2] != 0):
                    min_label = min(min_label, img[i-1][j])
                if (img[i][j-1][0] != 0 or img[i][j-1][1] != 0 or img[i][j-1][2] != 0):
                    min_label = min(min_label, img[i][j-1])
                if (img[i-1][j-1][0] != 0 or img[i-1][j-1][1] != 0 or img[i-1][j-1][2] != 0):
                    min_label = min(min_label, img[i-1][j-1])
                if (img[i-1][j+1][0] != 0 or img[i-1][j+1][1] != 0 or img[i-1][j+1][2] != 0):
                    min_label = min(min_label, img[i-1][j+1])
                img[i][j] = min_label

cv.imshow("Image", img)
cv.waitKey(0)
