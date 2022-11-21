#Calculadora_Update

print('Calculadora Amiga')
print()

print('Olá, meu caro amigo/ga, como você está?')
des = int(input('Selecione (1 - Bem, 2 - Mais ou menos, 3 - Mal): '))
while (des != 1) and (des != 2) and (des != 3):
    print('Escolha uma opção válida')
    des = int(input('Selecione (1 - Bem, 2 - Mais ou menos, 3 - Mal: '))

if des == 1:
    print('Que bom que esteja bem! Fico Feliz :)')
    print()
elif des == 2:
    print('Seu dia vai melhorar!')
    print()
elif des == 3:
    print('Que pena que as coisas não estejam bem, espero que melhore, você é incrivel')
    print()
    
x = False
while x != True:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    
    print('Agora escolha a operação que deseja: 4 - Soma 5 - Subtração 6 - Multiplicação 7 - Divisão')
    choose = int(input('Qual operação ? =>  '))
            
    while (choose != 4) and (choose != 5) and (choose != 6) and (choose != 7):
        print('Escolha inválida')
        choose = int(input('Qual operação ? =>  '))
                
    if choose == 4:
        som = a + b
        print(som)
    elif choose == 5:
        sub = a - b
        print(sub)
    elif choose == 6:
        mul = a * b
        print(choose)
    elif choose == 7:
        div = a/b
        print(div)
                
    print()
            
    choose_2 = int(input('Se desejar encerrar o programa (Aperte 0) Caso deseja continuar utilizando (Aperte Qualquer NÚMERO) => '))
    
    if choose_2 == 0:
        x = True
    else:
        print('Continuando o programa...')
        print()
    
MIT License

Copyright (c) 2022 César Costa Pessoa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
