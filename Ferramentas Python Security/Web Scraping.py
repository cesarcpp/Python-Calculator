#Criando um Web Scraping

#importando as bibliotecas
from bs4 import BeautifulSoup 
import requests

#criando um objeto onde armazena o conteudo requisitado do site...
site = requests.get("https://www.climatempo.com.br/").content

#criando um objeto onde armazena o site em formato HTML
soup = BeautifulSoup(site, 'html.parser')

#executando o comando Print para que o sistema mostre o HTML em formato
#de string
print(soup.prettify())

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(temperatura.string)
 
