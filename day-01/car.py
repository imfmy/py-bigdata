class Car:
    """汽车类"""

    def __init__(self, name, series, year):
        '''初始化汽车'''
        self.name = name
        self.series = series
        self.year = year
        self.odometer = 0

    def describe(self):
        '''打印出描述车的信息'''
        print(f'Hi, the car is {self.name}-{self.series}-'
              f'{self.year}, {self.odometer} KM')

    def get_odometer(self):
        """打印车的里程数"""
        return self.odometer

    def add_odometer(self, meters=100):
        """增加里程数"""
        self.odometer = self.odometer + meters


