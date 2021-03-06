# weatherapi (Умный сервис прогноза погоды)

### ABOUT
This project use public weather api for get weather status for choosed city

#### Used public apis:
    1. https://openweathermap.org/api

### How to run it
Firstly you need API_KEY for openweathermap.org/api. 
Use it as enviroment variable or as a variable on app/.env file
#### for Ubuntu:
    git clone git@github.com:KindleFlame/weatherapi.git
    python3 -m venv ./weatherapi/venv/ 
    source ./weatherapi/venv/bin/activate
    cd weatherapi/
    pip install -r requirements.txt
    export API_KEY=yourapikey
    python3 run.py

#### for Ubuntu, if you want run in docker container:
    git clone git@github.com:KindleFlame/weatherapi.git
    cd weatherapi/
    docker build -f .Dockerfile -t weatherapi .
    sudo docker run -it --net=host weatherapi

If you run script as above instructions, then by default yourserverhost will be 127.0.0.1:5000
and for use it need to go to the page https://127.0.0.1:5000/weather

### How to use it. 
Cities must be in English language
This project is writed on flask and has three interfaces:

1. You can get city weather by form on address: 'https://yourserverhost/weather'

2. Also you can use api query: 'https://yourserverhost/api/weather/<city_name>'.
    For example: 'https://yourserverhost/api/weather/Moscow'
3. Or you can send json data to 'https://yourserverhost/api/weather'
 for example, in this case you'll get such json:
```     
    {
     "status": "success", 
     "weather": {
       "description": "облачно с прояснениями", 
       "icon_img": "http://openweathermap.org/img/wn/04n@2x.png", 
       "status": "Clouds", 
       "temperature": 13.96, 
       "wind": "3 м/с"
    }
    }
 ```
 


