# Напишите программу, которая выводит чётные числа из заданного списка
# и останавливается, если встречает число 237

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(*[i for i in my_list[:my_list.index(237)] if i % 2 == 0] if 237 in my_list
      else [i for i in my_list if i % 2 == 0])


# print(my_list.index(237))

# for elem in my_list:
#     if elem % 2 == 0:
#         print(elem, end=' ')
#     elif elem == 237:
#         break
