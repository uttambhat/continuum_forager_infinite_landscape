import numpy as np
import matplotlib.pyplot as plt

def plot_trajectory(x_array,t_array,energies):
    energy_colors = (np.max(energies)-energies)/np.max(energies)
    if x_array.shape[1]==1:
        plt.scatter(t_array,x_array[:,0],c=energy_colors,alpha=0.5)
        plt.show()
    elif x_array.shape[1]==2:
        plt.scatter(x_array[:,0],x_array[:,1],c=energy_colors,alpha=0.5)
        plt.show()
    elif x_array.shape[1]==3:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(x_array[:,0],x_array[:,1],x_array[:,2],c=energy_colors,alpha=0.5)
        plt.show()

def plot_trajectory_and_revealed_food_sites(x_array,t_array,energies,revealed_food_sites):
    energy_colors = (np.max(energies)-energies)/np.max(energies)
    if x_array.shape[1]==1:
        plt.scatter(energies,x_array[:,0],c=energy_colors,alpha=0.5)
        plt.show()
    elif x_array.shape[1]==2:
        plt.scatter(revealed_food_sites[:,0],revealed_food_sites[:,1],s=10,alpha=0.5)
        plt.scatter(x_array[:,0],x_array[:,1],c=energy_colors,alpha=0.6)
        plt.show()
    elif x_array.shape[1]==3:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(revealed_food_sites[:,0],revealed_food_sites[:,1],revealed_food_sites[:,2],s=5,alpha=0.5)
        ax.scatter(x_array[:,0],x_array[:,1],x_array[:,2],c=energy_colors,alpha=0.6)
        plt.show()


