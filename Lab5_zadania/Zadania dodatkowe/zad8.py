def czy_anagram(a, b):
    a_pom = sorted(list(a.lower()))
    b_pom = sorted(list(b.lower()))

    i = 0
    while i < len(a_pom):
        if not (ord(a_pom[i]) in range(ord('a'), ord('z')+1)):
            a_pom.remove(a_pom[i])
        else:
            i += 1

    i = 0
    while i < len(b_pom):
        if not (ord(b_pom[i]) in range(ord('a'), ord('z') + 1)):
            b_pom.remove(b_pom[i])
        else:
            i += 1

    if a_pom == b_pom:
        print(f'Ciągi znaków: "{a}" oraz "{b}" są anagramami')
    else:
        print(f'Ciągi znaków: "{a}" oraz "{b}" nie są anagramami')


a1 = input("Podaj pierwszy tekst: ")
b1 = input("Podaj drugi tekst: ")
czy_anagram(a1, b1)
