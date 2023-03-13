# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

import random
n = int(input("Введите количество элементов в массиве: "))
m = []
for _ in range(n):
    m.append(random.randint(0, 10))
print(m)
result = {}
for i in m:
    result[i] = result.get(i, 0) + 1
print(result)

count = 0
for (key, value) in result.items():
    c = value//2
    count += c
print(count)


# Пробы и ошибки:

# for item in m:
#     if item == item:
#         count += 1
# print(count)

# list_1 = m[:2]
# # list_1 = [print(m[:(len(m)-1)//2])]
# print(list_1)    # как сделать, чтобы list_1 заполнялся через срез?

# if len(m) % 2 == 0:
#     list_1 = []
#     i = 0
#     while i < (len(m))//2:
#         list_1.append(m[i])
#         i += 1
#     print(list_1)
#     list_2 = []
#     i = len(m)//2
#     while i < len(m):
#         list_2.append(m[i])
#         i += 1
#     print(list_2)
#     count = 0
#     for item in list_1:
#         if item in list_2:
#             count += 1
#     print(count)
# else:
#     list_1 = []
#     i = 0
#     print((len(m)-1)//2)
#     while i < (len(m)-1)//2:
#         list_1.append(m[i])
#         i += 1
#     print(list_1)
#     list_2 = []
#     i = (len(m)-1)//2+1
#     print(i)
#     while i < len(m):
#         list_2.append(m[i])
#         i += 1
#     print(list_2)
#     list_3 = []
#     i = (len(m)-1)//2
#     print(i)
#     list_3.append(m[i])
#     print(list_3)
#     count = 0
#     for item in list_1:
#         if item in list_2 or item in list_3:
#             count += 1
#     for item in list_2:
#         if item in list_3:
#             count += 1
#     print(count)
