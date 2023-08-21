import random

def jogo_tesouro():
    row1 = ["", "", ""]
    row2 = ["", "", ""]
    row3 = ["", "", ""]
    map_preenchido = [row1, row2, row3]
    mapa = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(f"{row1}\n{row2}\n{row3}")
    
    numero = random.randint(1, 9)
    
    if numero <= 3:
        mapa[0][numero - 1] = "X"
    elif numero <= 6 and numero >3:
        mapa[1][numero - 4] = "X"
    else:
        mapa[2][numero - 7] = "X"
        
    while True:
        escolha = int(input("Escolha um espaço para procurar o tesouro de 1 a 9: "))
        
        if escolha <= 3:
            if mapa[0][escolha - 1] == "X":
                print("Parabéns, você encontrou o tesouro!")
                break
            elif map_preenchido[0][escolha - 1] == "M":
                print("Você já procurou ai pirata preguiçoso!")
            map_preenchido[0][escolha - 1] = "M"
        elif escolha <= 6 and escolha > 3:
            if mapa[1][escolha - 4] == "X":
                print("Parabéns, você encontrou o tesouro!")
                break
            elif map_preenchido[1][escolha - 4] == "M":
                print("Você já procurou ai pirata preguiçoso!")
            map_preenchido[1][escolha - 4] = "M"
        else:
            if mapa[2][escolha - 7] == "X":
                print("Parabéns, você encontrou o tesouro!")
                break
            elif map_preenchido[2][escolha - 7] == "M":
                print("Você já procurou ai pirata preguiçoso!")
            map_preenchido[2][escolha - 7] = "M"
        
        print(f"{map_preenchido[0]}\n{map_preenchido[1]}\n{map_preenchido[2]}" + "\n")

jogo_tesouro()

