dane=open("calkowite.txt","r")
dany=dane.read()
i=0
lista=[]
rob=""
while i<len(dany):
   if dany[i]!=0:
      rob+=dany[i]
   else:
      lista.append(rob)
   i+=1
   rob=""
lista.sort()
lista.reverse()
print(lista)