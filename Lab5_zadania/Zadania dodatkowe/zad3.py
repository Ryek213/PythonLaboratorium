def rownanie_kwadratowe(a, b=0, c=0):
    if a == 0:
        print("To nie jest równanie kwadratowe!! a musi być różne od 0!!!")
        return
    elif not isinstance(a, int) and not isinstance(a, float):
        print("a nie jest liczbą!")
        return
    elif not isinstance(b, int) and not isinstance(b, float):
        print("b nie jest liczbą!")
        return
    elif not isinstance(c, int) and not isinstance(c, float):
        print("c nie jest liczbą!")
        return

    delta = b**2 - 4 * a * c

    if delta < 0:
        return ()
    elif delta == 0:
        return -b / (2 * a),
    elif delta > 0:
        return (-b * delta ** 0.5) / (2 * a), (-b * delta ** 0.5) / (2 * a)


print(rownanie_kwadratowe(1, 2, 3))
print(rownanie_kwadratowe(1, 4, 4))
print(rownanie_kwadratowe(1, 4, 3))
print(rownanie_kwadratowe(4))
print(rownanie_kwadratowe(0))
print(rownanie_kwadratowe("a"))
# noinspection PyTypeChecker
print(rownanie_kwadratowe(5, "4"))
# noinspection PyTypeChecker
print(rownanie_kwadratowe(4, 2, "h"))
