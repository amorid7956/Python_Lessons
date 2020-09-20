first_matrix = [[31, 22], [37, 43], [51, 86]]
add_matrix = [[13, 4], [8, 25], [1, 18]]

second_matrix = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
third_matrix = [[3, 5, 8, 3], [8, 3, 7, 1]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for line in self.matrix:
            for el in line:
                s += str(el) + ' '
            s += '\n'
        return s

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.matrix)):
            temp_line = []
            for j in range(len(self.matrix[i])):
                temp_line.append(self.matrix[i][j] + other.matrix[i][j])
            result_matrix.append(temp_line)
        return Matrix(result_matrix)


m = Matrix(third_matrix)
print(m)
# Складывать и вычитать можно матрицы только одинакового размера.
a = Matrix(first_matrix)
b = Matrix(add_matrix)
sum = a + b
print(sum)  # результат сложения двух матриц
