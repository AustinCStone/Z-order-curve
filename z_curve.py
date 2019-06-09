
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


N_BITS = 3

def z_point(pt):
    all_coords = []
    for coord in pt:
        all_coords.append(('{0:0' + str(N_BITS) + 'b}').format(coord))
    z_str = []
    for bin_coords in zip(*all_coords):
        for coord in bin_coords:
            z_str.append(coord)
    return int(''.join(z_str), 2)

z_pt_to_xy = {}

for x in range(2**N_BITS):
    for y in range(2**N_BITS):
        for z in range(2**N_BITS):
            z_pt = z_point((x, y, z))
            z_pt_to_xy[z_pt] = (x, y, z)

sorted_z_pts = sorted(z_pt_to_xy.keys())
all_x = []
all_y = []
all_z = []
for z_pt in sorted_z_pts:
    x, y, z = z_pt_to_xy[z_pt]
    all_x.append(x); all_y.append(y); all_z.append(z)

ax = plt.axes(projection='3d')
ax.plot3D(all_x, all_y, all_z, 'gray')
plt.show()


