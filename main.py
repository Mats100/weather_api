import asyncio
import requests
async def get_data():
    city_name = input('Enter city: ')
    url = f'http://api.weatherstack.com/current?access_key=35d3d2527e9de163d12b7b328245f4e6&query={city_name}'
    response = requests.get(url)
    api_response = response.json()
    print(f'There is {str(api_response["current"]["temperature"])} degree outside and it feels'
          f'like {str(api_response["current"]["feelslike"])} degree and '
          f'{str(api_response["current"]["precip"])} % chance of rain and humidity'
          f' is {str(api_response["current"]["humidity"])} %')

asyncio.run(get_data())