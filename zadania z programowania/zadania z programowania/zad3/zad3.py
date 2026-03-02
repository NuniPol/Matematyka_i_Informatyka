dane = [w.strip() for w in open('slowa.txt').readlines()]

#Zadanie 3.1.
ile = 0
for s in dane:
    for i in range(len(s) - 2):
        if s[i] == 'k' and s[i + 2] == 't':
            ile += 1
            break
print(ile)

#Zadanie 3.2.
for s in dane:
    for z in s:
        if s.count(z) >= len(s) / 2:
            print(s)
            break