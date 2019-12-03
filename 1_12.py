import numpy as np

class fuel_calculator(object):
    def __init__(self, module_weight):
        self.total = 0
        self.calculate(module_weight)

    def calculate(self, weight):
        added_fuel_weight = np.floor_divide(weight, 3) - 2
        if added_fuel_weight > 0:
            self.total += added_fuel_weight
            self.calculate(added_fuel_weight)
        else:
            return self.total

def get_fuel(weight):
    return np.floor_divide(weight, 3) - 2

if __name__ == '__main__':
    with open("D:/tmp/input.txt", "r") as f:
        raw_data = f.readlines()
    data = [int(x.replace("\n","")) for x in raw_data]
    fuels = [fuel_calculator(x) for x in data]
    #a = fuel_calculator(1969)
    print(sum([x.total for x in fuels]))

