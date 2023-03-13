# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def simple_n(n: int):
#     for i in range(2, n//2):
#         if n % i == 0:
#             print(f'число {n} не является простым')
#         print(f'число {n} является простым')


# n = int(input("Введите число n: "))
# simple_n(n)


def simple_n(n: int):
    for i in range(2, n//2):
        if n % i == 0:
            return False
        return True


q = int(input("Введите число n: "))
print(simple_n(q))

# i = 2
# while i < n:
#     if n % 1 == 0 and n % n == 0 and n % i == 0:
#         a = 'no'
#     else:
#         a = 'yes'
#     i += 1
# if a == 'no':
#     print(f'число {n} не является простым')
# else:
#     print(f'число {n} является простым')
