# task 1
list1 = [123, 'word', 23.44, [1,2], ('jin', 44), {'sw':12,'ws':44}]
for i in list1:
    print(type(i))

# task 2
list2 = input().split()
x = len(list2)
y = x if x % 2 == 0 else  x - 1
for i in range(0, y, 2):
    list2[i], list2[i + 1] = list2[i + 1], list2[i]
print(list2)

# task 3
month = int(input('type month: '))
di = {1:'winter', 2:'winter', 3:'spring', 4:'spring',
      5:'spring', 6:'summer', 7:'summer', 8:'summer',
      9:'autumn', 10:'autumn', 11:'autumn', 12:'winter'}
print(di[month])
list1 = ['winter', 'winter', 'spring',
         'spring', 'spring', 'summer',
         'summer', 'summer', 'autumn',
         'autumn', 'autumn', 'winter']
print(list1[month-1])

# task 4
list2 = input('type words: ').split()
for i, j in enumerate(list2):
    if len(j) > 10:
        print(i+1, j[0:10])
    else:
        print(i+1, j)

# task 5
my_list = [7, 5, 3, 3, 2]
user_number = int(input('type number: '))
x = len(my_list)
for i in range(0, x):
    if user_number > my_list[i]:
        my_list.insert(i, user_number)
        break
    elif i < x - 1:
        if user_number <= my_list[i]:
            continue
    else:
        my_list.append(user_number)
print(my_list)

# task 6
products = []
number_of_products = int(input('укажите количество товаров: '))
number = 1
while number <= number_of_products:
    current_product = [input(f'укажите название товара № {number}: '), float(input('укажите цену: ')),
                   float(input('укажите количество: ')), input('укажите единицу измерения: ')]
    products.append((number, {'название':current_product[0], 'цена':current_product[1],
                           'количество':current_product[2], 'ед':current_product[3]}))
    number += 1
print(products)
analytics = {'название':[],'цена':[],'количество':[],'ед':[]}
for i in products:
    for j in analytics:
        if i[1][j] not in analytics[j]:
            analytics[j].append(i[1][j])

print(analytics)

