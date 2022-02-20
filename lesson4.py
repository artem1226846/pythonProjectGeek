# task 1
from sys import argv
script_name, work_hours, hour_income, premium = argv
salary = float(work_hours) * float(hour_income) + float(premium)
print(salary)

# task 2
list1 = list(map(int, input().split()))
list2 = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]
print(list2)

# task 3
answer = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(answer)

# task 4
list1 = input().split()
list2 = [i for i in list1 if list1.count(i) == 1]
print(list2)

# task 5
from functools import reduce
list1 = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x, y: x * y, list1))

# task 6
from itertools import count, cycle
start = int(input())
for i in count(start):
    if i > 30:
        break
    print(i)
list1 = input().split()
end = int(input())
x = 0
for i in cycle(list1):
    if x == end:
        break
    x += 1
    print(i)

# task 7

def fact(n):
    for i in range(1, n+1):
        yield i
res = 1
x = int(input('Введите число: '))
for el in fact(x):
    res = res * el
    print(f'{el}! = ', res)

