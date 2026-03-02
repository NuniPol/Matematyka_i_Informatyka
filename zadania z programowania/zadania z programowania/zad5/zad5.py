dane = [w.split() for w in open('liczby.txt').readlines()]
dane = [list(map(int, w)) for w in dane]

#Zadanie 5.1.
ile = 0
for liczba1 in dane[0]:
    for liczba2 in dane[1]:
        if liczba2 % liczba1 == 0:
            ile += 1
            break
print(ile)

#Zadanie 5.2.
pierwszy_wiersz = dane[0]
pierwszy_wiersz.sort()
pierwszy_wiersz.reverse()
print(pierwszy_wiersz[100])