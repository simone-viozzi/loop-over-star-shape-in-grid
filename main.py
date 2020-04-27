
import numpy as np


def index_generator(grid_dim):
    center = grid_dim//2
    dx = center + 1
    sx = center

    while(dx > 0 and sx < grid_dim):
        dx -= 1
        sx += 1
        yield range(dx, sx)

    while(dx <= (center) and sx >= (center + 1)):
        dx += 1
        sx -= 1
        yield range(dx, sx)


grid_dim = 7

A = np.zeros((grid_dim, grid_dim))

for r, i in zip(index_generator(grid_dim), range(grid_dim)):
    for j in r:
        A[i, j] = 1

print(A)
