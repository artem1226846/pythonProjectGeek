# task 1
a = input()
while a != '':
    with open('user_data.txt', 'a', encoding='utf-8') as f:
        f.write(f'{a}\n')
    a = input()

# task 2
strings = 0
strings_len = dict()
with open(r'text.txt', 'r', encoding='utf-8') as f:
    for i in f:
        strings += 1
        strings_len[f'string {strings} -'] = len(i.split())
print(f'number of strings: {strings}')
if strings != 0:
    print('number of words in strings:')
    for i, j in strings_len.items():
        print(i, j)

# task 3
from statistics import mean
sal = []
with open(r'staff.txt', 'r', encoding='utf-8') as f:
    for i in f:
        x = i.split()
        surname = x[0]
        salary = float(x[1])
        sal.append(salary)
        if salary < 20000:
            print(surname)
print(mean(sal))

# task 4
n = 0
words = ['Один', 'Два', 'Три', 'Четыре']
with open(r'text2.txt', 'r', encoding='utf-8') as f:
    for i in f:
        a = f'{words[n]} — {n+1}\n'
        with open(r'text3.txt', 'a', encoding='utf-8') as f2:
            f2.write(a)
        n += 1

# task 5
with open(r'text4.txt', 'w+', encoding='utf-8') as f:
    f.write('22 34 12 444 224')
    f.seek(0)
    print(sum(map(int, f.readline().split())))

# task 6
subjects = dict()
with open(r'subjects.txt', 'r', encoding='utf-8') as f:
    for i in f:
        x = ''
        subj = i.split(sep = ':')
        for j in subj[1]:
            try:
                int(j)
                x += j
            except ValueError:
                x += ' '
        subjects[subj[0]] = sum(map(int, x.split()))
print(subjects)

# task 7
from statistics import mean
import json
profits = []
firms = dict()
with open(r'firms.txt', 'r', encoding='utf-8') as f:
    for i in f:
        firm = i.split()
        name = firm[0]
        profit = float(firm[2]) - float(firm[3])
        if profit >= 0:
            profits.append(profit)
        firms[name] = profit
av_profit = {'average_profit': mean(profits)}
final_list = [firms, av_profit]
with open("firms.json","w") as write_f:
    json.dump(final_list, write_f)
