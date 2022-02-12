#task 1

var_1 = 23
var_2 = 'hello'
print(var_1, var_2)

var_1 = input()
var_2 = int(input())
print(var_1)
print(var_2**2)

#task 2

user_time = int(input())
time_hours = user_time // 3600
if time_hours < 10:
    time_hours = str(f'0{time_hours}')
time_minutes = (user_time % 3600) // 60
if time_minutes < 10:
    time_minutes = str(f'0{time_minutes}')
time_seconds = user_time % 60
if time_seconds < 10:
    time_seconds = str(f'0{time_seconds}')
print(f'{time_hours}:{time_minutes}:{time_seconds}')

#task 3

user_number = input()
print(int(user_number)+int(user_number*2)+int(user_number*3))

#task 4

user_number = int(input())
max_digit = user_number % 10
x = 10
y = (user_number // x) % 10
while (user_number // x)!=0:
    if y > max_digit:
        max_digit = y
    x *= 10
    y = (user_number // x) % 10
print(max_digit)

#task 5-6

benefit = int(input())
cost = int(input())
result = benefit - cost
if result < 0:
    print('loss')
elif result > 0:
    print('profit')
    profitability = result / benefit
    print(f'profitability = {profitability}')
    staff = int(input())
    profit_st = result / staff
    print(f'profit per employee = {profit_st}')
else:
    print('zero')

# #task 7

a = int(input())
b = int(input())
day = 1
while a < b:
    a += a*0.1
    day += 1
print(day)
