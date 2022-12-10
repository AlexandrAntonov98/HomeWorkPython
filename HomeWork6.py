# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
from random import sample
# длина списка
len_list = int(input("Ведите число длины списка: "))
# рандомный список
my_list = [i for i in sample(range(1, len_list*2), len_list)]
print("рандомный список: ", my_list)
# cортированный список
sort_list = [my_list[i]
             for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print("cортированный список: ", sort_list)
# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.
max_num = int(input("Ведите максимальное число в списке: "))
my_list = [i for i in range(20, (max_num + 1)) if i % 20 == 0 or i % 21 == 0]
print("Список кратный 20 или 21: ", my_list)
# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
name_list = "Илья", "Виктор", "Василиса", "Олег", "Александр", "Петр", "Алексей", "Степан"
print(name_list)

name_dict = {}

for name in name_list:
    key = name[0]

    if key not in name_dict:
        name_dict[key] = []
    name_dict[key].append(name)

print (name_dict)
