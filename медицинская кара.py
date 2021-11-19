first_name = input('Введите своё имя: ')
last_name = input('Введите свою фамилию: ')
age = int(input('Введите свой возраст: '))
wieght = int(input('Введите свой вес: '))
if 50 < wieght < 120:
    if age <= 30:
         print(first_name,last_name,',',age,'год,','вес',wieght,' - хорошее состояние!')
    else:
        if 30 <= age <= 40:
            print(first_name,last_name,',',age,'год,','вес',wieght,' - Требуется заняться собой!')
        else:
            print(first_name,last_name,',',age,'год,','вес',wieght,' - Требуется срочно обратиться к врачу!')
else:
    if wieght < 50:
        print('СРОЧНО К ВРАЧУ! ВЫ НЕ ЗДОРОВЫ! СЛИШКОМ НИЗКИЙ ВЕС! ВЫЗЫВАЙТЕ СКОРУЮ, ЕСЛИ СМОЖЕТЕ ПОДНЯТЬ ТЕЛЕФОН!')
    else:
        print('СРОЧНО К ВРАЧУ! ВЫ НЕ ЗДОРОВЫ! СЛИШКОМ БОЛЬШОЙ ВЕС! ВЫЗЫВАЙТЕ СКОРУЮ, ЕСЛИ ОНА СМОЖЕТ ВАС!')