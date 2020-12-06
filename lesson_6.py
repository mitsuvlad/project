# task1

import itertools
import time
class TrafficLight:
    __colors = [["red", 7], ["yellow", 2], ["green", 5]]
    def running(self):
        for light in itertools.cycle(self.__colors):
            print(f'{light[0]}')
            time.sleep(light[1])
trafficLight_1 = TrafficLight()
trafficLight_1.running()

# task2

class Road:
    __length = 5000
    __width = 20
    def __init__(self, weight, thickness):
        self.weight = weight
        self.thickness = thickness
    def calc(self):
        return f'{Road.__length}м * {Road.__width}м * {self.weight}кг * {self.thickness}см = ' \
               f'{round(Road.__length * Road.__width * 10 * 5 / 1000)} тонн'

a = Road(10, 5)
print(a.calc())

# task3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self. surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return f'{sum(self.__income.values())}'

empl = Position("Ivan", "Petrov", "manager", 50000, 10000)
print(f'{empl.get_full_name()}, {empl.position}, income - {empl.get_total_income()} ')

# task4
import random
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print (f'car - {self.name}, color - {self.color}, is_police - {self.is_police}')

    def go(self):
        return f'{self.name} go!'

    def stop(self):
        return f'{self.name} stoped!'
    def turn(self, direction=random.choice(["right", "left"])):
        self.direction = direction
        return f'{self.name} turn on {self.direction}'
    def show_speed(self):
        return f'{self.name} - {self.speed}km/h'
class TownCar(Car):

    def show_speed(self):
        return f'{self.name} speed - {self.speed} Over speed!' \
            if self.speed > 60 else f'{self.name} speed - {self.speed}'

class WorkCar(Car):

    def show_speed(self):
        return f'{self.name} speed - {self.speed} Over speed!' \
            if self.speed > 40 else f'{self.name} speed - {self.speed}'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(50, 'red', 'volvo')
print(town_car.go())
print (town_car.turn())
print (town_car.show_speed())
print (town_car.stop())

work_car = WorkCar(70, 'green', 'mustang')
print(work_car.go())
print (work_car.turn())
print (work_car.show_speed())
print (work_car.stop())

police_car = PoliceCar(90, 'blue', 'ford')
print(police_car.go())
print (police_car.turn())
print (police_car.show_speed())
print (police_car.stop())

# task5

