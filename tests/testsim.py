import numpy as np
import matplotlib.pyplot as plt
from forager import *
from resource_map import *
from plotter import *

D = 1

metabolic_rate = 0.01
L=2.
food_density=2.
foragerA = forager(detection_range=L,metabolic_rate=metabolic_rate,dimension=D)
mapA = resource_map(D,mesh_size=L,food_density=food_density)

x_array = [np.copy(foragerA.position)]
t_array = [foragerA.lifetime]
e_array = [foragerA.energy]

while foragerA.alive:
    foragerA.go_to_nearest_food_and_consume(mapA)
    x_array.append(np.copy(foragerA.position))
    t_array.append(foragerA.lifetime)
    e_array.append(foragerA.energy)

x_array = np.array(x_array)
t_array = np.array(t_array)
e_array = np.array(e_array)
revealed_food_sites = mapA.show_all_food_in_revealed_cells()
#plot_trajectory_and_revealed_food_sites(x_array,t_array,e_array,revealed_food_sites)
plot_trajectory(x_array,t_array,e_array)

