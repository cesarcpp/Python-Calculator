import random

escolha = False
print("Olá, bem vindo ao jogo")
nome = input("Qual o seu nome? ")
print()
print("Que bom ter você aqui, " + nome)
print()
print(nome + " consegue adivinhar um número de 0 a 10?")
while (escolha == False):
    number = random.randint(0,10)
    N = int(input("Digite o número que você pensou: "))
    print()
    if (N == number):
        print("Você acertou! Parabéns")
        print()
        new = input("Quer jogar novamente ? (S/N) ")
        if (new == 'N'):
            escolha = True
            print("Obrigado por Jogar!")
        else:
            escolhe = False
    else:
        print("Você errou, o número era " + str(number))
        tent = input("Quer tentar novamente ? (S/N) ")
        if (tent == 'N'):
            escolha = True
            print("Obrigado por Jogar!")
        else:
            escolha = False
