# Pavel

# Урок 8. Задание 1. Тема: Функции в python.
# Напишите функцию, чтобы найти максимальное из трех чисел
#
def max_num(num1, num2, num3):
    """Ищем максимальное число из трех"""
    if num1 < num3 and num2 < num3:
        number = f'Максимальное число {num3}'
    elif num1 < num2 and num3 < num2:
        number = f'Максимальное число {num2}'
    elif num2 < num1 and num3 < num1:
        number = f'Максимальное число {num1}'
    elif num1 < num2 == num3:
        number = f'Максимальные числа {num2} и {num3}'
    elif num2 < num1 == num3:
        number = f'Максимальные числа {num1} и {num3}'
    elif num3 < num1 == num2:
        number = f'Максимальные числа {num1} и {num2}'
    elif num1 == num2 == num3:
        number = f'Числа {num1}, {num2}, {num3} равны!'
    else:
        number = f'Проверьте данные!'

    return number


biggest_number = max_num(
                        int(input('Введите 1-ое число: ')),
                        int(input('Введите 2-ое число: ')),
                        int(input('Введите 3-ое число: '))
                    )
print(biggest_number)

# # Задание 2.
# Напишите функцию, для суммирования всех чисел в списке. Не использовать встроенную функцию sum
# Образец списка: (8, 2, 3, 0, 7)

list1 = (8, 2, 3, 0, 7)


def sum_num(var):
    total = 0
    for i in var:
        total += i
    return total


print(f'Сумма чисел в списке {list1} равна {sum_num(list1)}')


# # Задание 3.
# Напишите функцию, для умножения всех чисел в списке
# Образец списка: (8, 2, 3, -1, 7)

list1 = (8, 2, 3, -1, 7)


def multi_num(var):
    total = 1
    for i in var:
        total *= i
    return total


print(f'Произведение чисел в списке {list1} равна {multi_num(list1)}')

# # Задание 4.
# '''Напишите функцию, для переворота строки
# Пример строки: 1234abcd'''

str1 = '1234abcd'


def rev_str(var):
    return var[::-1]


print(rev_str(str1))

# # Задание 5.
# '''Напишите функцию, для вычисления факториала числа (неотрицательное целое число).
# Функция принимает число в качестве аргумента
# 5! = 1*2*3*4*5'''
#
def fact_num(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total


fact_in_num = int(input("Введите число: "))
print(f'Факториал числа {fact_in_num} равна {fact_num(fact_in_num)}')

# # Задание 6.
# '''Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра
# Пример строки: ‘The quick Brow Fox’'''
#
def count_upper_lower(var):
    upper_count = 0
    lower_count = 0
    for letter in var:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    return upper_count, lower_count


str1 = 'The quick Brow Fox'
print(count_upper_lower(str1))
#
# # Задание 7.
# '''Напишите функцию, которая принимает слово и определяет является ли оно палиндромом
# (палиндром — Слово или фраза, которые одинаково читаются слева направо и справа налево.)'''
#
def is_palindrome(word):
    return word == word[::-1]


word = input('Введите слово, которое может быть палиндромом: ')
print(is_palindrome(word))
#
# # Задание 8.
# '''Пользователь делает вклад в размере n рублей сроком на years лет под 10% годовых.
# Написать функцию bank, принимающая количество денег и лет, и возвращающую сумму,
# которая будет на счете через years лет'''
#
def bank(n, years):
    return round(n * 1.1 ** years, 2)


n = int(input('Введите сумму вклада: '))
years = int(input('На сколько лет вы хотите внести вклад: '))
print(f'Ваша сумма {n}$ через {years} лет будет составлять {bank(n, years)}$')
#
# # Задание 9.
# '''С помощью функции извлеките из списка числа, делимые на 15
# nums = [45, 55, 60, 37, 100, 105, 220]'''
#
def divisible_by_15(nums):
    return [i for i in nums if i % 15 == 0]


nums = [45, 55, 60, 37, 100, 105, 220]
print(divisible_by_15(nums))

# # Задание 10.
# '''Напишите функцию, которое принимает целое число и возвращает сумму цифр целого числа 108 -> 9'''
#
def sum_of_digits(n):
    return sum(int(i) for i in str(n))


n = input('Введите число: ')
print(f'Сумма цифр числа {n} равна {sum_of_digits(n)}')
#
# # Задание 11.
# '''Напишите функцию, которая будет принимать количество секунд и возвращать их в днях-часах-минутах-секундах
# 91000 секунд = 1 день, 1 час, 16 минут, 40 секунд'''
#
def time_form(seconds):
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    return f"{days} дней, {hours} часов, {minutes} минут, {seconds} секунд"


sec = int(input('Введите количество секунд: '))
print(time_form(sec))
#
# # Задание 12.
# '''Создайте пакет ‘figures’, состоящий из трех подпакетов: ‘triangle’, ‘circle’, ‘square’.
# В каждом подпакете будем иметь файл code.py, где создадим ряд функций:
# – для пакета ‘circle’: функции circle_perimeter() – вычисляет длину окружности,
# circle_area() – вычисляет площадь окружности. Еще заведем переменную default_radius = 5,
# – для пакета ‘triangle’: функции triangle_perimeter() – вычисляет периметр треугольника,
# triangle_area() – вычисляет площадь фигуры. Дополнительно создадим три переменные (длины сторон треугольника):
# a = 7, b = 2, c = 8, которые также не будут видны при импорте.
# – для пакета ‘square’: функции square_perimeter() – вычисляет периметр квадрата, square_area() –
# вычисляет площадь фигуры. Дополнительная переменная a = 15 не доступна при импорте и принимается функциями,
# если пользователь не предоставил свои размеры стороны квадрата.
# Ваша итоговая задача – позволить человеку, загрузившему ваш пакет, иметь возможность напрямую импортировать
# все функции из подпакетов. Например, он может написать так: ‘from figure import circle_area’.'''

from figures.circle.code import *
from figures.triangle.code import *
from figures.square.code import *


radius = int(input('Введите радиус круга: '))
print(f'Длина окружности с радиусом {radius} равна {round(circle_perimetr(radius)), 2}')
print(f'Площадь окружности с радиусом {radius} равна {round(circle_area(radius)), 2}')

a_tr = int(input('Введите сторону 1-ую сторону треугольника: '))
b_tr = int(input('Введите сторону 2-ую сторону треугольника: '))
c_tr = int(input('Введите сторону 3-ую сторону треугольника: '))

if (a_tr + b_tr + c_tr) / 2 == a_tr or (a_tr + b_tr + c_tr) / 2 == b_tr or (a_tr + b_tr + c_tr) / 2 == c_tr:
    print(f'Такого треугольника не существует!')
else:
    print(f'Периметр треугольника со сторонами {a_tr}, {b_tr} и {c_tr} равна {triangle_perimeter(a_tr, b_tr, c_tr)}')
    print(f'Площадь треугольника со сторонами {a_tr}, {b_tr} и {c_tr} равна {triangle_area(a_tr, b_tr, c_tr)}')

a_kv = int(input('Введите сторону квадрата: '))

print(f'Периметр квадрата со сторонами {a_kv} равна {square_perimeter(a_kv)}')
print(f'Площадь квадрата со сторонами {a_kv} равна {square_area(a_kv)}')


# # Задание 13.
# '''10 любых задач с https://www.codewars.com/'''

def human_years_cat_years_dog_years(humanYears):
    """I got them at the same time as kitten/puppy. That was humanYears years ago.
    Return their respective ages now as [humanYears,catYears,dogYears]"""
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 +(4 * (humanYears - 2))
        dogYears = 15 + 9 +(5 * (humanYears - 2))
    return [humanYears, catYears, dogYears]

def how_much_water(water, load, clothes):
    """My washing machine uses water amount of water to wash load (in JavaScript and Python)
    or max_load (in Ruby) amount of clothes. You are given a clothes amount of clothes to wash.
    For each single item of clothes above the load, the washing machine will use 10% more water
    (multiplicative) to clean."""
    if clothes < load:
        return 'Not enough clothes'
    elif clothes > 2 * load:
        return 'Too much clothes'
    else:
        return round(water * 1.1 ** (clothes - load), 2)
    pass

def chromosome_check(sperm):
    """The male gametes or sperm cells in humans and other mammals are heterogametic
    and contain one of two types of sex chromosomes. They are either X or Y."""
    if sperm == 'XX':
        return "Congratulations! You're going to have a daughter."
    elif sperm == 'XY':
        return "Congratulations! You're going to have a son."

def simple_multiplication(number):
    """This kata is about multiplying a given number by eight
    if it is an even number and by nine otherwise."""
    return number * 9 if number % 2 else number * 8

