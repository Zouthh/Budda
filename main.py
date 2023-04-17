import os
import requests

# Ejecutamos el archivo Budda.py.
os.system('python ignore.py')

# Función para obtener la información de la dirección IP utilizando la API de IP-API
def get_ip_info(ip_address):
    response = requests.get('http://ip-api.com/json/{}'.format(ip_address))
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Loop principal
while True:
    # Pedir al usuario que ingrese una dirección IP
    ip_address = input("Ingrese una dirección IP para rastrear (o 'q' para salir): ")

    # Salir del loop si el usuario ingresa 'q'
    if ip_address.lower() == 'q':
        break

    # Obtener la información de la dirección IP
    ip_data = get_ip_info(ip_address.strip())
    if ip_data:
        # Imprimir la información de la dirección IP
        print('Información para la dirección IP: {}'.format(ip_address.strip()))
        print('País: {}'.format(ip_data['country']))
        print('Región: {}'.format(ip_data['regionName']))
        print('Ciudad: {}'.format(ip_data['city']))
        print('Latitud: {}'.format(ip_data['lat']))
        print('Longitud: {}'.format(ip_data['lon']))
        print('ISP: {}'.format(ip_data['isp']))
        print('Organización: {}'.format(ip_data['org']))
        print('Código postal: {}'.format(ip_data['zip']))
        print('Zona horaria: {}'.format(ip_data['timezone']))
        print('-----------------------------------------------------')
    else:
        print('No se pudo obtener información para la dirección IP: {}'.format(ip_address.strip()))

print("Saliendo del programa.")
