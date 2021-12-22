import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../data/PennFudan/PedMasks/FudanPed00001_mask.png', 0)

print(img.shape)
plt.imshow(img)
plt.show()