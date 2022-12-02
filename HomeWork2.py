# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import random

# num = float(input('Введите число: '))
# while num != int(num):
#     num *= 10
#
# sum = 0
# while num > 0:
#     sum += num % 10
#     num //= 10
# print(int(sum))

# 2. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

# n = int(input('Введите число: '))
# my_list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# print(f'Последовательность: {my_list} \nСумма: {round(sum(my_list), 3)}')

# 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('Начальный список: ' + str(my_list))
# for i in range(len(my_list)-1, 0, -1):
#     j = random.randint(0, i + 1)
#     my_list[i], my_list[j] = my_list[j], my_list[i]
# print('Перемешанный список: ' + str(my_list))





