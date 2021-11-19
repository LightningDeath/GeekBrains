import math

second = int(input('Введите секунды:'))
# список времени с количеством секунд в дне, часе, минуте соответственно
time = [86400, 3600, 60]
n = 0
# инициализируем сравнение полученного числа со списком
while n <= len(time) and second <= time[n]:
    n += 1
if n > len(time):
    print(second, 'сек.')
if n == 1:
    hour = math.floor(second/time[n])
    minute = math.floor((second - hour * time[n])/time[n+1])
    second = hour - minute * time[n+1]
    print(hour, ' hour', minute, 'minute', second, 'second')
else:
    if n == 2:
        minute = math.floor(second / time[n])
        second = second - minute
        print(minute, 'minute', second, 'second')
if n == 0:
    days = math.floor(second/time[n])
    hour = math.floor((second - days * time[n])/time[n+1])
    minute = math.floor((days - hour*time[n+1])/time[n+2])
    second = hour - minute
    print(days, 'days', hour, 'hour', minute, 'minute', second, 'second')
