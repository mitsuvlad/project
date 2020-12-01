my_dic = {}
with open('subj.txt', encoding='utf-8') as subj:
    for line in subj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dic[name] = name_sum
print(my_dic)