# Pavel

import requests
from pprint import pprint
from countryinfo import CountryInfo

while True:
    country = CountryInfo(input('Введите город: ')).info()

    print(f'''
Name : \033[31m{country['name']}\033[0m
NativeName: \033[31m{country['nativeName']}\033[0m
Capital : \033[32m{country['capital']}\033[0m
Capital_latlng: \033[32m{country['capital_latlng']}\033[0m
Region : \033[33m{country['region']}\033[0m
Provinces: \033[33m{country['provinces']}\033[0m
Population : \033[34m{country['population']}\033[0m
Borders: \033[32m{country['borders']}\033[0m
Language : \033[35m{country['languages']}\033[0m
TimeZones : {country['timezones']}
Area : \033[36m{country['area']} km²\033[0m
Translations: \033[35m{country['translations']}\033[0m
Wiki : \033[38m{country['wiki']}\033[0m
''')



url = "https://airbnb13.p.rapidapi.com/search-location"

querystring = {
    "location": "Paris",
    "checkin": "2023-09-16",
    "checkout": "2023-09-17",
    "adults": "1",
    "children": "0",
    "infants": "0",
    "pets": "0",
    "page": "1",
    "currency": "USD"}

headers = {
    "X-RapidAPI-Key": "bac79eaabfmsh0b5842b3efa7f3ep174c2cjsne3c3dc6d8f6f",
    "X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
}

city = input('Введите город для просмотра: ')
querystring['q'] = city
response = requests.get(url, headers=headers, params=querystring).json()
for i in response['results']:
    address = i['address']
    type1 = i['type']
    price = i['price']['total']
    beds = i['beds']
    name = i['name']
    rating = i['rating']
    amenities = i['previewAmenities']
    print(f'''
В городе {city}, расположенный по адресу {address} 
и названием {name} с рейтингом {rating} и дополнительными удобствами с {amenities}
есть комнаты с типом {type1} c количеством кроватей {beds}.
Общая стоимость будет {price}
	''')
