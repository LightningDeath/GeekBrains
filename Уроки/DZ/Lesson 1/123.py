import math
second = int(input('Введите секунды:'))
# создаем список с количеством секунд в дне, часе, минуте соответственно
time = [86400, 3600, 60]
n = 0
if second <= 86400:
    if second <= 3600:
        hour = math.floor(second / time[n])
        minute = math.floor((second - hour * time[n]) / time[n + 1])
        second = hour - minute * time[n + 1]
        print(hour, ' hour', minute, 'minute', second, 'second')
    else:
        if second <=60:
            minute = math.floor(second / time[n])
            second = second - minute * time[n]
            print(minute, 'minute', second, 'second')
else:
    days = math.floor(second / time[n])
    hour = math.floor((second - days * time[n]) / time[n + 1])
    minute = math.floor(((second - days * time[n]) - hour * time[n + 1]) / time[n + 2])
    second = second - (days * time[0] + hour * time[1] + minute * time[2])
    print(days, 'days', hour, 'hour', minute, 'minute', second, 'second')