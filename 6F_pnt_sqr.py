# Point in a square yes or no
# /\
# \/  square with side sqrt 2

x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1 and (abs(x) + abs(y)) <= 1


if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
