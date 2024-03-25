from VehiclePark import VehiclePark
from Car import Car
from Bicycle import Bicycle
from GolfCart import GolfCart
from Motorcycle import Motorcycle

park = VehiclePark()
park.add_vehicle(Bicycle("sd20", "Schwin", "Discover", "2020"))
park.add_vehicle(Motorcycle("kn21", "Kawasaki", "Ninja", "2021"))
park.add_vehicle(Motorcycle("hgw19", "Honda", "Gold Wing", "2019"))
park.add_vehicle(GolfCart("eegw23", "E-Z-GO", "Express S4", "2023"))
park.add_vehicle(GolfCart("ccv15", "Club Car", "Villager 2", "2015"))
park.add_vehicle(Car("tc21", "Toyota", "Corolla", "2021"))

park.list_vehicles()
park.remove_vehicle("eegw23")
park.search_vehicle("ccv15")
park.list_vehicles()
