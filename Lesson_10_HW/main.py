# Pavel

import re

# Задание 1. Тема: Регулярные выражения
# В примере найти и вывести трехзначные числа с помощью регулярных выражений.

sample = 'Exercises number 1, 12, 13, and 345 are important 456'

print(re.findall(r'\d{3}', sample))


# Задание 2.
# Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF,
# то есть # и содержит затем 6 шестнадцатеричных символов.

colors = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fghw3d', '#8B0000']
print(re.findall(r'\#([A-F0-9]{6})', str(colors)))

# Задание 3.
# Найти в тексте время. Время имеет формат часы:минуты.
# И часы, и минуты состоят из двух цифр, пример: 09:00.
# Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00».
# Учтите, что «37:98» – некорректное время.

text = ['Завтрак в 09:00', 'Завтрак в 90:00', 'Обед  в 13:00', 'Обед в 13:61', 'Ужин в 19:05', 'Ужин в 37:98',
        'Ужин в 24:01']
time = re.compile(r'([0-1]\d|2[0-3]):([0-5]\d)')
norm_time = list(filter(time.findall, text))
print(norm_time)

text = ['Завтрак в 09:00', 'Завтрак в 90:00', 'Обед  в 13:00', 'Обед в 13:61', 'Ужин в 19:05', 'Ужин в 37:98',
        'Ужин в 24:01']
print(re.findall(r'([0-1]\d|2[0-3]):([0-5]\d)', str(text)))

# Задание 4.
# Создать запрос для выбора из текста дробных чисел с разделителем дробной части в виде точки.
# Разряды целой части могут не выделяться или отделяться пробелом или запятой. 1231.12313

numbers = [1231.12313, 2121.121, 3.14, 6598, 9898787, 999.99, '098 90', '123,123']
print(re.findall(r'(\d+[.]\d+)', str(numbers)))


# Задание 5.
# Добавить регулярное выражения для поиска и вывода MAC адресов в скрипте который работал
# с конфигурациями маршрутизатора (можно переделать весь скрипт для работы с регуляркой)

def mac(adress):
    return re.findall(r'([A-Fa-f0-9]{2,4}[-.:]){2,5}[A-Fa-f0-9]{2,4}', adress)


# Задание 1. Тема: Работа с внешними данными: JSON, CSV
# С сайта https://jsonplaceholder.typicode.com/
# a) На основе WEB ресурса Создать свои JSON файлы
# b) c JSON файлов переделать данные в формат CSV файла
# с) с CSV файла обратно конвертировать данные в JSON формат и создать файл

import requests
import json
import csv

"""save as json file"""

comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()

list1 = []

for comment in comments:
    num_id = comment['id']
    name = comment['name']
    email = comment['email']

    list1.append({
        'Номер_id': num_id,
        'Заголовок': name,
        'Почта': email
    })

with open('comments.json', 'w', encoding='UTF-8') as file:
    json.dump(list1, file, ensure_ascii=False, indent=4)


"""json to csv file"""

with open("comments.json", encoding="UTF-8") as file:
    src = json.load(file)


with open("json_to_csv.csv", 'w', encoding="cp1251", newline='') as file2:
    writer = csv.DictWriter(file2, fieldnames="Номер_id Заголовок Почта".split())
    writer.writeheader()

    for line in src:
        writer.writerow(line)


"""csv to json file"""

json_data = []

with open("json_to_csv.csv") as file:
    reader = csv.DictReader(file)

    for line in reader:
        json_data.append(line)


with open('csv_to_json.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)


# Задание 2.
# У системного/сетевого администратора есть инструмент мониторинга сети PRTG
#   (Графическое отображения только для примера )
#   Администратор сгенерировал с системы мониторинга отчет о трафике в файлах формата CSV и XML, и теперь необходимо:
# a) С файла historicdata.csv вытащить все значения поля «Traffic In (speed)», выяснить максимум и минимум трафика,
#   а так же конвертировать значения в читабельный вид (дано в kbit/s, нужен вид в Gbit/s или Mbit/s
#   в зависимости от читабельности)
# b) С файла historicdata.xml вытащить все значения поле «Traffic Out (volume)», выяснить максимум и минимум
#   трафика, а так же конвертировать значения в читабельный вид (дано в KByte, нужен вид в GByte или MByte
#   в зависимости от читабельности)

"""work with csv file"""

with open('historicdata.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Traffic In (speed)'])



""""work with xml file"""

import xml.etree.ElementTree as ET

tree = ET.parse('historicdata.xml')
root = tree.getroot()





