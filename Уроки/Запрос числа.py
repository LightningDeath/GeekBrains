number = int(input('Введите число: '))
while number < 0 or number > 10:
    print('Вы ввели не подходящее число!')
    number = int(input('Введите число в диапазоне от 0 до 10: '))
result = number**2
print('Вы ввели подходящее число!')
print('результат: ',result)