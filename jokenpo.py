from random import randint
from time import sleep

game = False
itens = ("Pedra", "Papel", "Tesoura")
opcoes = randint(0, 2)
while (game == False):
    print('''Escolha as opções: 
        [0] Pedra 
        [1] Papel
        [2] Tesoura''')
    jogada = int(input("Qual a sua jogada ? "))
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!!")
    sleep(2)
    print('-=' * 11)
    print(f"O computador jogou: {itens[opcoes]}")
    print(f"O jogador jogou: {itens[jogada]}")
    print('-=' * 11)
    
    #Caso o computador escolha Pedra
    if opcoes == 0:
        if jogada == 1:
            print("O JOGADOR VENCEU!!")
        elif jogada == 2:
            print("O COMPUTADOR VENCEU!!")
        elif jogada == 0:
            print("EMPATE!")
        else:
            print("JOGADA INVÁLIDA")
    
    #Caso o computador escolha Papel
    if opcoes == 1:
        if jogada == 2:
            print("O JOGADOR VENCEU!")
        elif jogada == 0:
            print("O COMPUTADOR VENCEU!")
        elif jogada == 1:
            print("EMPATE!")
        else:
            print("JOGADA INVÁLIDA!")
    
    #Caso o computador escolha Tesoura
    if opcoes == 2:
        if jogada == 0:
            print("O JOGADOR VENCEU!")
        elif jogada == 1:
            print("O COMPUTADOR VENCEU!")
        elif jogada == 2:
            print("EMPATE!")
        else:
            print("JOGADA INVÁLIDA")
    loop = True
    while (loop == True):
        continuar = input("Deseja jogar novamente ? (S/N) => ")
        if continuar == 'S':
            game = False
            loop = False
        elif continuar == 'N':
            game = True
            loop = False
        else:
            print("Digite uma opção válida")
