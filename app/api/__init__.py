from .src import OpenWeatherMap

sources = {
    'openweathermap': OpenWeatherMap
}


def api_input(city):
    weather = sources['openweathermap']
    data = weather(city)

    return data

