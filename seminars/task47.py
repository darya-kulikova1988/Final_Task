# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok
# def function(x):
#     if x % 2 == 0:
#         return x
#     else:
#         return ' '


# arg1 = function
# arg2 = [1, 2, 3, 4]
# func = map(arg1, arg2)
# print(list(func))


values = [1, 23, 42, 'asdfg']
def transformation(x): return x
# transformation = lambda x:x

transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
