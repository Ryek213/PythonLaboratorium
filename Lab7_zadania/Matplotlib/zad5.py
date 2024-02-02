import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

oceny = {
    "Numer_albumu": ["w64354", "w12345", "w54132", "w51241", "w51321", "w1234", "w12435", "w5112", "w8523"],
    "Zerowy_termin": [4.0, 3.0, 3.5, 4.0, 2.0, 2.0, 5.0, 4.5, 3.0],
    "Pierwszy_termin": [np.NaN, 3.5, 4.0, 4.0, 3.0, 2.0, np.NaN, np.NaN, 3.0],
    "Drugi_termin": [np.NaN, np.NaN, np.NaN, np.NaN, 3.5, 2.0, np.NaN, np.NaN, np.NaN]
}

oceny = pd.DataFrame(oceny)
print(oceny)

fig, ax = plt.subplots()
X_axis = np.arange(len(oceny["Numer_albumu"]))
ax.bar(X_axis - 0.25, oceny["Zerowy_termin"], 0.25, label="Zerowy termin")
ax.bar(X_axis, oceny["Pierwszy_termin"], 0.25, label="Pierwszy termin")
ax.bar(X_axis + 0.25, oceny["Drugi_termin"], 0.25, label="Drugi termin")

plt.ylim(1.5, 5)
plt.yticks(np.arange(2, 5.5, 0.5))
plt.xticks(X_axis, oceny["Numer_albumu"])
ax.grid(axis="y")
plt.legend()

plt.show()
