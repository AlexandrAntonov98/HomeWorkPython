# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетным индексами.
# my_list = [1, 3, 4, 5, 6, 8, 89, 8]
# summa = 0
# for i in range(8):
#     if i % 2 != 0:
#         summa = summa + my_list[i]
# print(f'Сумма чисел с нечетными индексами: {summa}')
# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй
# и предпоследний и т.д.
# from random import randint
#
# number = int(input('Введите размер списка: '))
# list1 = []
# list2 = []
#
# for i in range(number):
#     list1.append(randint(0, 9))
#
# for i in range(len(list1)):
#     while i < len(list1)/2 and number > len(list1) / 2:
#         number = number - 1
#         a = list1[i] * list1[number]
#         list2.append(a)
#         i = i + 1
#
# print(list1)
# print(list2)
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# from random import uniform
#
# n = int(input('Введите размер списка '))
# list1 = []
# for i in range(n):
#     f = uniform(0, 9)
#     list1.append(round(f, 2))
#
# min = list1[0]
# max = 0
# for i in range(len(list1)):
#
#     if max < list1[i]:
#         max = list1[i]
#     if min > list1[i]:
#         min = list1[i]
# dif = (max - int(max)) - (min - int(min))
#
# print(list1)
# print(max, min)
# print(round(dif, 2))
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов
# a = int(input('Введите число: '))
# b = ''
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)
