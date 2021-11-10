import numpy as np
import matplotlib.pyplot as plt
from resource_map import *
from forager import *

D = 2
lengthscale = 1.
m = resource_map(D,mesh_size=lengthscale)
_ = m.reveal_and_fill_food_sites((0,0),3)
_ = m.reveal_and_fill_food_sites((10,10),3)

cells = m.show_all_revealed_cells()
x = m.show_all_food_in_revealed_cells()

"""
# test if the cells and food sites are in the same regions
plt.scatter(cells[:,0],cells[:,1])
plt.show()
plt.scatter(x[:,0],x[:,1])
plt.show()

# test if every food site's round value corresponds to the cell_id
for key in m.resource_mesh.keys():
    if len(m.resource_mesh[key])>0:
        print(key,np.all(np.floor(np.array(list(m.resource_mesh[key])))==np.array(key).reshape(1,-1)))

"""
f = forager(detection_range=lengthscale,metabolic_rate=1.,dimension=D)
f.nearest_food(m)

