dane = [int(w) for w in open('liczby.txt').readlines()]

ile = 0
pierwsza = 0
for liczba in dane:
    liczba_str = str(liczba)
    if liczba_str[0] == liczba_str[-1]:
        ile += 1
        if ile == 1:
            pierwsza = liczba
print(ile, pierwsza)