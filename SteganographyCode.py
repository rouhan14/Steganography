import numpy as np
import cv2
import numpy as np

def label_connected_components(image):
    height, width = image.shape
    labels = np.zeros_like(image, dtype=int)
    current_label = 1
    
    def eight_connectivity(x, y, current_label):
        coord = [(x, y)]
        while coord:
            x, y = coord.pop()
            if labels[x, y] != 0 or image[x, y] == 0:
                continue
            labels[x, y] = current_label
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < height and 0 <= new_y < width:
                        coord.append((new_x, new_y))
    
    for i in range(height):
        for j in range(width):
            if labels[i, j] == 0 and image[i, j] == 1:
                eight_connectivity(i, j, current_label)
                current_label += 1
    
    return labels

def visualize_labels(labels):
    unique_labels = np.unique(labels)
    colors = np.random.randint(0, 255, size=(unique_labels.max() + 1, 3), dtype=np.uint8)
    colors[0]=[0,0,0]
    colored_image = colors[labels]
    return colored_image

binary_image=cv2.imread('Image_01.bmp',-1)
binary_image=np.where(binary_image==255,1,0)



labels = label_connected_components(binary_image)
colored_image = visualize_labels(labels)
cv2.imshow('Labeled Image',  colored_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()