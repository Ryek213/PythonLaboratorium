import matplotlib.pyplot as plt

oceny = [4.0, 3.0, 3.5, 3.5, 3.5, 4.0, 5.0, 5.0, 4.5, 4.0, 4.0, 3.5, 3.0, 3.0, 3.0, 3.5, 2.0, 2.0]

plt.hist(oceny, bins=(2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0), edgecolor="black")
plt.xlabel("Oceny")
plt.ylabel("Liczba studentów")
plt.show()
