# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр треугольника
# по координатам трех его вершин.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.50


a = distance(x1, y1, x2, y2)
b = distance(x1, y1, x3, y3)
c = distance(x3, y3, x2, y2)

print(format(a + b + c, ".6f"))
