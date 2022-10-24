#Resposta 01
clubes= []

for time in range(10):
    clubs.append(input("digite os clubes: "))

    print("digite o nome de seu time para conferir se está na lista. ")
    print("*"*26)

    x = input("verifique aqui: ")
    if x in clubs:
        print(f"achei o time {x} foi selecionado. ")
    else:
        print(f"não encontrei o {x}, não foi selecionado. ")