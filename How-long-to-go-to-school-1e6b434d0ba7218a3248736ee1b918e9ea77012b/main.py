from func import lonlat_distance
from getting import getting
import requests

address = input()
ostankino_tower = 'ул. Академика Королева, 15, Москва, 127427'


geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"


geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": address,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)


geocoder_params_ostankino = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": ostankino_tower,
    "format": "json"}

response_ostankino = requests.get(geocoder_api_server, params=geocoder_params_ostankino)

tompony = getting(response)
tompony_ostankino = getting(response_ostankino)

l = int(lonlat_distance(tompony, tompony_ostankino)) / 1000

h1 = 525

h2 = (l / 3.6 - (h1 ** 0.5)) ** 2

print(int(h2), 'м')


