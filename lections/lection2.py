# list_1 = []
# list_2 = list()
# print(list_1, list_2)
# list_3 = [1, 2, 3, 8]
# print(*list_3)
# print(len(list_3))  # длина массива
# print(list_3[3])     # вывод элемента конкретного
# print(list_3[-1])  # вывод последнего элемента

# list_4 = [1, 5]
# print(list_4)
# list_4.append(8)
# print(list_4)
# list_4.append(85)
# print(list_4)

# list_5 = []
# print(list_5)
# for i in range(5):
#     list_5.append(i)
#     print(list_5)

# # Удаление последнего элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)

# # # Удаление конкретного элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.pop(3))
# print(list_1)

# # Удаление конкретного элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# list_1.insert(3, 77)
# print(list_1)

# # # Создание кортежа
# t = ()
# print(type(t))
# t = (1,)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))
# v = tuple(v)
# print(v)
# print(type(v))

# # a = 1    # множественное присваивание
# # b = 2
# # print(a, b)
# # a, b = 1, 2
# # print(a, b)

a, b, c = v
print(a, b, c)

# t = (1, 2, 3, 5,)
# for i in t:
#     print(i)

# t = (1, 2, 3, 5,)
# for i in range(len(t)):
#     print(t[i])

# v = [1, 2, 3, 5]
# v[0] = 2
# print(v)

# Словари
# d = {}
# print(d)
# d = dict()
# print(d)

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

# Словари

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# dictionary[895] = 98998
# print(dictionary)
# print(dictionary['left'])  # ← типы ключей могут отличаться
# print(dictionary['up'])  # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left'])  # ⇐
# # print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left']  # удаление элемента
# print(dictionary)

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
#     # print(item)

# for (k, v) in dictionary.items():  # где k- ключ, v- значение
#     print(v)
# print(dictionary.items())

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue','gray'}
# colors.remove('red')  # удаление
# print(colors)  # {'green', 'blue','gray'}
# # colors.remove('red')  # KeyError: 'red'
# colors.discard('red')  # ok удаляет, если есть, если нет - не ругается
# print(colors)
# colors.clear()
# print(colors)

# q = set()

# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8}
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, объединение
# print(c)
# print(u)

# i = a.intersection(b)
# print(i)  # i = {8, 2, 5} пересечение
# dl = a.difference(b)  # dl = {1, 3} разность
# dr = b.difference(a)  # dr = {13, 21} разность
# q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}
# print(q)

# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

# list_1 = [0 for item in range(5)]
# print(list_1)
# list_2 = [10 for item in range(4)]
# print(list_2)

# Создать список, состоящий из четных чисел от 1 до 100
# список от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)

# list_2 = [i for i in range(1, 101)]
# print(list_2)
# if list_1 == list_2:
#     print('Yes')

# list_3 = [(i, i*i) for i in range(1, 101) if i % 2 == 0]
# print(list_3)

# list_4 = [i*2 for i in range(10) if i % 2 == 0]
# print(list_4)
