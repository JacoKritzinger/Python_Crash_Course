import battery
from car import Car as C
from electric_car import ElectricCar as EC

my_tesla = EC('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_nissan = C('nissan','gtr',2020)
# my_nissan.read_odometer()

print(my_tesla)
print(my_tesla.get_descriptive_name())
print(my_nissan.get_descriptive_name())