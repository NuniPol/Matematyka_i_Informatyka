dane = [w.strip() for w in open('bin.txt').readlines()]

#Zadanie 7.1.
ile = 0
for liczba2 in dane:
    liczba_blokow = 1
    for i in range(len(liczba2) - 1):
        if liczba2[i] != liczba2[i + 1]:
            liczba_blokow += 1
    if liczba_blokow <= 2:
        ile += 1
print(ile)

#Zadanie 7.2.
max_liczba2 = ''
max_liczba10 = 0

for liczba2 in dane:
    liczba10 = int(liczba2, 2)
    if liczba10 > max_liczba10:
        max_liczba10 = liczba10
        max_liczba2 = liczba2
print(max_liczba2)