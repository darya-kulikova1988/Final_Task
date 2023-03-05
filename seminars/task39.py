# Даны два массива чисел. Требуется вывести те элементы первого массива(в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# Вывод:
# 3 3 2 12
import random


def massive(n):
    m = []
    for _ in range(n):
        m.append(random.randint(0, 10))
    return m


n1 = int(input("Введите количество элементов в массиве: "))
m1 = massive(n1)
print(m1)
n2 = int(input("Введите количество элементов в массиве: "))
m2 = massive(n2)
print(m2)
m3 = []
for item in m1:
    if item not in m2:
        m3.append(item)
print(m3)


# print([elem for elem in m1 if elem not in m2])

# from random import randint
# list_1 = [randint(1, 20) for _ in range(int(input('Input length 1 mass: ')))]
# list_2 = [randint(1, 20) for _ in range(int(input('Input length 2 mass: ')))]
# print(f'Mass_1: {list_1}\nMass_2: {list_2}')
# print(f'New mass: {[elem for elem in list_1 if elem not in list_2]}')
