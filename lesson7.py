# task 1
class MyError(Exception):
    def __init__(self, text):
        self.txt = text

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        mat = ''
        for i in self.matrix:
            mat = mat + f'{i}'[1:-1].replace(',','') + '\n'
        return mat[:-1]

    def __add__(self, other):
        try:
            x = []
            for i in range(len(self.matrix)):
                if len(self.matrix) != len(other.matrix):
                    raise MyError('Матрицы различаются по числу строк!')
                y = []
                for j in range(len(self.matrix[i])):
                    if len(self.matrix[i]) != len(other.matrix[i]):
                        raise MyError('Матрицы различаются по числу столбцов!')
                    y.append(self.matrix[i][j] + other.matrix[i][j])
                x.append(y)
            return Matrix(x)
        except MyError as mr:
            print(mr)


obj = Matrix([[1,2,3,4],[1,2,3,2],[2,3,2,3]])
obj2 = Matrix([[1,2,3,4],[1,2,3,2],[2,3,2,3]])
print(obj+obj2)

# task 2
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def fab_cons(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fab_cons(self):
        return round(self.size / 6.5 + 0.5, 2)

class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def fab_cons(self):
        return round(self.height * 2 + 0.3, 2)

a = Coat(int(input('Укажите размер для пальто: ')))
b = Costume(int(input('Укажите рост для костюма: ')))
print('Общий расход ткани = ', a.fab_cons + b.fab_cons, end='')

# task 3
class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f'Клетка с количеством ячеек равным {self.cells}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        x = self.cells - other.cells
        if x == 0:
            return 'Клетки одинакового размера'
        else:
            return Cell(abs(x))

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        x = max(self.cells, other.cells)
        y = min(self.cells, other.cells)
        return Cell(x // y)

    def make_order(self, cells):
        x = self.cells % cells
        y = self.cells // cells
        if x == 0:
            return ('*' * cells + '\n') * y
        else:
            return ('*' * cells + '\n') * y + '*' * x

