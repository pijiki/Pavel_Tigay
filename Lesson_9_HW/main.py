# Pavel

# Задание 1. Тема: Полезные функции (zip, map, filter, lambda)
#  С помощью функции map выведите список имен с заглавной буквы.

names = ['alfred', 'tabitha', 'william', 'arla']


def reg(name):
    return name.title()


list1 = list(map(reg, names))
print(list1)


names = ['alfred', 'tabitha', 'william', 'arla']
up_reg = list(map(lambda name: name.title(), names))
print(up_reg)

# Задание 2.
# С помощью функции filter выведите список оценок, которые больше 75.
#
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def num(number):
    return number > 75


big_num = list(filter(num, scores))
print(big_num)

big_num2 = list(filter(lambda numb: numb > 75, scores))
print(big_num2)


# Задание 3.
# С помощью функции filter и Лямбда-функции выведите список слов-палиндромов.

words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']

def pal(word):
    return word.lower() == word.lower()[::-1]


pal_word = list(filter(pal, words))
print(pal_word)



pal_word2 = list(filter(lambda word: word.lower() == word.lower()[::-1], words))
print(pal_word2)


# Задание 4.
# Напишите две функции (с генератором и без), которые будут формировать два списка:
# list1 — это список четных чисел и list2 — это список не четных чисел. Диапазон от 1 до n
# (n – это число, которое ввел юзер). Затем напишите к ней декоратор, который будет выводить
# время потраченное на выполнение работы функции, а также размер списка, который она сформировала.

from datetime import datetime


def performance(arg):
    def performance2(object):
        def wrapper(*args, **kwargs):
            print(arg)
            start = datetime.now()
            decor = object(*args, **kwargs)
            stop = datetime.now()
            print(stop - start)
            return decor

        return wrapper

    return performance2


@performance('С генератором четные')
def generator_chet(number):
    list1 = [i for i in range(number + 1) if i % 2 == 0]
    return list1

@performance('С генератором нечетные')
def generator_nechet(number):
    list2 = [i for i in range(number + 1) if i % 2]
    return list2


@performance('Без генератора четные')
def without_generator_chet(number):
    list1 = []
    for i in range(number+1):
        if i % 2 == 0:
            list1.append(i)
    return list1

@performance('Без генератора нечетные')
def without_generator_nechet(number):
    list2 = []
    for i in range(number+1):
        if i % 2:
            list2.append(i)
    return list2

num = int(input("Введите число: "))

print(list(generator_chet(num)))
print(list(generator_nechet(num)))
print(list(without_generator_chet(num)))
print(list(without_generator_nechet(num)))

# Задание 5.
# Есть список слов. Нужно с помощью map и lambda функции вернуть список длин этих слов.

list1 = ('apple', 'banana', 'cherry')


def length_words(word):
    return len(word)


dl_words = list(map(length_words, list1))
print(dl_words)


dl_words2 = list(map(lambda wrd: len(wrd), list1))
print(dl_words2)


# Задание 6.
# Есть два текстовых списка. Нужно вернуть один список объединенных слов.

list1 = ['apple', 'banana', 'cherry']
list2 = ['orange', 'lemon', 'pineapple']

def plus_word(elem1, elem2):
    return elem1 + elem2


list3 = list(map(plus_word, list1, list2))
print(list3)

list4 = list(map(lambda word1, word2: word1 + word2, list1, list2))
print(list4)
