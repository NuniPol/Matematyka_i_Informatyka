import math

dane = [w.split() for w in open('prostokaty_przyklad.txt').readlines()]
dane = [[int(w[0]), int(w[1])] for w in dane]

#Zadanie 2.1.
max_pole = -math.inf #Liczba nieskończenie mała
min_pole = math.inf #Liczba nieskończenie duża
for p in dane:
    pole = p[0] * p[1]
    if pole > max_pole:
        max_pole = pole
    if pole < min_pole:
        min_pole = pole

print(max_pole, min_pole)

#Zadanie 2.2.
obwody = set()

for p in dane:
    obw = 2 * p[0] + 2 * p[1]
    obwody.add(obw)
print(len(obwody))