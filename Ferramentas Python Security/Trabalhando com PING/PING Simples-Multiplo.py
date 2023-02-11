#importamos a biblioteca time // OS // Socket
import os
import time
import socket
import sys #Uma bibliote diferente da OS

print('-' * 60)
ip_host = input ("Digite o IP ou Host a ser verificado: ")

#como chamar os funcionamentos do sistemas
os.system(' ping -n 6 {} '.format(ip_host))

#como acessar um arquivo
with open('hosts.txt') as file:
    dump = file.read()#-ler o arquivo
    dump = dump.splitlines() #-Splitlines irá fazer com que nosso código fique em linha

#criando um laço de repetição para percorrer os IPs no txt 
    for ip in dump:
        print('Verificando o IP: ', ip)
        os.system(' ping -n 2 {}'.format(ip))
        time.sleep(5)#-definimos um tempo limite de stand-by de uma funcionalidade a outra

#Fazendo o desenvolvimento de um cliente TCP

def main( ):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("A conexão falhou!")
        print(f"Error: {error}")
        sys.exit( )
        
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + " e na porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as error:
        print("A conexão falhou na Porta e Host indicado")
        print(f"Erro: {error}")
        sys.exit( )


if __name__ == "__main__":
    main()

#Fazendo o desenvolvimento de um cliente UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso!!")

host = 'localhost'
porta = 5433

mensagem = 'Olá servidor, tudo bem?'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvform(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print('Cliente: Fechando a Conexão')
    s.close()

#Criando um Server para conexão de um server

host_2 = 'localhost'
porta_2 = 5432

s.bind((host_2, porta_2))
mensagem_2 = '\nServidor: Olá Cliente, tranquilo?'

while 1:
    dados_2, endereco = s.recvfrom(4096)

    if dados_2:
        print('Servidor enviando mensagem...')
        s.sendto(dados_2 + (mensagem_2.encode()), endereco)






        
