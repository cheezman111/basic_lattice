import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

#-----------------------------------------------------
#---- Create Graph -----------------------------------
#-----------------------------------------------------

# Create an empty networkx graph.
lattice = nx.Graph()

# Set the size of the lattice.
size = 4

# Iterate each coordinate from 0 to 'size'. For every combination add a node 
# with an attribute containing a tuple of the coordinates labeled as 'position'.
node_count = 0
for x in range(size):
    for y in range(size):
        for z in range(size):
             lattice.add_node(node_count, position=(x,y,z))
             node_count += 1


#-----------------------------------------------------
#---- Plot Graph -------------------------------------
#-----------------------------------------------------

# Create empty lists to add position values. Matplotlib takes separate lists.
x_list = []
y_list = []
z_list = []
# Extract positions attributes from graph. nx will return a dictionary.
positions_dictionary = nx.get_node_attributes(lattice, 'position')
# Iterate through the keys in the dictionary to access the positions.
for position in positions_dictionary.values():
    # Extract coordinates from the position tuple.
    x, y, z = position
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)

# Set up 3d scatter plot.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', proj_type='ortho')
ax.scatter(x_list, y_list, z_list)

# Display scatter plot.
fig.show()

