import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Circle
from homography_computation import homography_computation
from modify_parse_effect import modify_parse_effect

# from skimage import transform
# from skimage.io import imread, imshow

img = Image.open("./img/Gunkanjima.png")
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(img)
plt.show()

# Represent the 4 points of the rectangular shape
actual_points = [[1097, 531], [1336, 551], [1338, 762], [1098, 767]]
projected_points = [[1097, 531], [1338, 535], [1338, 762], [1098, 767]]
color = "red"

fig, ax = plt.subplots(1, 2, figsize=(15, 10), dpi=80)
ax[0].imshow(img)
ax[1].imshow(img)

# Actual points
for point in actual_points:
    patch = Circle((point[0], point[1]), 7, facecolor=color)
    ax[0].add_patch(patch)

# Wanted points
for point in projected_points:
    patch = Circle((point[0], point[1]), 7, facecolor=color)
    ax[1].add_patch(patch)

plt.show()

H = homography_computation(actual_points,projected_points)
print(H)

# have to zoom


img_projected = modify_parse_effect(img, H)

fig, ax = plt.subplots(1, 2, figsize=(15, 10), dpi=80)
ax[0].imshow(img)
ax[1].imshow(img_projected)
plt.show()