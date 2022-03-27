from eletric_car import ElectricCar as  E
my_car = E('LynkCo','06','2021')
my_car.describe()
# Hi, the electric car is LynkCo-06-2021, 0 KM
my_car.battery.describe_battery()
# The battery capacity is 70 kWH