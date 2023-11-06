print("Wprowadź trzy liczby:")
x = float(input("1.: "))
y = float(input("2.: "))
z = float(input("3.: "))

if x > y:
    if x >= z:
        if y > z:
            print(z, y, x)
        else:
            print(y, z, x)
    else:
        print(y, x, z)
else:
    if y >= z:
        if x > z:
            print(z, x, y)
        else:
            print(x, z, y)
    else:
        print(x, y, z)