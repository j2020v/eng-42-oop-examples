from vehicle_functions import *
from bike_functions import *


# my_car = Vehicle('LEP195', 'blue', 4)
# print(my_car.number_plate)
# print(my_car.color)
# print(my_car.accelarate())
# print(my_car.doors)
# print(my_car.play_music())

print('--------------------------------')

my_car2 = Vehicle('BMW', 'SW5123', 'green', 2)
print(my_car2.model)
print(my_car2.color)
print(my_car2.doors)
print(my_car2.accelarate())
print(my_car2.brk())

print('--------------------------------')

my_bike = Vehicle('Dutch bike', 'green')
print(my_bike.model)
print(my_bike.play_music())
print(my_bike.turn())


