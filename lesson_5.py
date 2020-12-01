# task1

with open('task_1.txt', 'w', encoding='utf-8') as task_1:
    while True:
        data = input("Enter a data")
        if data == "":
            break
        task_1.write(f"{data}\n")
# task2

with open('my_file.txt', 'r', encoding='utf-8') as task_2:
    result = [f'{line} {" ".join(count.split())} - {len(count.split())} words ' for line, count in enumerate(task_2, 1)]
    print(*result, f"Total lines - {len(result)}", sep='\n')
# task3

with open('salary.txt', 'r', encoding='utf-8') as salary:
    empl_dict = {line.split()[0]: float(line.split()[1]) for line in salary}
    print(f'average salary - {sum(empl_dict.values()) / len(empl_dict)}\n'
          f'salary less than 20000 {[item[0] for item in empl_dict.items() if item[1] < 20000] } ')

# task4

dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "четыре"}
with open('trans.txt', 'w', encoding='utf-8') as trans:
    with open('data.txt', 'r', encoding='utf-8') as data:
        trans.writelines([line.replace(line.split()[0], dic.get(line.split()[0])) for line in data])

# task5

from random import randint
with open('numbers.txt', 'w', encoding='utf-8') as num:
    my_list = [randint(1, 100) for _ in range(100)]
    num.write(" ".join(map(str, my_list)))
print(f'sum - {sum(my_list)}')

# task6
my_dic = {}
with open('subj.txt', encoding='utf-8') as subj:
    for line in subj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dic[name] = name_sum
print(my_dic)





