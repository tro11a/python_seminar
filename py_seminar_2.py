# Задача из дз №1
# x = str(input('Введите любое положительное число: ').replace('.', '0'))
# # x = input(str('Введите любое положительное число: '))
# snum = list(x.strip())
# # if '.' in snum:
# #     index = snum.index('.')
# #     snum.pop(index)
# result = list(map(int, snum))
# s = sum(result)
# print(s)

# Задача из дз 2
# n = int(input('Введите любое положительное число: '))
# nlist = []
# if n > 0:
#     i = 0
#     x = 1
#     while i < n:
#         x = x*(i+1)
#         nlist.append(x)
#         i += 1
#     print(nlist)
# elif n == 0:
#     x = 0
#     print(nlist)
# else:
#     print(str('Вы ввели некорректное значение!'))

# Задача из дз 3
import random
y = str(input('Введите любsые значения через пробел: '))
list = list(y.split())
random.shuffle(list)
print(list)
