dane = [w.strip() for w in open('anagram.txt').readlines()]

#Zadanie 6.1.
ile_z = 0
ile_pz = 0
for liczba2 in dane:
    if liczba2.count('1') == liczba2.count('0'):
        ile_z += 1
    elif liczba2.count('1') == liczba2.count('0') + 1 or liczba2.count('1') + 1 == liczba2.count('0'):
        ile_pz += 1
print(ile_z, ile_pz)

#Zadanie 6.2.
ile_bez_zera = 0
max_s_r_c = 0
max_l = 0

for liczba2 in dane:
    liczba10 = int(liczba2, 2)
    liczba10_str = str(liczba10)

    if liczba10_str.count('0') == 0:
        ile_bez_zera += 1

    cyfry = [int(c) for c in liczba10_str]
    rozne_cyfry = set(cyfry)
    suma_r_cyfr = sum(rozne_cyfry)
    if suma_r_cyfr > max_s_r_c:
        max_s_r_c = suma_r_cyfr
        max_l = liczba10

print(ile_bez_zera, max_l)

