# task 1
import time
class TrafficLight:
    __color = ['red','yellow','green']

    def running(self):
        if self.__color == ['red','yellow','green']:
            while True:
                print(self.__color[0])
                time.sleep(7)
                print(self.__color[1])
                time.sleep(2)
                print(self.__color[2])
                time.sleep(4)
        else:
            print('Error')

a = TrafficLight()
a.running()

# task 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 0.05 / 1000
        print(f'{mass} т')

obj = Road(20, 5000)
obj.calc_mass()

# task 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}')
    def get_total_income(self):
        total_income = self._income['wage']+self._income['bonus']
        print(f'Суммарный доход: {total_income}')

obj = Position('Ivan','Ivanov','developer',10000,2000)
print(obj.name)
print(obj.surname)
print(obj.position)
print(obj._income)
obj.get_full_name()
obj.get_total_income()

# task 4
class Car:
    def __init__(self,speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)

class PoliceCar(Car):
    def __init__(self,speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if not self.is_police:
            print('Это не полицейская машина!')

    def go(self):
        if self.is_police:
            print('Полицейская машина начала погоню')

police = PoliceCar(60, 'red', 'bmw', True)

class TownCar(Car):
    def __init__(self,speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police:
            print('Это полицейская машина!')

    def show_speed(self):
        if not self.is_police:
            if self.speed > 60:
                print('Превышение скорости!')
                police.go()
            else:
                print(self.speed)

class SportCar(Car):
    def __init__(self,speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police:
            print('Это полицейская машина!')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
            police.go()
        else:
            print(self.speed)


car1 = TownCar(70, 'red', 'bmw', False)
car1.go()
car1.turn('направо')
car1.show_speed()
car1.stop()

# task 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

obj1 = Pen('pen')
obj1.draw()

obj2 = Pencil('pencil')
obj2.draw()

obj3 = Handle('handle')
obj3.draw()


