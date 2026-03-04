#Zadanie 0.3
#a
def dodawanie_wektorów(u,v):
    wyniki=[]
    for i in range(len(u)):
        wyniki.append(u[i]+v[i])
    return wyniki

print(dodawanie_wektorów([3,2,4], [-4,7,-1]))

#zadanie 2.1
def czyanagramy1(a,b):
    lista_a = list(a)
    lista_b = list(b)
    lista_a.sort()
    lista_b.sort()
    if lista_a == lista_b:
        return True
    else:
        return False

def czyanagramy2(a,b):
    return sorted(a) == sorted(b)

czyanagramy3=lambda a,b:sorted(a) == sorted(b)

