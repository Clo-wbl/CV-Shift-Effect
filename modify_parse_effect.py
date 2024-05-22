import numpy as np

def modify_parse_effect(img, H):
    img = np.array(img)
    height, width, channels = img.shape
    img_projected = np.zeros_like(img)

    for y in range(height):
        for x in range(width):
            coord_image_before = np.array([x, y, 1])
            coord_image_after = np.dot(H, coord_image_before)
            coord_image_after /= coord_image_after[2]

            xp, yp = int(coord_image_after[0]), int(coord_image_after[1])
            if 0 <= xp < width and 0 <= yp < height:
                img_projected[yp, xp] = img[y, x]

    # return img_projected

# import numpy as np

# def modify_parse_effect(img, H):
#     img = np.array(img)
#     height, width, channels = img.shape
#     img_projected = np.zeros_like(img)

#     # Déterminer les coins de l'image projetée transformée
#     corners = np.array([[0, 0, 1], [0, height - 1, 1], [width - 1, 0, 1], [width - 1, height - 1, 1]])
#     transformed_corners = np.dot(H, corners.T).T
#     transformed_corners /= transformed_corners[:, 2, np.newaxis]

#     # Trouver les dimensions de l'image projetée
#     min_x = int(np.floor(np.min(transformed_corners[:, 0])))
#     max_x = int(np.ceil(np.max(transformed_corners[:, 0])))
#     min_y = int(np.floor(np.min(transformed_corners[:, 1])))
#     max_y = int(np.ceil(np.max(transformed_corners[:, 1])))
#     projected_height = max_y - min_y + 1
#     projected_width = max_x - min_x + 1

#     # Créer une image projetée redimensionnée
#     projected_img_resized = np.zeros((projected_height, projected_width, channels), dtype=img.dtype)

#     # Appliquer la transformation inverse pour remplir l'image projetée redimensionnée
#     H_inv = np.linalg.inv(H)
#     for y in range(projected_height):
#         for x in range(projected_width):
#             coord_image_after = np.array([x + min_x, y + min_y, 1])
#             coord_image_before = np.dot(H_inv, coord_image_after)
#             coord_image_before /= coord_image_before[2]
#             xp, yp = int(coord_image_before[0]), int(coord_image_before[1])
#             if 0 <= xp < width and 0 <= yp < height:
#                 projected_img_resized[y, x] = img[yp, xp]

#     return projected_img_resized