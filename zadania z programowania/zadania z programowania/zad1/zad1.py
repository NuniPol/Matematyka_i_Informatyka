dane = [int(w) for w in open('liczby.txt').readlines()]

#Zadanie 1.1.
kwadraty = [i ** 2 for i in range(1, 100)]

ile = 0

for i in dane:
    if i in kwadraty:
        ile += 1
        if ile == 1:
            print(i)

print(ile)

#Zadanie 1.2.
max_l_dziel = 0
max_liczba = 0
for i in dane:
    l_dziel = 0
    for j in range(1, i + 1):
        if i % j == 0:
            l_dziel += 1
    if l_dziel > max_l_dziel:
        max_l_dziel = l_dziel
        max_liczba = i

print(max_liczba, max_l_dziel)
