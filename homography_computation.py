import numpy as np

def homography_computation(points_before, points_after):
    # A = []
    # for i in range(len(points_before)):
    #     x, y, z = points_before[i][0], points_before[i][1], 1
    #     xp, yp, zp = points_after[i][0], points_after[i][1], 1
    #     A.append([xp, yp, zp, 1, 0, 0, 0, 0, -xp * x, -x * yp, -zp * x])
    #     A.append([0, 0, 0, xp, yp, zp, 1, -y * xp, -yp * y, -zp * y])

    # A = np.array(A)
    # U, S, V = np.linalg.svd(A)
    # H = V[-1].reshape(3, 3)
    # return H / H[-1, -1]

    # assert points_before.shape == points_after.shape, "Shape does not match"
    # num_points = points_before.shape[0]

    x, y, z = points_before[0], points_before[1], 1
    xp, yp, zp = points_after[0], points_after[1], 1

    A = []
    for i in range(len(points_before)):
        x, y, z = points_before[i][0], points_before[i][1], 1
        xp, yp, zp = points_after[i][0], points_after[i][1], 1
        A.append(np.array([
        [0, 0, 0, -zp*x, -zp*y, -zp*z, yp*x, yp*y, yp*z],
        [zp*x, zp*y, zp*z, 0, 0, 0, -xp*x, -xp*y, -xp*z]
    ]))
    
    A = np.concatenate(A, axis=0)

    U, S, V = np.linalg.svd(A, full_matrices=True)
    
    # H -> V's last column
    H = V[-1].reshape((3,3))
    return H/H[2,2]