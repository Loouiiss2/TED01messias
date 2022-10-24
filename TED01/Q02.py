#Resposta 02

import random
list=[]

for x in range(30):
    x = random.randing(1,15)
    list.append(x)
    meu_número = int(input("digite um número de 1 a 15: "))
    contador = 0
for x in list:
    if x == meu_número:
        contador += 1
        print(f"escolhi meu némero:{meu-número}. ")
        print(f"meu número repetiu,{contador} vezes. ")
        print(F"números sorteados são: {list}. ")
