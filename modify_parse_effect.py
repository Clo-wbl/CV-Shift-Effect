import numpy as np

def modify_parse_effect(img, H):
    img = np.array(img)
    height, width, channels = img.shape
    img_projected = np.zeros_like(img)

    zm = 0.5
    Z = [[zm, 0, 0], [0, zm, 0], [0, 0, zm]]

    for y in range(height):
        for x in range(width):
            coord_image_before = np.array([x, y, 1])
            coord_image_after = np.dot(H, coord_image_before)
            coord_image_after /= coord_image_after[2]

            xp, yp = int(coord_image_after[0]), int(coord_image_after[1])
            if 0 <= xp < width and 0 <= yp < height:
                img_projected[yp, xp] = img[y, x]

    return img_projected
