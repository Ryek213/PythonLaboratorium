import matplotlib.pyplot as plt

kategorie = ["Mleko", "Ryż", "Oranżada", "Makaron"]
wartosci = [23, 40, 72, 35]

plt.pie(wartosci, labels=kategorie, autopct='%.2f%%')
plt.show()
