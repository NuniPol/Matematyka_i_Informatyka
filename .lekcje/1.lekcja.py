#procedura-funkcja niezwracająca wartości
def czesc50():
    for i in range(50):
        print("cześć")
#n-parametr wejściowy
def czesc(n):
    for i in range(n):
        print("Cześć")
#"a" i "b"-parametry wejsciowe
def dodadawanie(a,b):
    print(a+b)
#dane o czlowieku
#d[0] - imie
#d[1] - nazwisko
#d[2] - wiek
def przywitaj_sie(dane):
    print(f"Witaj {dane[0]} {dane[1]} masz {dane[2]}")
dane=["Janusz",'kowal',45]
#funkcje zwracające wartość
def Pp(a):
    return a*a
def Psb(a,b):
    return a*b
def Pc(a,b):
    return (Pp(a)*2+Psb(a,b)*4)