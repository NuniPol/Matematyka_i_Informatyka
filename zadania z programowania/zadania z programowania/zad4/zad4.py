from math import gcd

#Zadanie 4.1.
dane1 = [w.strip() for w in open('skrot.txt').readlines()]
lista1 = []
for liczba in dane1:
    if not ('1' in liczba or '3' in liczba or '5' in liczba or '7' in liczba or '9' in liczba):
        lista1.append(int(liczba))
print(len(lista1), max(lista1))

#Zadanie 4.2.
dane2 = [w.strip() for w in open('skrot2.txt').readlines()]
for liczba in dane2:
    liczba_int = int(liczba)
    skrot_lista = [z for z in liczba if z in ['1', '3', '5', '7', '9']]
    skrot_str = ''.join(skrot_lista)
    skrot_int = int(skrot_str)
    if gcd(liczba_int, skrot_int) == 7:
        print(liczba_int)