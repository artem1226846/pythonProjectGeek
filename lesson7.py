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
            for i in range(len(self.matrix)):
                if len(self.matrix) != len(other.matrix):
                    raise MyError('Матрицы различаются по числу строк!')
                for j in range(len(self.matrix[i])):
                    if len(self.matrix[i]) != len(other.matrix[i]):
                        raise MyError('Матрицы различаются по числу столбцов!')
                    self.matrix[i][j] += other.matrix[i][j]
            return Matrix(self.matrix)
        except MyError as mr:
            print(mr)

obj = Matrix([[1,2,3,4],[1,2,3,2],[2,3,2,3]])
obj2 = Matrix([[1,2,3,4],[1,2,3,2],[2,3,2,3]])
print(obj+obj2)