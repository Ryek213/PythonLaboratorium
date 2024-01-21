import keyword

slowa = ["for", "print", "break", "done", "bad"]

for word in slowa:
    if keyword.iskeyword(word):
        print(f'Słowo "{word}" jest słowem kluczowym')
    else:
        print(f'Słowo "{word}" nie jest słowem kluczowym')
