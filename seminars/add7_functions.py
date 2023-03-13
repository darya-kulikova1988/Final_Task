# # import random
# # my_string = '51551532132131'
# # my_string = list(my_string)
# # my_string = [int(x) for x in my_string if int(x) % 2 == 0]
# # print(my_string)
# # # print(sum(my_string))

# # my_string = list(map(int, my_string))
# # my_string = list(map(lambda x: int(x), my_string))
# # print(my_string)


# # def is_odd(num: int | float) -> str | bool:  # тайп хиддинг
# #     if num % 2 == 0:
# #         return True
# #     else:
# #         return 'Нечетное'


# # my_string = list(filter(is_odd, my_string))
# # # my_string = list(filter(lambda x: x % 2 == 0, my_string))
# # print(my_string)

# # print(sum(my_string))

# # for i in range(len(my_string)):
# #     my_string[i] = int(my_string[i])
# # print(my_string)
# # print(sum(my_string))
# # my_list = [random.randint(0, 10) for _ in range(10)]
# # print(my_list)


# # def is_odd(lst: list) -> list:
# #     new_list = [x for x in lst if int(x) % 2 == 0]
# #     new_list = list(filter(lambda x: x % 2 != 0, lst))
# #     return new_list


# my_string1 = 'fdbbc'
# my_string1 = list(my_string1)
# print(my_string1)

# for i, item in enumerate(my_string1):
#     print(f'{i+1}.{item}')

# # for i in range(len(my_string1)):
# #     print(f'{i}.{my_string1[i]}')


# def func(num: int):
#     num1 = num**2
#     num2 = num-2
#     return num1, num2


# # print(func(5))
# power, minus = func(5)
# print(power)
# print(minus)

# ZIP
my_string1 = 'fdbbc'
my_string2 = [i for i in range(10)]
my_string1 = list(my_string1)
print(my_string1)
print(my_string2)

new_string = list(zip(my_string1, my_string2))
print(new_string)

new_string = []
for i, item in enumerate(my_string1):
    new_string.append((my_string1[i], my_string2[i]))
print(new_string)

# LAMBDA - анонимная однострочная функция, которая что-то возвращает (одноразовая, в памяти не остается )
operation = {'+': lambda x, y: x+y,
             '-': lambda x, y: x-y}
string = '3+2'
string = list(string)
print(string)
for i, item in enumerate(string):
    if string[i] in ['+', '-']:
        print(operation.get(string[i])(int(string[i-1]), int(string[i+1])))
