# task1
class Matrix:
    def __init__(self,array):
        self.array = array

    def __str__(self):
        return '\n'.join('\t'.join([str(item) for item in line]) for line in self.array)

    def __add__(self, other):
        m = [[int(self.array[line][item]) + int(other.array[line][item]) for item in range(len(self.array[line]))]
             for line in range(len(self.array))]
        return Matrix(m)


m_1 = [[1, 2, 3], [10, 15, 30], [13, 78, 66]]
m_2 = [[10, 24, 36], [19, 13, 37], [10, 18, 76]]
mtr_1 = Matrix(m_1)
mtr_2 = Matrix(m_2)
sum_mtr = mtr_1 + mtr_2
print(sum_mtr)

# task2
from abc import ABC, abstractmethod


class Clothing:
    def __int__(self, param):
        self.param = param

    @property
    @abstractmethod
    def costs(self):
        pass

    def __add__(self, other):
        return self.costs + other.costs


class Coat(Clothing):
    @property
    def costs(self):
        print(f'costs of clothing for coat - {self.param / 6.5 + 0.5}')
        return self.param / 6.5 + 0.5


class Costume(Clothing):
    @property
    def costs(self):
        print(f'costs of clothing for costume - {2 * self.param + 0.3}')
        return self.param * 2 + 0.3


coat = Coat(12)
costume = Costume(35)
print(coat + costume)

