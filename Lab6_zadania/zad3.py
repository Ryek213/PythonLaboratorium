import time

czas = int(input("Podaj czas w sekundach: "))

while czas >= 0:
    print(czas)
    czas = czas - 1
    time.sleep(1)
