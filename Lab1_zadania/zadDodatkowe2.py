import math

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

p = (a + b + c)/2

pole = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"Pole tego trójkąta jest równe: {pole}")
