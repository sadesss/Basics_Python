# Дано натуральное число n>1. Проверьте, является ли оно простым. Сложность - корень из n.
n = int(input())


def IsPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if IsPrime(n):
    print("YES")
else:
    print("NO")
