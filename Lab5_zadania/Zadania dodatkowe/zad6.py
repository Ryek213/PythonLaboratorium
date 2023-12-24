def nwd(a, b):
    while True:
        if a > b:
            a = a - b
        else:
            b = b - a

        if a == b:
            break

    return a


print(nwd(12, 27))
print(nwd(3, 9))
print(nwd(827, 21))
print(nwd(95, 143))
print(nwd(34, 85))
