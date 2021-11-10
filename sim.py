import numpy as np
import matplotlib.pyplot as plt
from forager import *
from resource_map import *
from plotter import *

D = 1
food_density = 1.
L_range = range(21)
intercept = 0.01
for slope in np.round(np.arange(0.01,0.11,0.01),2):
    lifetimes = []
    for L in L_range:
        metabolic_rate = intercept+slope*L
        lifetimes_L = []
        for config in range(100):
            foragerA = forager(detection_range=L,metabolic_rate=metabolic_rate,dimension=D,step_size=0.1)
            mapA = resource_map(D,mesh_size=L,food_density=food_density)
            
            x_array = []
            t_array = []
            e_array = []
            
            while foragerA.alive:
                foragerA.go_to_nearest_food_and_consume(mapA)
                x_array.append(np.copy(foragerA.position))
                t_array.append(foragerA.lifetime)
                e_array.append(foragerA.energy)
            
            x_array = np.array(x_array)
            t_array = np.array(t_array)
            e_array = np.array(e_array)
            lifetimes_L.append(foragerA.lifetime)
            print(slope,L,np.round(metabolic_rate,3),config,foragerA.lifetime)
        
        lifetimes.append(lifetimes_L)
    lifetimes = np.array(lifetimes)
    np.save("/home/uttam/Dropbox/c/smart_forager/continuum_forager/results/D="+str(D)+"/lifetimes_L"+str(min(L_range))+"-"+str(max(L_range))+"_metabolism_slope="+str(slope).replace(".","p")+"_intercept_"+str(intercept).replace(".","p")+".npy",lifetimes)


