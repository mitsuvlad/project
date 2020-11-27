# task1

from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        return time * rate + bonus
    except ValueError:
        return "Enter 3 numbers"
print(salary())

# task2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[el] for el in range(1,len(my_list)) if my_list[el] > my_list[el-1]]
print(new_list)

# task3

gen_list = [num for num in range(20, 240) if num % 20 == 0 or num % 21 == 0]
print(gen_list)
# task4

task_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq_list = [item for item in task_list if task_list.count(item) == 1]
print(uniq_list)

# task5

from functools import reduce

def multip(int_1, int_2):
    return int_1 * int_2

even_list = [i for i in range(100, 1001, 2)]
print(reduce(multip, even_list))

# task6
from itertools import count, cycle
my_count = count(3)
my_cycle = cycle("ABC")
for _ in range(8):
    print(next(my_count), next(my_cycle))
# task7
def fact(numeric):
    f_num = 1
    if numeric == 0:
        yield 1
    for i in range(1, numeric + 1):
        f_num *= i
        yield f'{i}! = {f_num}'
for el in fact(int(input('Enter factorial'))):
    print(el)