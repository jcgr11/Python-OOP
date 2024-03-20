class VehiclePark:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f'{vehicle}\nThis vehicle has been added.\n')

    def remove_vehicle(self, id):
        for vehicle in self.vehicles:
            if vehicle.id == id:
                self.vehicles.remove(vehicle)
                return print(f'\nYou removed \n{vehicle}\n')

    def search_vehicle(self, id):
        for vehicle in self.vehicles:
            if vehicle.id == id:
                return print(f'\nYou searched for\n{vehicle}\n')

    def list_vehicles(self):
        print('Current Inventory')
        for vehicle in self.vehicles:
            print(vehicle)
            print('#' * 20)