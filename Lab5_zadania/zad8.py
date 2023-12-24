def potegowanie(a, n):
    if n > 1:
        return a * potegowanie(a, n-1)
    else:
        return a


print(potegowanie(2, 10))
print(potegowanie(3, 4))
