from car import Car


class Battery:
    """定义一个电池类"""

    def __init__(self, capacity=70):
        """初始化电池属性"""
        self.capacity = capacity

    def describe_battery(self):
        print(f'The battery capacity is {self.capacity} kWH')


class ElectricCar(Car):
    """电动汽车继承汽车类"""

    def __init__(self, name, series, year):
        """初始化父类属性"""
        super().__init__(name, series, year)
        """子类特有的属性"""
        self.battery = Battery()

    def describe(self):
        '''打印出描述电动汽车的信息'''
        print(f'Hi, the electric car is {self.name}-{self.series}-'
              f'{self.year}, {self.odometer} KM')

