tupla1=(1,2,3,"cuatro",[10,20])
tupla2=9,8,7
print(len(tupla1))
print(tupla2[1])
print(tupla2[2:4])
tupla1=tupla1*3
print(tupla1)
tupla1+=(100,)
print(tupla1)

lista=[7,7,7,7,7,]
lista=tuple(lista)
print(lista)


lista10=[10 for i in range(10)]

lista10=[round(random.random()*100)for i in range(10)]
print(lista)



import random
tup=tuple(round(random.random()*100)for i in range(10))
print(tup)

import random
tam =round(random.randint(10,25))
tup = tuple(round(random.random()*100)for i in range(tam))
print (tup)
for i in tup:
    cont=0
    for j in range(i):
        if i%j==0:
            cont+=1
    if cont==1:
        print ("primo")
