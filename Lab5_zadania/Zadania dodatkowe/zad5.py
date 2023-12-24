def wspolne_wartosci(a, b):
    lista = list()

    for i in a:
        for k in b:
            if i == k:
                lista.append(i)

    return lista


print(wspolne_wartosci((4, 6, 2, 12, "a", "bf"), (4, 2, "a", "c", 54)))
