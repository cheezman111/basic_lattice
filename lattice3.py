import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

#-----------------------------------------------------
#---- Create Lattice Vectors -------------------------
#-----------------------------------------------------
a = 1.5
b = 4

a1 = np.array((a,0,0))
a2 = np.array((np.sqrt(3)/2*a, 1/2*a, 0))
a3 = np.array((0,0,b))


#-----------------------------------------------------
#---- Create Points ----------------------------------
#-----------------------------------------------------


# Set the size of the lattice.
size = 4

lattice_points = []
for x in range(size):
    for y in range(size):
        for z in range(size):
            point = x*a1 + y*a2 + z*a3
            lattice_points.append(point)


#-----------------------------------------------------
#---- Plot Graph -------------------------------------
#-----------------------------------------------------
plot_graph = True

if plot_graph:
    x_list = []
    y_list = []
    z_list = []
    for position in lattice_points:
        # Extract coordinates from the position tuple.
        x, y, z = tuple(position)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)

    # Set up 3d scatter plot.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d', proj_type='ortho')
    ax.scatter(x_list, y_list, z_list)

    # Display scatter plot.
    fig.show()

