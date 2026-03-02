dane = [int(w) for w in open('liczby.txt').readlines()]

#Zadanie 9.1.
for liczba in dane:
    liczba_str = str(liczba)
    liczba_list = list(liczba_str)
    liczba_list.reverse()
    liczba_odwr_str = ''.join(liczba_list)
    liczba_odwr = int(liczba_odwr_str)
    if liczba_odwr % 17 == 0:
        print(liczba_odwr)

#Zadanie 9.2.
max_liczba = 0
max_roznica_abs = 0
for liczba in dane:
    liczba_str = str(liczba)
    liczba_list = list(liczba_str)
    liczba_list.reverse()
    liczba_odwr_str = ''.join(liczba_list)
    liczba_odwr = int(liczba_odwr_str)
    roznica_abs = abs(liczba - liczba_odwr)
    if roznica_abs > max_roznica_abs:
        max_roznica_abs = roznica_abs
        max_liczba = liczba

print(max_liczba, max_roznica_abs)

#Zadanie 9.3.
zbior = set()

for liczba in dane:
    zbior.add(liczba)

ile2 = 0
ile3 = 0

for liczba in zbior:
    if dane.count(liczba) == 2:
        ile2 += 1
    elif dane.count(liczba) == 3:
        ile3 += 1

print(len(zbior), ile2, ile3)