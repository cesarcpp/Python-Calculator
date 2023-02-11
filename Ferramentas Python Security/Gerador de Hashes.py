#Gerador de Hashes

import hashlib

string = input("Digite o texto a ser gerado a Hash: ") #Input para colocar o texto

menu = int(input(''' #MENU - ESCOLHA O TIPO DE HASH #
                               1) md5
                               2) Sha1
                               3) Sha256
                               4) Sha512

                               Digite o número do hash a ser gerado: ''')) #Menu para escolha do Hash a ser gerado

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8')) #utilizando a biblioteca para gerar o MD5
    print("O Hash da string por MD5 é: ", resultado.hexdigest()) #printando o Hash gerado no console
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8')) #utilizando a biblioteca para gerar o SHA1
    print("O Hash da string por SHA1 é: ", resultado.hexdigest()) #printando o Hash gerado no console
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8')) #utilizando a biblioteca para gerar o SHA256
    print("O Hash da string por SHA256 é: ", resultado.hexdigest()) #printando o Hash gerado no console
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8')) #utilizando a biblioteca para gerar o SHA512
    print("O Hash da string por SHA256 é: ", resultado.hexdigest()) #printando o Hash gerado no console
else:
    print("Ocorreu um erro, tente novamente") #printar caso o usuário erre os comandos
