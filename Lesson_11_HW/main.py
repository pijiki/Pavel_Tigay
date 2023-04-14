# Pavel

# Задание 1. Тема: Основы ООП
# Создать класс компьютер#
# C параметрами: Владелец, Процессор, ОЗУ, Объём жесткого диска, Монитор
# Прописать метод строкового представления класса
# Создать метод который будет возвращать имя владельца компьютера:
# Запускать его самостоятельно (через указания вручную),
# Сделать чтоб он запускался в конструкторе (автоматически)
# Создать метод который будет сравнивать два класса по их ОЗУ

# from functools import total_ordering
#
#
# @total_ordering
# class Computer:
#
#     def __init__(self, user, CPU, RAM, ROM, monitor):
#         self.user = user
#         self.CPU = CPU
#         self.RAM = RAM
#         self.ROM = ROM
#         self.monitor = monitor
#         self.say_my_name()
#
#     def __str__(self):
#         return f'Класс Computer со свойствами user={self.user}, ' \
#                f'CPU = {self.CPU}, RAM = {self.RAM}, ROM = {self.ROM}, monitor = {self.monitor}'
#
#     def say_my_name(self):
#         print(f'Пользователя зовут {self.user}')
#
#     def __eq__(self, other):
#         return self.RAM == other.RAM
#
#     def __lt__(self, other):
#         return self.RAM < other.RAM
#
#
# user1 = Computer(input('Введите имя 2-го пользователя: '), 'i5-11450', 8, 1000, '24 inch')
# user2 = Computer(input('Введите имя 2-го пользователя: '), 'i7-12450', 16, 1500, '32 inch')
#
# print(user1)
# print(user2)
#
#
# print(user1 > user2)
# print(user1 < user2)
# print(user1 >= user2)
# print(user1 <= user2)
# print(user1 == user2)
# print(user1 != user2)

# Задание 2.
# Создать Класс животное с одним параметром (по схеме)
# от него унаследовать четыре подкласса с уникальными параметрами
# затем создать по два объекта (экземпляра) от каждого подкласса


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
# class Birds(Animal):
#     def __init__(self, name, color, arial, size_wings, eats):
#         super(Birds, self).__init__(name)
#         self.color = color
#         self.arial = arial
#         self.wings = size_wings
#         self.eat = eats
#
#     def __str__(self):
#         return f'Класс Birds с name={self.name}, color={self.color}, arial={self.arial}, ' \
#                f'size wings={self.wings}, eats={self.eat}'
#
# class Mamal(Animal):
#     def __init__(self, name, color, arial, size, eats):
#         super(Mamal, self).__init__(name)
#         self.color = color
#         self.country = arial
#         self.size = size
#         self.eat = eats
#
#     def __str__(self):
#         return f'Класс Mamal с name={self.name}, color={self.color}, arial={self.arial}, ' \
#                f'size={self.size}, eats={self.eat}'
#
# class Reptile(Animal):
#     def __init__(self, name, arial, size_scales, size, eats):
#         super(Reptile, self).__init__(name)
#         self.arial = arial
#         self.scales = size_scales
#         self.size = size
#         self.eat = eats
#
#     def __str__(self):
#         return f'Класс Reptile с name={self.name}, arial={self.arial}, size scales={self.scales}, ' \
#                f'size ={self.size}, eats={self.eat}'
#
# class Fish(Animal):
#     def __init__(self, name, arial, color, eats):
#         super(Fish, self).__init__(name)
#         self.arial = arial
#         self.color = color
#         self.eat = eats
#
#
#     def __str__(self):
#         return f'Класс Fish с name={self.name}, arial={self.arial}, color={self.color}, eats={self.eat}'
#
#
# bird_eagle = Birds('Eagle', 'brown', 'USA', 40, "meat")
# bird_chiken = Birds('Chiken', 'white', 'everywhere', 20, 'corn')
#
#
# mamal_rat = Mamal('rat', 'grey', 'everywhere', 15, 'omnivorous')
# mamal_monkey = Mamal('monkey', 'orange', 'jungle', 50, 'fruits')
#
#
# reptile_snake = Reptile('snake', 'jungle', '6 mm', '1 m', 'meat')
# reptile_chameleon = Reptile('chameleon', 'jungle', '2 mm', '200 mm', 'insects')
#
#
# fish_clown = Fish('fish_clown', 'ocean', 'white-orange', 'plankton')
# fish_shark = Fish('white_shark', 'ocean', 'white-blue', 'meat')


# Задание 3.
# Создать класс Фигура с одним параметром (по схеме),
# от него унаследовать три подкласса с уникальными параметрами
# в каждом подклассе создать полезные методы
# Решить двумя способами, с помощью полиморфизма и без него


class Figures:
    def __init__(self, name):
        self.name = name


class Triangle(Figures):
    def __init__(self, name, a, b, c):
        super(Triangle, self).__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.perimetr(a, b, c)
        self.square(a, b, c)

    def perimetr(self, a, b, c):
        print(f'Периметр треугольника = {a + b + c}')

    def square(self, a, b, c):
        p = (a + b + c) / 2
        print(f'Площадь треугольника = {(p * (p - a) * (p - b) * (p - c)) ** 0.5}')


class Quadrilateral(Figures):
    def __init__(self, name, a, b):
        super(Quadrilateral, self).__init__(name)
        self.a = a
        self.b = b
        self.perimetr(a, b)
        self.square(a, b)

    def perimetr(self, a, b):
        print(f'Периметр четырехугольника = {(a + b) * 2}')

    def square(self, a, b):
        print(f'Площадь четырехугольника = {a * b}')


class Circle(Figures):
    def __init__(self, name, r):
        super(Circle, self).__init__(name)
        self.r = r
        self.perimetr(r)
        self.square(r)

    def perimetr(self, r):
        print(f'Периметр круга = {2 * 3.14 * r}')

    def square(self, r):
        print(f'Площадь круга = {3.14 * r ** 2}')


figure1 = Triangle('triangle', 5, 6, 10)
figure2 = Quadrilateral('rectangle', 5, 7)
figure3 = Circle('circle', 8)


