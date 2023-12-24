def pole_trojkata(a, b, c):
    if a <= 0:
        return "Trojkat powinien miec boki o dodatnich dlugosciach!!"
    if b <= 0:
        return "Trojkat powinien miec boki o dodatnich dlugosciach!!"
    if c <= 0:
        return "Trojkat powinien miec boki o dodatnich dlugosciach!!"
    if a + b < c or a + c < b or b + c < 0:
        return "Nie można stworzyć trójkąta z tych boków"

    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5


print(pole_trojkata(3, 4, 5))
print(pole_trojkata(1, 4, 0))
print(pole_trojkata(-5, 6, 10))
print(pole_trojkata(10, 10, 10))
print(pole_trojkata(1, 3, 10))
