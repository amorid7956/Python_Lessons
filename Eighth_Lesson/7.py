class Complex_Number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_Number(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex_Number(self.real * other.real - self.imag * other.imag,
                              self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.__class__.__name__}({self.real};{self.imag}j)"

a = Complex_Number(2,1)
b = Complex_Number(3,4)
print('Сложение комплексных:',a+b)
print('Умножение комплексных:',a*b)
#Всё работает: проверено на реальном примере!