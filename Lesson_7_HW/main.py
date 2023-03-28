# # Pavel
# import sys
# import logging
#
#
# '''Урок № 7. Задание 1 Тема: break, continue, pass
# Есть список list1 = [i for i in range(100)], создайте новый список
# с пробросом каждого пятого элемента (используйте continue)'''
#
# list1 = [i for i in range(100)]
# list2 = []
# for i in list1:
#     if i % 5 == 0 and i != 0:
#         continue
#     list2.append(i)
# print(list2)
#
#
# '''Урок № 7. Задание 2
# Напишите скрипт который будет работать циклично в интерактивном режиме,
# скрипт должен запрашивать имя пользователя, если пользователь не вводя имя нажмет на Enter
# то скрипт должен завершиться (используйте break)'''
#
# while True:
#     name = input('Введите свое имя: ')
#     if not name:
#         break
#
# '''Урок № 7. Задание 3
# Есть список: list1 = [‘micros’, ‘python’, ‘linux’, ‘windows’, ‘bobo’],
# из него составить новый список, но без буквы ‘i’, результат:
# list2 = [‘mcros’, ‘python’, ‘lnux’, ‘wndows’, ‘bobo’] (используйте pass)'''
#
# list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
# list2 = []
# for word in list1:
#     if word != 'i':
#         list2.append(word.replace('i', ''))
#     else:
#         pass
# print(list2)
#
#
# '''Урок № 7. Задание 1 Тема: Try/except/finally/else
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них
# не является числом, то должна выполняться конкатенация, то есть соединение, строк.
# В остальных случаях введенные числа суммируются.'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# while True:
#     value1 = input("Введите первое значение: ")
#     value2 = input("Введите второе значение: ")
#     if not value1:
#         break
#     elif not value2:
#         break
#     try:
#         num1 = float(value1)
#         num2 = float(value2)
#     except ValueError as error:
#         print("Конкатенация: " + value1 + value2)
#         logger.error(error)
#         print(logger)
#     else:
#         print("Сумма: " + str(num1 + num2))
#
# '''Урок № 7. Задание 2
# Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’],
# необходимо разделить на два списка, в первом только цифровые значения, а во втором только строки'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
# numbers = []
# strings = []
# for element in list1:
#     try:
#         if type(element) == int:
#             numbers.append(element)
#         elif type(element) == str:
#             strings.append(element)
#     except ValueError as error:
#         strings.append(element)
#         logger.error(error)
#         print(logger)
# print("Список чисел:", numbers)
# print("Список строк:", strings)
#
#
# '''Урок № 7. Задание 3
# Тот же самый пример, с сообщением после каждой итерации о том что элемент N добавлен'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
# numbers = []
# strings = []
# for element in list1:
#     try:
#         if type(element) == int:
#             numbers.append(element)
#             print(f"Элемент {element} добавлен в список строк чисел.")
#         elif type(element) == str:
#             strings.append(element)
#             print(f"Элемент {element} добавлен в список строк слов.")
#     except ValueError as error:
#         strings.append(element)
#         logger.error(error)
#         print(logger)
# print("Список чисел:", numbers)
# print("Список строк:", strings)
#
#
# '''Урок № 7. Задание 4
# Приведенный ниже код назначает 5-ю букву каждого слова в food новый список fifth.
# Однако код в настоящее время выдает ошибки. Вставьте предложение try/except, которое позволит запустить код
# и создать список 5-й буквы в каждом слове. Если слово недостаточно длинное, оно не должно ничего выводить.
# Примечание. pass — Оператор является нулевой операцией; ничего не произойдет при его выполнении.'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
# fifth = []
# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError as error:
#         pass
#         logger.error(error)
#         print(logger)
# print(fifth)
#
#
# '''Урок № 7. Задание 5
# Приведенный ниже код делит значения элемента на самого себя, но вылетает с ошибками, необходимо учесть
# все типы ошибок и дописать код (условия цикла менять нельзя, использовать полный синтаксис try/except/else)'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
# for index in range(len(my_list)+5):
#     try:
#         print(my_list[index] / my_list[index])
#     except ZeroDivisionError as error:
#         logger.error(error)
#         print(f'“Нельзя делить на ноль:”', error)
#     except TypeError as error:
#         logger.error(error)
#         print(f'Нельзя делить разные типы данных:', error)
#     except IndexError as error:
#         logger.error(error)
#         print(f'Нет такого индекса в списке:', error)
#     else:
#         print(f'Деление выполнено успешно')
#
#
# '''Урок № 7. Задание 6
# Дописать код (нельзя использовать просто except)'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
# search_key = "non-existent key"
# try:
#     print(my_dict[search_key])
# except KeyError as error:
#     logger.error(error)
#     print(f"Сорри, {search_key} это не правильный ключ")
#
#
# '''Урок № 7. Задание 7.
# Замените первый if на try/except/else'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# if len(sys.argv) < 2:
#     try:
#         city = sys.argv[1]
#         city = city.lower()
#     except IndexError as error:
#         logger.error(error)
#         print("Try again")
#         exit()
#     if city == "tashkent"[0:len(city)]:
#         print("В Ташкенте тепло и солнечно")
#     elif city == "london"[0:len(city)]:
#         print("В Лондоне пасмурно и сыро")
#     elif city == "moskow"[0:len(city)]:
#         print("В Москве идёт сильный дождь")
#     elif city == "paris"[0:len(city)]:
#         print("погода для романтики")
#     elif city == "rio de janeyro"[0:len(city)]:
#         print("В Рио постоянно карнавалы")
#     else:
#         print("прогноз не ясен, карантин")
#         print("Вы не указали название города")
#
# '''Урок № 7. Задание 8.
# Следующий код работает отлично, если пользователь вводит цифровое значение, но всегда есть НО:'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# try:
#     min = int(input("Введите первое число: "))
#     max = int(input("Введите второе число: "))
#     for i in range(min, max + 1):
#         print(f"Квадрат числа {i} равен {i*i}")
# except ValueError as error:
#     logger.error(error)
#     print(f"Элемент не является числом.")
#
# '''Урок № 7. Задание 9.
# Ловить ошибки это конечно здорово, но уметь логировать их и записывать в файл еще лучше,
# задача разобраться со стандартной библиотекой logging
# a) Найдите способ чтоб можно было добавить время ошибки, например вот так:
# b) Ко всем предыдущим примерам добавить логирования в файл'''
#
# logging.basicConfig(filename='my_error.log', format='%(asctime)s %(levelname)s %(message)s')
# logger = logging
# try:
#     1/0
# except ZeroDivisionError as error:
#     logger.error(error)
#     print(logger)
#
#
# '''Урок № 7. Задание 1 Тема: Работа с файлами
# Откройте файл mbox-short.txt, “прочитайте” каждую строку в этом файле и найдите строки,
# соответствующие данной: “From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008” .
# Затем распечатайте все ВХОДЯЩИЕ email адреса и их общее количество. Для решения данной задачи
# используйте методы строк. (используйте with open).'''
#
# cnt = 0
# with open("files/mbox-short.txt", mode='r', encoding='UTF-8') as mail:
#     for line in mail:
#         if line.startswith('From '):
#             print(line.strip().split()[1])
#             cnt += 1
# print(f'Количество входящих писем: {cnt}')
#
# '''Урок № 7. Задание 2.
# Откройте файл romeo.txt. “Прочитайте” в нем каждую строку. Получите отдельные слова из каждой строки,
# после чего составьте список слов. В списке слова не должны дублироваться. После чего распечатайте список,
# в котором все слова будут отсортированы в алфавитном порядке. (используйте open)'''
#
# file = open('files/romeo.txt', mode='r', encoding='UTF-8')
# word = list(set(file.read().split()))
# print(word)
# file.close()
#
# '''Урок № 7. Задание 3.
# Напишите код программы, которая будет открывать файл «article.txt» и выводить на печать построчно
# последние строки в количестве lines (число которую можно запросить у пользователя).
# Число должно быть положительным (используйте with open)'''
#
# lines = int(input("Введите число строк: "))
# with open("files/article.txt", mode="r", encoding='UTF-8') as file:
#     if lines > 0:
#         content = file.readlines()
#         start = len(content) - lines
#         for i in range(start, len(content)):
#             print(content[i], end="")
#     else:
#         print("Число должно быть положительным!")
#
# '''Урок № 7. Задание 4.
# Документ «article.txt» содержит следующий текст: (используйте open)
# Требуется реализовать код программы, которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).'''
#
# file = open("files/article.txt", mode="r", encoding='UTF-8')
# text = file.read()
# words = text.split()
# max_length = 0
# max_words = []
# for word in words:
#     length = len(word)
#     if length > max_length:
#         max_length = length
#         max_words = [word]
#     elif length == max_length:
#         max_words.append(word)
# if len(max_words) == 1:
#     print(f"Слово с максимальной длиной: {max_words[0]}")
# else:
#     print(f"Список слов с максимальной длиной: {max_words}")
# file.close()

'''Урок № 7. Задание 5.
Объедините содержимое файлов pushkin.txt, byron.txt, romeo.txt в один файл Poems.txt.
(используйте with open и просто open)
Разверните строки каждого стихотворения.
Постарайтесь придерживаться правильного выравнивание текста и чтоб знак «=>»
вставлялся ровно посередине каждого стихотворения (добейтесь результата в точности как на картинке)'''






