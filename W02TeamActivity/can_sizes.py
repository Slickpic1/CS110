#Import Libraries
from numpy import pi

class Can:
    #Initialize class with all our values
    def __init__(self,name,radius,height,cost_per_can):
        self.name = name
        self.radius = radius
        self.height = height
        self.cost_per_can = cost_per_can
        self.volume = self.compute_volume(radius,height)
        self.surface_area = self.compute_surface_area(radius,height)
        self.storage_efficiency = self.compute_storage_efficiency(self.volume,self.surface_area)
        self.cost_efficiency = self.compute_cost_efficiency(self.volume,self.cost_per_can)

    def compute_volume(self,r,h):
        return pi*r*r*h
    
    def compute_surface_area(self,r,h):
        return 2*pi*r*(r+h)

    def compute_storage_efficiency(self,volume,surface_area):
        return volume/surface_area

    def compute_cost_efficiency(self,volume,cost):
        return volume/cost

#Read data from file
def read_file():
    file_data = open("can_data.txt","r")
    return file_data

#Parse through data to convert it to usable classes
def parse_data(file_data):
    #Convert file into classes
    can_list = []
    for line in file_data:
        can_data = line.split(",")   #split into list

        #Split data into different values (could do in one line, but very messy)
        name = str(can_data[0])
        radius = float(can_data[1])
        height = float(can_data[2])
        cost_per_can = float(can_data[3])

        #create new class and add can to list
        can = Can(name,radius,height,cost_per_can)
        can_list.append(can)
    return can_list

def compare_cost_efficiency(can_list):
    #Create list of cost_efficiency
    cost_efficiency = []
    for can in can_list:
        cost_efficiency.append(can.cost_efficiency)

    #Find max in the list and return which one it is
    max_value = max(cost_efficiency)
    return cost_efficiency.index(max_value)

def compare_storage_efficiency(can_list):
    storage_efficiency = []
    for can in can_list:
        storage_efficiency.append(can.storage_efficiency)

    #Find max in list and return index of it
    max_value = max(storage_efficiency)
    return storage_efficiency.index(max_value)

def display_storage_efficiencies(can_list):
    for can in can_list:
        print(f"{can.name}: {can.storage_efficiency:.2f}")

def display_best_values(can_list,best_cost,best_storage):
    #Display best storage
    print(f"The {can_list[best_storage].name} can has the best storage efficiency of {can_list[best_storage].storage_efficiency:.2f}.")
    print(f"The {can_list[best_cost].name} can has the best cost efficiency of {can_list[best_cost].cost_efficiency:.2f}")
    return

def display(can_list,best_cost,best_storage):
    print()   #Print newline
    display_storage_efficiencies(can_list)
    print("\n===========================\n")
    display_best_values(can_list,best_cost,best_storage)
    print()

def main():
    #Get can data from file
    file_data = read_file()

    #Create list of Cans
    can_list = parse_data(file_data)

    #Compare cost per can and efficiency
    best_cost = compare_cost_efficiency(can_list)
    best_storage = compare_storage_efficiency(can_list)

    #Display everything
    display(can_list,best_cost,best_storage)

main()