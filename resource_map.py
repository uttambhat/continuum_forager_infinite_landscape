import numpy as np

class resource_map:
    def __init__(self,dimension,food_value=1.,food_density=1.,mesh_size=1.):
        self.dimension = dimension
        self.food_value = food_value
        self.food_density = food_density
        self.mesh_size = mesh_size
        self.mean_food_sites_per_cell = self.food_density*self.mesh_size
        self.resource_mesh = {}
    
    def fill_mesh_cell(self,cell_id):
        if cell_id in self.resource_mesh.keys():
            return 0
        else:
            n = np.random.poisson(self.mean_food_sites_per_cell)
            locations = np.random.uniform(0.,self.mesh_size,(n,self.dimension)) + self.mesh_size*np.array(cell_id).reshape(1,-1)
            locations_tuple = [tuple(x) for x in locations]
            self.resource_mesh[cell_id] = dict(zip(locations_tuple,np.ones(n)))
            return 1
    
    def convert_to_base(self,n,base):
        if n<np.power(base,self.dimension):
            result = np.zeros(self.dimension)
            place = 0
            while n>0:
                result[place] = n%base
                n = (n-result[place])/base
                place += 1
            return result.astype(int)
        else:
            raise Exception("n should be less than base^(dimension)!")
    
    def neighborhood_fill(self,cell_id,integer_distance):
        total_cells = np.power(2*integer_distance+1,self.dimension)
        result = []
        for i in range(total_cells):
            cell = tuple((self.convert_to_base(i,2*integer_distance+1)-integer_distance) + cell_id)
            result.append(cell)
            if not cell in self.resource_mesh.keys():
                self.fill_mesh_cell(cell)
        return result
    
    def reveal_and_fill_food_sites(self,cell_id,integer_distance=0):
        result = []
        neighboring_cell_ids = self.neighborhood_fill(cell_id,integer_distance)
        for cell in neighboring_cell_ids:
            result += list(self.resource_mesh[cell].keys())
        return np.array(result)
    
    def show_all_revealed_cells(self):
        return np.array(list(self.resource_mesh.keys()))
    
    def show_all_food_in_revealed_cells(self):
        result = []
        for key in self.resource_mesh.keys():
            result += list(self.resource_mesh[key].keys())
        return np.array(result)
