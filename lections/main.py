# //
# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c+'89')
# print(type(c))

# //
# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))


# //
# a = 5.56566
# b = 6.515151
# print(round(a*b, 2))
# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 3 < 10
# print(a)

# //
# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i+1
# else:
#     print('Пожалуй')
#     print('хватит ')
# print(i)

# //
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n//2:
#         print(n)
#         flag = False
#     i += 1


# //
# for i in 1, -2, 3, 14, 5:
#     print(i)

# //
# r = range(1, 10, 2)
# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)

# a = 'qwerty'
# print(a[2])


# //
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(4):
#         line += "+"
#     print(line)

# //
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text))
# print(text.upper())
# print(text.lower())
# print(text.replace('ещё', 'ЕЩЁ'))
# print('ещё' in text)
print(text[len(text)-1])
print(text[-1])
print(text[:])  # вывод всех символов
print(text[:2])  # символы с индексами до 2
print(text[20:])  # вывод до конца
print(text[20:30])  # вывод с указанного элемента до указанного, не включая
print(text[0:len(text):6])  # вывод каждого 6-го элемента (с шагом 6)
print(text[::6])  # то же самое
text = text[2:9]+text[-1]+text[2]
print(text)
