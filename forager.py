import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from resource_map import *

class forager:
    def __init__(self,detection_range,metabolic_rate,dimension,velocity=1.,step_size=0.01,max_energy=1.,initial_position=None):
        self.detection_range = detection_range
        self.metabolic_rate = metabolic_rate
        self.dimension = dimension
        self.velocity = velocity
        self.step_size = step_size
        self.step_time = self.step_size/self.velocity
        self.metabolism_per_step = self.metabolic_rate*self.step_time
        self.max_energy = max_energy
        self.energy = self.max_energy
        self.alive = True
        self.lifetime = 0.
        if initial_position==None:
            self.position = np.zeros(self.dimension)
    
    def random_step(self):
        if self.alive:
            self.position += np.random.normal(0.,self.step_size,self.dimension)
            self.energy -= self.metabolism_per_step
            self.lifetime += self.step_time
            if self.energy<=0.:
                self.alive = False
        #return self.position
    
    def consume(self,mapA,food_position):
        if self.alive:
            cell_id = tuple(np.floor(food_position/mapA.mesh_size))
            if tuple(food_position) in mapA.resource_mesh[cell_id].keys():
                del mapA.resource_mesh[cell_id][tuple(food_position)]
                self.energy = min(self.energy+mapA.food_value,self.max_energy)
        #return self.energy
    
    def nearest_food(self,mapA):
        if np.isclose(mapA.mesh_size,self.detection_range):
            cell_id = tuple(np.floor(self.position/mapA.mesh_size))
            nearby_food_sites = mapA.reveal_and_fill_food_sites(cell_id,integer_distance=1)
            if len(nearby_food_sites)>0:
                distances = cdist(nearby_food_sites,self.position.reshape(1,-1))
                nearest_food_index = np.argmin(distances)
                nearest_food_position,nearest_food_distance = nearby_food_sites[nearest_food_index],distances[nearest_food_index,0]
                return nearest_food_position,nearest_food_distance
            else:
                return np.ones(self.dimension)*np.inf,np.inf
    
    def go_to_nearest_food_and_consume(self,mapA):
        nearest_food_position,nearest_food_distance = self.nearest_food(mapA)
        if nearest_food_distance<self.detection_range:
            self.position = nearest_food_position
            travel_time = nearest_food_distance/self.velocity
            self.lifetime += travel_time
            self.energy -= travel_time*self.metabolic_rate
            if self.energy<0.:
                self.lifetime -= (-self.energy/self.metabolic_rate)
                self.alive=False
            if self.alive: #in case it was never alive can't use just else
                self.consume(mapA,nearest_food_position)
        else:
            self.random_step()
        #return self.position,self.energy
             

