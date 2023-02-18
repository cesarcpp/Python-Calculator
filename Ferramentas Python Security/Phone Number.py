#Verificador de Telefone

import phonenumbers

from phonenumbers import geocoder

phone_number = input('Digite o telefone no formato: +551140028922: ')

phone = phonenumbers.parse(phone_number)

print(geocoder.description_for_number(phone, 'pt'))
