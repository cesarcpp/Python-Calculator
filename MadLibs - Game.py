#Importando os modulos
from tkinter import *

#Criando um Layout
root = Tk()
root.geometry('300x300')
root.title('MadLibs Generator - Game')
Label(root, text= 'Gerador de MadLibs \n Se divirta!' , font='arial 20 bold').pack()
Label(root, text= 'Clique em qualquer um:' , font='arial 15 bold').place(x=40, y=80)

#Definindo as funções de cada MadLib
def madlib1():
    animal= input('Digite o nome de um animal: ')
    profissão= input('Digite o nome de uma profissão: ')
    roupa= input('Escolha o que o personagem está vestindo: ')
    sentimento= input('Digite o sentimento que o personagem está tendo: ')
    nome= input('Digite o nome do companheiro de aventura: ')
    comida= input('Digite o que os personagens comeram: ')
    print(nome + ' e eu estavamos viajando para Nova York a procura de um trabalho como ' + profissão + ''' até que durante a viagem avistamos um/uma ''' + animal + ''' ficamos perplexos só estavamos usando ''' + roupa + ''' e não tinhamos nada a oferecer além de ''' + comida +''' sentimos ''' + sentimento + ''' mas tudo correu bem! ''')

def madlib2():
    time= input('Insira o nome do time de futebol: ')
    ano= int(input('Insira o ano de fundação do clube: '))
    titulos= int(input('Insira o numero de titulos que o clube teve: '))
    jogador= input('Insira o nome do principal jogador do clube: ')
    print('O ' + time + ' fundado no ano de ' + str(ano) + ' teve ao todo ' + str(titulos) + ' titulos em sua história, conquistados graças ao grande jogador ' + jogador)

def madlib3():
    nome= input('Insira o nome do seu jogador: ')
    base= input('Insira a base que ele começou no futebol: ')
    primeiro_time= input('Insira a primeiro time da carreira do seu jogador: ')
    auge= input('Insira o time que ele teve seu age na carreira: ')
    ultimo_time= input('Insira o time onde ele encerrou a carreira: ')
    gols= int(input('Insira a quantidade de gols que ele teve na carreira: '))
    assist= int(input('Insira a quantidade de assistências que ele teve na carreira: '))
    titulos= int(input('Insira a quantidade de titulos que ele teve na carreira: '))
    print('O jogador ' + nome + ' começou na base do ' + base + ' após um tempo, sua estreia profissional foi pelo ' + primeiro_time +
          ''' ao rodar o mundo do futebol o ''' + nome + ' teve seu auge no poderoso ' + auge +
          ''' e após anos em alto nivel, decidiu encerrar sua carreira no ''' + ultimo_time + ' sua carreira teve ao todo: ' + str(gols) + ' Gols; '
          + str(assist) + ' Assistências e conquistou ' + str(titulos)+ ' Titulos.')

#Definindo os botões para rodar o MadLibs
Button(root, text='Viagem Louca', font ='arial 15', command = madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text='Time de Futebol', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=60, y=180)
Button(root, text='Carreira de Futebol', font ='arial 15', command = madlib3, bg = 'ghost white').place(x=60, y=240)

#Inserindo um looping para rodar o programa
root.mainloop()
