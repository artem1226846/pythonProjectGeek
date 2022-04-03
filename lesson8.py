# task 1
class Data:
    def __init__(self, data):
        self.data = data
        print(Data.validate(self.data))

    @classmethod
    def get_data(cls, data):
        try:
            data = list(map(int,data.split(sep='-')))
            return cls(data)
        except ValueError:
            print('data is invalid')

    @staticmethod
    def validate(data):
        if data[1] in [1,3,5,7,8,10,12] and data[0] <= 31 and 1000 < data[2] < 2100:
            return 'data is valid'
        elif data[1] in [4,6,9,11] and data[0] <= 30 and 1000 < data[2] < 2100:
            return 'data is valid'
        elif data[1] == 2 and data[0] <= 29 and 1000 < data[2] < 2100:
            return 'data is valid'
        else:
            return 'data is invalid'


Data.get_data('01-12-2022')
Data.get_data('01-22-2022')

# task 2
class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise DivZero('Деление на ноль невозможно')
    else:
        res = a / b
        print('Частное: ', res)
except DivZero as dz:
    print(dz)

# task 3
class IsNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

numbers = []

while True:
    try:
        a = input('Введите число (чтобы завершить программу введите "stop"): ')
        if a[0] in list(map(str, range(10))):
            numbers.append(int(a))
        elif a == 'stop':
            break
        else:
            raise IsNumber('Необходимо ввести число')
    except IsNumber as inu:
        print(inu)
print(numbers)

# task 4-6
class Lab:
    """
    проект "научно-исследовательская лаборатория
    """

    name = 'Laboratory of pharmacology'
    money = 0
    resources = {'животные':0, 'расходный материал':0}
    papers = 0
    experiments = 0
    def get_funding(self, amount):
        print(f'Лаборатория получила финансирование в размере {amount} рублей')
        self.money += amount

    planned_exp = 0

my_lab = Lab()

class Staff(Lab):
    salary = 0
    def __init__(self,name, age, work_exp, at_work = False):
        self.name = name
        self.age = age
        self.work_experience = work_exp
        self.at_work = at_work

    def get_salary(self):
        try:
            if self.salary > my_lab.money:
                raise NoMoney('Недостаточно средств для выплаты зарплаты')
            my_lab.money -= self.salary
        except NoMoney as nm:
            print(nm)

class Head(Staff):
    def __init__(self, name, age, work_exp, publ, degree, is_acad = False):
        super().__init__(name, age, work_exp)
        self.publications = publ
        self.degree = degree
        self.is_academic = is_acad
        self.salary = 60000 if self.is_academic else 50000

    @staticmethod
    def buy_res(name, number):
        prices = {'животные':100, 'расходный материал':20}
        price = prices[name]
        try:
            if price * number > my_lab.money:
                raise NoMoney('Недостаточно средств для покупки')
            my_lab.resources[name] += number
            my_lab.money -= price*number
        except NoMoney as nm:
            print(nm)
        except KeyError:
            print('неподходящий товар')

    @staticmethod
    def plane_exp():
        my_lab.planned_exp = (my_lab.money - my_lab.money/2) // 2100

    def make_report(self):
        print(f'Отчет: число выполненных эксперимнтов = {my_lab.experiments}, число опубликованных работ = {my_lab.papers}')
        self.get_salary()

class Researcher(Staff):
    salary = 30000
    def __init__(self,name, age, work_exp, publ, degree):
        super().__init__(name, age, work_exp)
        self.publications = publ
        self.degree = degree

    @staticmethod
    def make_exp():
            if my_lab.resources['расходный материал'] >= 5 and my_lab.resources['животные'] >= 20:
                my_lab.resources['расходный материал'] -= 5
                my_lab.resources['животные'] -= 20
                my_lab.experiments += 1

            else:
                raise NoMoney('недостаточно материалов для эксперимента')

    def make_paper(self):
        self.get_salary()
        self.publications +=1
        head.publications +=1
        my_lab.papers += 1

class NoMoney(Exception):
    def __init__(self, txt):
        self.txt = txt


my_lab.get_funding(float(input('введите размер гранта: ')))
head = Head('Ivan Ivanov', 24,2,2,'PhD')
researcher = Researcher('Artem',25,2,2,'no')

n = 0
while n != 2:
    head.buy_res(input('введите название товара: '),
                 float(input('введите количество: ')))
    n +=1
x = 0
head.plane_exp()
while x <= my_lab.planned_exp:
    try:
        researcher.make_exp()
        researcher.make_paper()
    except NoMoney:
        break

head.make_report()


# task 7
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 0:
            return self.a
        elif self.b < 0:
            if self.b == -1:
                return f'{self.a} - i'
            return f'{self.a} - {-self.b}i'
        return f'{self.a} + {self.b}i' if self.b != 1 else f'{self.a} + i'

    def __add__(self, other):
        return ComplexNumber(self.a+other.a, self.b+other.b)

    def __mul__(self, other):
        x1 = self.a * other.a - self.b * other.b
        x2 = self.a * other.b + self.b * other.a

        return ComplexNumber(x1, x2)

num1 = ComplexNumber(2,3)
num2 = ComplexNumber(-1,1)
print(num1+num2)
print(num1*num2)