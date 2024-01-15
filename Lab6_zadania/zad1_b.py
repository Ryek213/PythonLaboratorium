import random


roczniki = list()
for i in range(1990, 2007):
    roczniki.append(i)

print(f"Szczęśliwy rocznik: {random.choice(roczniki)}")
