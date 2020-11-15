#task1
count = input ("Введите количество ")
print (f"Вы ввели, {count}")
# task2
import datetime
time = int(input ("Введите время в секундах "))
print (datetime.timedelta(seconds=time))
# task3
number = int(input ("Введите число "))
number_sum = (number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number)))
print (number_sum)
# task4
n = int(input("Введите положительное целое число "))
max_n = 0
while n > 0:
    s = n % 10
    if s >= max_n:
        max_n = s
    n //= 10
print (max_n)
# task 5
proceeds = float(input("Введите значение выручки "))
costs = float(input("Введите значение издержек "))
if proceeds > costs:
    profit = (proceeds - costs)
    profitability = (proceeds - costs) / costs
    print (f"Фирма работает в прибыль. Рентабельность фирмы - {profitability:.2%}")
    numbers = int(input("Введите численность фирмы "))
    profit_on_employment = profit / numbers
    print(f"Прибыль на работника - {profit_on_employment:.2f}")
else:
    print ("Фирма работает в убыток")
# task 6
a = float(input("Введите результат первого дня "))
b = float(input("Введите желаемый результат "))
count_days = 1
sum_km = a
while sum_km < b:
    a *= 1.1
    count_days += 1
    sum_km = sum_km + a
print (f"Вы достигнете результата на - {count_days:.0f} день")
