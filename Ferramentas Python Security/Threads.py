#trabalhar com threads e IPs
from threading import Thread #importando a biblioteca Thread
import time #importando a biblitoeca time

def carro(velocidade, piloto): #criando uma função para realizar a rodagem dos carros
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f"Piloto: {piloto} Km: {trajeto} \n")

t_carro1 = Thread(target=carro, args=[1, "Bruno"]) #utilizando a biblioteca thread para criar as threads
t_carro2 = Thread(target=carro, args=[2, "Carlos"])

t_carro1.start() #iniciando as threads
t_carro2.start()
