import random

x = set()
a = random.randint(3, 7)
print("a:", a)
while len(x) < a:
    x.add(random.randint(0, 10))
print("X:", x)

y = set()
b = random.randint(3, 7)
print("b:", b)
while len(y) < b:
    y.add(random.randint(0, 10))
print("Y:", y)


# Ćwiczenie a
if 5 in x:
    print("Zbiór X zawiera liczbę 5")
else:
    print("Zbiór X nie zawiera liczby 5")

# Ćwiczenie b
flaga = True
for i in x:
    if not (i in y):
        flaga = False
        break

if flaga:
    print("X jest podzbiorem Y")
else:
    print("X nie jest podzbiorem Y")

# Ćwiczenie c
flaga = True
for i in y:
    if not (i in x):
        flaga = False
        break

if flaga:
    print("Y jest podzbiorem X")
else:
    print("Y nie jest podzbiorem X")

# Ćwiczenie d
flaga = True
for i in y:
    if not (i in x):
        flaga = False
        break

if flaga:
    print("X jest nadzbiorem Y")
else:
    print("X nie jest nadzbiorem Y")

# Ćwiczenie e
flaga = True
for i in x:
    if not (i in y):
        flaga = False
        break

if flaga:
    print("Y jest nadzbiorem X")
else:
    print("Y nie jest nadzbiorem X")

# Ćwiczenie f
xy_sum = set()
for i in x:
    xy_sum.add(i)
for i in y:
    xy_sum.add(i)

print(f"Suma X i Y: {xy_sum}")

# Ćwiczenie g
xy_diff = set()
for i in x:
    xy_diff.add(i)
for i in y:
    if i in x:
        xy_diff.remove(i)

print(f"Różnica X i Y: {xy_diff}")

# Ćwiczenie h
yx_diff = set()
for i in y:
    yx_diff.add(i)
for i in x:
    if i in y:
        yx_diff.remove(i)

print(f"Różnica Y i X: {yx_diff}")

# Ćwiczenie i
xy_prod = set()
for i in x:
    for k in y:
        if i == k:
            xy_prod.add(i)

print(f"Iloczyn X i Y: {xy_prod}")

# Ćwiczenie j
xy_sym_diff = set()
for i in xy_diff:
    xy_sym_diff.add(i)
for i in yx_diff:
    xy_sym_diff.add(i)

print(f"Różnica symetryczna X i Y: {xy_sym_diff}")

# Ćwiczenie k
s = int()
for i in x:
    s = max(s, i)
for i in y:
    s = max(s, i)
print(f"Najwyższa liczba z obu zbiorów: {s}")

# Ćwiczenie l
y.add(x.pop())
print("\nĆwiczenie l:")
print("X:", x)
print("Y:", y)

# Ćwiczenie m
for i in x:
    y.add(i)
print("\nĆwiczenie m:")
print("X:", x)
print("Y:", y)

# Ćwiczenie n
for i in range(len(x)):
    x.pop()
for i in range(len(y)):
    y.pop()
print("\nĆwiczenie n:")
print("X:", x)
print("Y:", y)
