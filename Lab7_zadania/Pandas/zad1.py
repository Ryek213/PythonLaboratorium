import numpy as np
import pandas as pd

data = {'Nr_Albumu': [12345, 54123, 98745, 64985],
        'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'Nazwisko': ['Kowalska', 'Nowak', 'Wójcik', 'Ferenc'],
        'Ocena': [4.0, 5.0, 3.5, 4.0],
        'Wiek': [18, 23, 20, 20]}

df = pd.DataFrame(data)

# a
print("a:")
print(df[df['Ocena'] > 4])
print('\n')

# b
print("b:")
print(df.sort_values('Ocena'))
print('\n')

# c
print("c:")
dfgOcena = df.groupby('Ocena')
for ocena in dfgOcena.first().index:
    suma = 0
    ile = 0
    for index in dfgOcena.get_group(ocena).index:
        suma += df.loc[index, "Wiek"]
        ile += 1
    print(f"Średnia wieku dla oceny {ocena}: {suma/ile}")
print('\n')

# d
print("d:")
poprawa = {'Nr_Albumu': [12345, 98745, 64985],
        'Ocena_poprawa': [4.5, 4.0, 4.0]}
df_poprawa = pd.DataFrame(poprawa)
print(df_poprawa)

df = df.join(df_poprawa.set_index("Nr_Albumu"), on="Nr_Albumu")
print(df)
print('\n')

# e
print("e:")
df.to_csv("df.csv", index = False)
print("Zapisano DataFrame df do pliku df.csv")
print('\n')

# f
print("f:")
df1 = pd.read_csv("df.csv")
print("Wczytano plik df.csv do zmiennej df1")
print(df1)

if len(df1.compare(df).index) == 0:
    print("Ramki danych są takie same")
else:
    print("Ramki danych różnią się")
    df1.compare(df)
print('\n')

# g
print("g:")

df.loc[len(df)] = [54647, "Maksymilian", "Kowalski", 5.0, 30, np.NaN]
print(f"Nowy student:\n {df.loc[4]}")
print('\n')

# h
print("h:")
print("Unikalne wartości:", df["Ocena"].unique().tolist())
print('\n')

# i
print("i:")
print(f"Liczba studentów z oceną 5.0: {len(df[df['Ocena'] == 5])}")