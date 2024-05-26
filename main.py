import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Circle
from homography_computation import homography_computation
from modify_parse_effect import modify_parse_effect

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

# Computing Homography
H = homography_computation(actual_points,projected_points)
print("Homography matrix : \n")
print(H)

img_projected = modify_parse_effect(img, H)

# Try to zoom into the image ; doesn't work - in case you see what is wrong,
# I would be glad that you enlighten me on this subject
# zm = 2
# Z = [[zm, 0, 0], [0, zm, 0], [0, 0, 1]]

# height, width, channels = img_projected.shape

# for y in range(height):
#     for x in range(width):
#         coord_zoom = np.dot(Z,np.array([x, y, 1]))
#         xx, yy = int(coord_zoom[0]), int(coord_zoom[1])
#         if 0 <= xx < width and 0 <= yy < height:
#             img_projected[yy,xx]=img_projected[y,x]


fig, ax = plt.subplots(1, 2, figsize=(15, 10), dpi=80)
ax[0].imshow(img)
ax[1].imshow(img_projected)
plt.show()

# Comments : the building's roof is now parallel to the horizontal axis
# Transformation worked and homography matrix is relevant