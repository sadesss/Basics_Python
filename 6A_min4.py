# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
# которая не содержит инструкции if, а использует стандартную функцию min.
# Считайте четыре целых числа и выведите их минимум.

a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a, b, c, d):
    res = min(a, b)
    res = min(res, c)
    res = min(res, d)
    return res


print(min4(a, b, c, d))
