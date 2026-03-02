dane = [w.strip() for w in open('slowa.txt').readlines()]

#Zadanie 8.1.
for s in dane:
    if s.count('w') == s.count('k'):
        print(s)

#Zadanie 8.2.
max_slowo = 0
max_l_wakacje = 0
for s in dane:
    ile_w = s.count('w')
    ile_a = s.count('a')
    ile_k = s.count('k')
    ile_c = s.count('c')
    ile_j = s.count('j')
    ile_e = s.count('e')

    l_wakacje = min([ile_w, ile_a // 2, ile_k, ile_c, ile_j, ile_e])

    if l_wakacje > max_l_wakacje:
        max_l_wakacje = l_wakacje
        max_slowo = s

print(max_slowo)