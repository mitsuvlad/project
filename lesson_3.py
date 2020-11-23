# Task1
def my_func():
    arg_1 = float(input("Введите делимое"))
    arg_2 = float(input("Введите делитель"))
    try:
        return arg_1/arg_2
    except ZeroDivisionError:
        print("Деление на ноль!")

print(my_func())
# Task2
def users_data (**kwargs):
    return ','.join(kwargs.values())

print (users_data(name = input("Enter your name:"), surname = input("Enter your surname:"), birthday = input("Enter your birthday:"),
                  city = input("Enter your city:"), email = input("Enter your email:"), phone = input("Enter your phone:")))
# task3
def my_function(number_1, number_2, number_3):
    return sum(sorted([number_1, number_2, number_3])[1:])

print(my_function(5, 7, 6))
# task4
def exponention(x,y):
    try:
        result = x ** y
    except TypeError:
        return "enter a float number"
    return result

print(exponention(5, -1))
# task5
def sum_numbers():
    sum = 0
    while True:
        list = input('Enter a number or "q" to exit').split()
        for number in list:
            if number == "q":
                return sum
            else:
                try:
                    sum += int(number)
                except ValueError:
                    print("to exit from program type 'q'")
        print(f'sum_numbers = {sum}')
print(sum_numbers())
# task6
def int_func():
    for word in input('enter words with space').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if  chars == len(word) else f'{word} only small letters')

int_func()


