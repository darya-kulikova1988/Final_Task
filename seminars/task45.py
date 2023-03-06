# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз(перестановка чисел новую пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

k = int(input("Введите число k: "))
list_divide = []
list_sum_divide = []
final = []
for i in range(1, k):
    for divide in range(1, i):
        if i % divide == 0:
            list_divide.append(divide)
    list_sum_divide.append(sum(list_divide))
    # print(list_divide)
    list_divide = []
# print(list_sum_divide)
# print(len(list_sum_divide))
for index in range(1, len(list_sum_divide)):
    for sum in range(1, len(list_sum_divide)):
        if index == list_sum_divide[sum-1] and sum == list_sum_divide[index-1] and index != list_sum_divide[index-1]:
            final.append(index)
print(*final)
