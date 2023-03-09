# def f(x):
#     return x*x


# a = f
# print(a(5))  # переименовали функцию f
# print(f(4))
# # print(f(5))
# # print(type(f))


# def calk1(a, b):
#     return a+b

# calk1=lambda a,b: a+b

# # def calk2(a, b):
# #     return a*b


# def math(op, x, y):
#     print(op(x, y))

# # math(calk1, 5, 10)


# # math(calk1, 5, 10)
# # math(calk2, 5, 10)

# # calk1=lambda a,b:a+b
# # def calk1(a, b):
# #     return a+b
# math(lambda a, b: a+b, 5, 45)

# math(calk1, 5, 45)

# a = [1, 2, 3, 5, 8, 15, 23, 38]
# b = list()
# for elem in a:
#     if elem % 2 == 0:
#         b.append((elem, elem*elem))
# print(b)


# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)


# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# data = '556 555 544 66 2 144 2'
# # print(data)
# # data = data.split()
# # print(data)

# data = list(map(int, data.split()))
# print(data)


# функция фильтра

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)

# colors = ['red', '7', 'blue']
# data = open('file.txt', 'a')  # здесь указываем режим, в котором будем работать
# data.writelines(colors)  # разделителей не будет
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')
# print(56)

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
