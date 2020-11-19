# task1
my_list = [1, "строка", [list]]
for el in my_list:
    print(type(el))
# task2
user_list = list(input('Введите значения списка'))
i = 0
for i in range(1, len(user_list), 2):
    user_list[i-1], user_list[i] = user_list[i], user_list[i-1]
print(user_list)
# task3
month = int(input('Введите месяц в виде целого числа от 1 до 12'))
seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
print(f'По словарю это - {seasons_dict[month//3]}\nПо списку это - {seasons_list[month/3]}')
# task4
string = input("Введите строку из нескольких слов, разделённых пробелами").split()
for i, word in enumerate(string,1):
    print (f'{i} {word[:10]}')
# task5
numbers_list = [8, 5, 5, 4, 2, 1]
number = int(input("Введите натуральное число"))
i = 0
for n in numbers_list:
    if number <= n:
        i += 1
numbers_list.insert(i, number)
print(numbers_list)
# task6
goods = []
features = {'name': '', 'price': '', 'count': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'count': [], 'unit': []}
num = 0
while True:
    if input("Нажмите 'Q' что бы завершить программу, либо 'Enter' что бы продолжить"):
        break
    num += 1
    for f in features.keys():
        pro = input(f'Введите значение свойства {f}')
        features[f] = int(pro) if (f == 'price' or f == 'count') else pro
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f"Структура товаров {goods}")
    print(f"Текущая аналитика {'-'*30}")
    for key, value in analytics.items():
        print(f'{key}:{value}')







