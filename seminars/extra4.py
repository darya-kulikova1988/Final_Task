# Отсортируйте словарь по значению в порядке возрастания и убывания.
# import random
# my_dict = {i: random.randint(1, 10) for i in range(1, 5)}
# print(my_dict)


# sorted_list = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# print(sorted_list)

# sorted_list2 = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
# print(sorted_list2)

new_dict = {'Иванов': [34, 100, 3], 'Федоров': [40, 150, 5]}
print([elem for elem in new_dict.items()])
sorted_dict = dict(
    sorted(new_dict.items(), key=lambda x: x[1][2], reverse=True))
print(sorted_dict)
sorted_dict2 = sorted(new_dict.items(), key=lambda x: x[1][2], reverse=True)
print(sorted_dict2)
print([elem[1][0] for elem in sorted_dict2])
print(*[(elem[0], elem[1][0]) for elem in sorted(
    new_dict.items(), key=lambda x: x[1][2], reverse=True)])
