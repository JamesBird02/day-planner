import csv
import random
from urllib import request
import json
import datettime


def get_quote(quotes_file = 'quotes.csv'):
    try:
        with open(quotes_file) as csvfile:
            quotes = [{'author': line[0],
                       'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]

    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always Look on the Bright Side of Life.'}]

    return random.choice(quotes)


def get_weather(coords={'lat': 54.52429, 'lon': -1.55039}):
    try:
        api_key = '0f696e7d5a1641338ff29d984e9207e6'
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'],
                    'country': data['city']['country'], 'periods': list()}

        for period in data['list'][0:9]:  # populate list with next 9 forecast periods
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})

        return forecast

    except Exception as e:
        print(e)

def get_article():
    pass


if __name__ == '__main__':
    pass

