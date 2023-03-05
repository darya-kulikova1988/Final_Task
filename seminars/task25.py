# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

import string
import random
# string = str.upper('a a a b c a a d c d d')
# print(string)
# new_string = (string.split())
# result = {}
# for i in new_string:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1


# size = int(input('Введите размер строки: '))
# new_string = ''.join([random.choice(string.ascii_letters)
#                      for _ in range(size)])
# print(new_string)
# counter = {}
# for letter in new_string:
#     counter[letter] = counter.get(letter, 0) + 1
# print(counter)

# for key, values in counter.items():
#     if values > 1:
#         print(key, end='')


# size = int(input('Введите размер строки: '))
# new_string = ''.join([random.choice(string.ascii_letters)
#                      for _ in range(size)])
new_string = str.upper('a a a b c a a d c d d')
print(new_string)
counter = {}
for letter in new_string:
    count = counter.get(letter, 0)
    print(count, end=' ')
    counter[letter] = count + 1
    # if count == 1:
    #     print(letter, end=' ')
    # elif count > 1:
    #     print(f'{letter}_{count}', end=' ')
