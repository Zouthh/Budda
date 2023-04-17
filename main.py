import os
import requests

# Ejecutamos el archivo Budda.py.
os.system('python ignore.py')

# Pedimos al usuario que ingrese una dirección IP personalizada.
ip_address = input('Ingrese una dirección IP para buscar su información: ')

# Hacemos una solicitud HTTP a la API de IP-API.com para obtener información de la dirección IP ingresada.
response = requests.get('http://ip-api.com/json/{}'.format(ip_address))
ip_data = response.json()

# Verificamos si la clave 'isp' está presente en el diccionario ip_data.
if 'isp' in ip_data:
    isp = ip_data['isp']
else:
    isp = 'Información no disponible'

# Imprimimos toda la información disponible de la dirección IP.
print('IP Address: {}'.format(ip_data['query']))
print('ISP: {}'.format(isp))
print('Organization: {}'.format(ip_data['org']))
print('AS Number: {}'.format(ip_data['as']))
print('Latitude: {}'.format(ip_data['lat']))
print('Longitude: {}'.format(ip_data['lon']))
print('Region: {}'.format(ip_data['regionName']))
print('Country: {}'.format(ip_data['country']))
print('Zip Code: {}'.format(ip_data['zip']))
print('Time Zone: {}'.format(ip_data['timezone']))
print('Reverse DNS: {}'.format(ip_data['reverse'] if 'reverse' in ip_data else 'N/A'))
print('Mobile: {}'.format(ip_data['mobile'] if 'mobile' in ip_data else 'N/A'))
print('Proxy: {}'.format(ip_data['proxy'] if 'proxy' in ip_data else 'N/A'))

