import requests
import os

API_KEY = os.getenv('API_KEY', '')
# API_KEY = '24b37b34c869c9d6f69fa51d30245426'


def API_LINK(city, source='openweathermap'):
    main_link = 'https://api.openweathermap.org/data/2.5/'
    method = 'weather?'
    kwargs = {
        'q': city,
        'lang': 'ru',
        'units': 'metric',
        'appid': API_KEY,
    }

    kwargs = ['='.join(i) for i in kwargs.items()]

    # EXAMPLE: '''https://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&units=metric&appid=24b37b34c869c9d6f69fa51d30245426'''
    link = main_link + method + '&'.join(kwargs)

    return link


def url_request(url):
    with requests.Session() as session:
        return session.get(url)


def json_request(url):
    with requests.Session() as session:
        return session.get(url).json()


def get_weather_info(city, source):
    link = API_LINK(city, source)
    weather_info = json_request(link)
    return weather_info


# from collections import namedtuple
# BASE_WEATHER_FIELDS =    'temperature status description'.split()
# WEATHER_DEFAULT_VALUES = (None,       None, None)
#
# BASE_WEATHER = namedtuple('BaseWeather', BASE_WEATHER_FIELDS)
# BASE_WEATHER.__new__.__defaults__ = WEATHER_DEFAULT_VALUES


# class BaseWeather(BASE_WEATHER):
class BaseWeather:
    source = None
    temperature = None
    status = None
    description = None
    icon = None
    wind = None

    def get_weather_info(self, city):
        return get_weather_info(city, self.source)
    
    def to_dict(self):
        return dict(self.__dict__)


class OpenWeatherMap(BaseWeather):
    
    def __init__(self, city):
        weather_info = self.get_weather_info(city)

        self.temperature = weather_info.get('main', {}).get('temp', 'unknown')

        # TODO: add wind direction
        wind = weather_info.get('wind', {})
        self.wind = str(wind.get('speed', 'unknown')) + ' м/с'

        weather = weather_info.get('weather')[0]

        icon_id = weather.get('icon')
        self.icon_img = f'http://openweathermap.org/img/wn/{icon_id}@2x.png'

        self.status = weather.get('main', 'unknown')
        self.description = weather.get('description', 'unknown')
