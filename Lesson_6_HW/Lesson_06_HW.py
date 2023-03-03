# Pavel
from pprint import pprint

''' Урок №6. Задание 1. Тема: Словари (Dict) / Методы словарей.
Есть два словаря, объедините их:'''

dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
}
dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
}

dict1.update(dict2)
pprint(dict1)


''' Урок №6. Задание 2.
Напишите сценарий Python для создания и печати словаря, содержащего число
(от 1 до n включительно) (где n — введенное пользователем число) в форме (x, x * x).'''

n = int(input("Введите конечное число: "))
num = {i: i*i for i in range(1, n+1)}
print(num)


''' Урок №6. Задание 3.
Напишите код для суммирования всех значений словаря и вывод среднего арифметического значения.'''

n = int(input("Введите конечное число: "))
num = {i for i in range(1, n+1)}
print(f'Сумма всех значений: {sum(num)}\nСреднее арифметическое: {sum(num) / len(num)}')


''' Урок №6. Задание 4.
Напишите код для объединения двух списков в словарь ключ: значение.
СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА (содержимое списков произвольный)'''

dict_keys = ['management', 'sales', 'hr', 'production', 'admins']
dict_items = ['vlan10', 'vlan20', 'vlan30', 'vlan40', 'vlan50' ]
dict1 = dict(zip(dict_keys, dict_items))
print(dict1)


''' Урок №6. Задание 5.
Есть словарь координат городов:
Составьте словарь расстояний между городами по формуле:'''
#
cities = {
   'Moscow': (550, 370),
   'London': (510, 510),
   'Paris': (480, 480),
}

distances = {}
moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']

distance1 = ((int(london[0]) - int(paris[0])) ** 2 + (int(london[1])- int(paris[1])) ** 2) ** 0.5
distance2 = ((int(moscow[0]) - int(london[0])) ** 2 + (int(moscow[1])- int(london[1])) ** 2) ** 0.5
distance3 = ((int(moscow[0]) - int(paris[0])) ** 2 + (int(moscow[1])- int(paris[1])) ** 2) ** 0.5

distances = {
    'London-Paris': round(distance1, 4),
    'Moscow-London': round(distance2, 4),
    'Moscow-Paris': round(distance3, 4)
}

print(distances)


''' Урок №6. Задание 1. Тема: Кортежи (tuple)/Множества (set)
Есть кортеж a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
Выведите в отдельный кортеж числа, которые меньше или равны 5 и числа, которые больше 5.'''

a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
b = tuple(i for i in a if i <= 5)
c = tuple(i for i in a if i > 5)
print(b)
print(c)


''' Урок №6. Задание 2.
Вы принимаете от пользователя его имя, фамилию, возраст.
Сохраните их в соответствующие переменные. Сохраните полученные значения в список.'''

name = input("Введите свое имя: ")
fam = input("Введите свою фамилию: ")
age = int(input("Введите свой возраст: "))
sp = (name, fam, age)
print(f'Ваши данные: {sp}')


''' Урок №6. Задание 3.
Напишите программу, которая принимает от пользователя секвенцию чисел,
разделенных запятой и пробелом. После чего запишите каждое число в кортеж.'''

num = input("Введите числа c помощью указанных знаков ', ': ")
print(f'Список чисел: {tuple(num.split(", "))}')


''' Урок №6. Задание 4.
Напишите программу, которая будет принимать три имени в качестве входных данных
от пользователя в одном input() и превращать данные в кортеж, ну а затем доставать их:'''

name = input("Введите имена через пробел: ")
name1, name2, name3, *_ = name.split()
print(f'Кортеж имен: {tuple(name.split())}')
print(f'Первое имя: {name1}')
print(f'Второе имя: {name2}')
print(f'Третье имя: {name3}')


''' Урок №6. Задание 5.
Дан кортеж чисел numbers = (1, 2, 3, 4, 5, 6, 7). напишите программу,
которая превращает каждый элемент кортежа в его квадрат и образует второй кортеж.'''

numbers = (1, 2, 3, 4, 5, 6, 7)
numbers1 = tuple(i*i for i in numbers)
print(f'Квадрат чисел {numbers}\n\t\tравна {numbers1}')

''' Урок №6. Задание 6.
Напишите программу, которая выводит все четные числа из кортежа в исходном порядке,
и останавливается когда число равно 815.
numbers = (386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527)'''

numbers = (386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399,
           162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67,
           104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527)
chet_num = []
for i in numbers:
    if i % 2 == 0 and i != 815:
        chet_num.append(i)
    elif i == 815:
        break
print(f'Список четных числе: {tuple(chet_num)}')


''' Урок №6. Задание 7.
Есть кортеж с данными numbers = (12, 33, 44, 33, 12, 45, 11, 55, ’44’, 30, 10),
создайте список и кортеж данных без дубликатов'''

numbers = (12, 33, 44, 33, 12, 45, 11, 55, "44", 30, 10)
numbers = set(numbers)
print(numbers)


''' Урок №6. Задание 8.
Получите кортеж VLANов со строки:
config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'
общих vlan
vlan которые есть в config_sw1 но нет в config_sw2
уникальные vlan c двух сторон
все vlan без дубликатов'''

config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw1 = set(tuple(config_sw1.split()[-1].split(',')))
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'
config_sw2 = set(tuple(config_sw2.split()[-1].split(',')))
print(config_sw1 & config_sw2)
print(config_sw1 - config_sw2)
print(config_sw1 ^ config_sw2)
print(config_sw1 | config_sw2)


''' Урок №6. Задание 1. Тема: Вложенность
В задании создан словарь, с информацией о разных устройствах.
Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1).
И вывести информацию о соответствующем устройстве'''

n = input('Введите название устройства [r1/r2/sw1]: ')
devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
if n == 'r1' in devices:
    pprint(devices['r1'])
elif n == "r2" in devices:
    pprint(devices["r2"])
elif n == 'sw1' in devices:
    pprint(devices['sw1'])
else:
    print(f'Sorry try again')


''' Урок №6. Задание 2.
Есть словарь кодов товаров и словарь количества товара на складе,
задача сопоставить два словаря и высчитать общее количество.'''

goods = {
 'Лампа': '12345',
 'Стол': '23456',
 'Диван': '34567',
 'Стул': '45678',
}
store = {
 '12345': [
  {
   'quantity': 27,
   'price': 42
  },
 ],
 '23456': [
  {
   'quantity': 22,
   'price': 510
  },
  {
   'quantity': 32,
   'price': 520
  },
],
 '34567': [
  {
   'quantity': 2,
   'price': 1200
  },
  {
   'quantity': 1,
    'price': 1150
  },
 ],
 '45678': [
  {
   'quantity': 50,
   'price': 100
  },
  {
   'quantity': 12,
   'price': 95
  },
  {
   'quantity': 43,
   'price': 97
  },
 ],
}


goods['Лампа'] = store['12345']
goods['Стол'] = store['23456']
goods['Диван'] = store['34567']
goods['Стул'] = store['45678']

for good, code in goods.items():
    quantity = 0
    price = 0
    for i in code:
        quantity += i['quantity']
        price += i['price']
    print(f'Продукт: {good}, Количество: {quantity}, Стоимость: {price}')
