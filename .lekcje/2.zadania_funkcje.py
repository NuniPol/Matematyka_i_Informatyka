#Zadanie 0.3
#a
def dodawanie_wektorów(u,v):
    wynikiA=[]
    for i in range(len(u)):
        wynikiA.append(u[i]+v[i])
    return wynikiA

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

#zadanie 0.3
#b
def mnożenie_wektorów(u,v):
    wynikiB=[]
    for i in range(len(u)):
        wynikiB.append(u[i]*v[i])
    return wynikiB
#c
def mnożenie_wektora(v,k):
    wynikiC=[]
    for i in range(len(v)):
        wynikiC.append(v[i]*k)
    return wynikiC

#zadanie 2.2
def jaki_trojkat(a,b,c):
    lista=[a,b,c]
    lista.sort()
    if lista[0]**2+lista[1]**2==lista[2]**2:
        print("prostokątny")
    elif lista[0]**2+lista[1]**2>lista[2]**2:
        print("ostrokątny")
    else:
        print("szerokokątny")
