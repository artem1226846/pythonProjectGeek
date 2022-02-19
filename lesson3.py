# task 1
def func_div(a, b):
    if b == 0:
        return 'Деление на ноль невозможно'
    else:
        return a / b
user_numbers = input('Введите 2 числа, разделенных пробелом: ').split()
print(func_div(int(user_numbers[0]), int(user_numbers[1])))

#task 2
def user_data(name, surname, year_of_birth, current_city, email, phone_number):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year_of_birth}, '
          f'Город проживания: {current_city}, email: {email}, Телефон: {phone_number}')
user_name = input('Введите ваше имя: ')
user_surname = input('Введите вашу фамилию: ')
user_year_of_birth = input('Введите ваш год рождения: ')
user_current_city = input('Введите ваш город проживания: ')
user_email = input('Введите ваш email: ')
user_phone_number = input('Введите ваш телефон: ')

user_data(name = user_name, surname = user_surname,year_of_birth = user_year_of_birth,
          current_city = user_current_city, email= user_email, phone_number = user_phone_number)


# task 3
def my_func(a, b, c):
    min_n = min(a, b, c)
    if min_n == a:
        return b + c
    elif min_n == b:
        return a + c
    else:
        return a + b

# task 4
num1 = float(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
def my_func(x, y):
    return x**y
print(my_func(num1, num2))

def my_func(x, y):
    res = 1/x
    for i in range(1,abs(y)):
        res = res / x
    return res
print(my_func(num1, num2))

# task 5

def my_func():
    my_sum = 0
    while True:
        x = input('Введите числа через пробел: ').split()
        for i in x:
            try:
                my_sum += float(i)
            except ValueError:
                print('Сумма = ',my_sum)
                return
        print('Сумма = ',my_sum)
my_func()

# task 6-7

def int_func(x):
    x = x.lower()
    x_upper = x.upper()
    x = x_upper[0] + x[1:]
    return x

words = input().split()
for word in range(len(words)):
    words[word] = int_func(words[word])
print(words)

