# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели
# и проверяет, является ли этот день выходным.
import math

# print('Введите число от 1 до 7: ')
# a = int(input())

# if a == 6:
#    print('Суббота')
# elif a == 7:
#    print('Воскресенье')
# else:
#    print('Будний день')

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print('Задайте значение X: ')
# x = int(input())
# print('Задайте значение Y: ')
# y = int(input())
# print('Задайте значение Z: ')
# z = int(input())

# for x in [True, False]:
#    for y in [True, False]:
#        for z in [True, False]:
#            print('not', x, 'or', y, 'or', z, '=', 'not', x, 'and', 'not', y, 'and', 'not', z)


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём.
# X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

# print('Задайте значение X: ')
# x = int(input())
# print('Задайте значение Y: ')
# y = int(input())

# if x > 0 and y > 0:
#    print('Первая четверть')
# if x < 0 and y > 0:
#    print('Вторая четверть')
# if x < 0 and y < 0:
#    print('Третья четверть')
# if x > 0 and y < 0:
#    print('Четвёртая четверть')
# elif x == 0 or y == 0:
#    print('Неверные значения')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

# print('Задайте номер четверти: ')
# quarter = int(input())

# if quarter == 1:
#    print('x > 0 and y > 0')
# if quarter == 2:
#    print('x < 0 and y > 0')
# if quarter == 3:
#    print('x < 0 and y < 0')
# if quarter == 4:
#    print('x > 0 and y < 0')
# elif quarter > 4:
#    print('Неверные данные')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве

print('Введите значение координаты X точки A: ')
x1 = int(input())
print('Введите значение координаты Y точки A: ')
y1 = int(input())
print('Введите значение координаты X точки B: ')
x2 = int(input())
print('Введите значение координаты Y точки B: ')
y2 = int(input())

distance = math.isqrt((x2 - x1)**2 + (y2 - y1)**2)
print(float(distance))





