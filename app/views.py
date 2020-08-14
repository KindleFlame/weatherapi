from flask import render_template, redirect, make_response, jsonify
from flask import request
from app import app
from app.forms import FormWeatherQuery
from .api import api_input


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/weather', methods=['GET', 'POST'])
def register():
    form = FormWeatherQuery(request.form)
    if request.method == 'POST' and form.validate():
        user, city = form.username.data, form.city.data
        print(user)

        weather = api_input(city)

        data = weather.to_dict()

        return render_template('weather_result.html', data=data)
    return render_template('weather_form.html', form=form)


@app.route('/api/weather', methods=['POST'])
def weather_api():
    data = request.get_json()

    if not data or 'city' not in data:
        return make_response(jsonify({
            'status': 'failed',
            'message': 'data must have city key'
        }), 400)

    city = data.get('city')
    weather = api_input(city)
    answer = weather.to_dict()

    response_object = {
        'status': 'success',
        'weather': answer,
    }

    return make_response(jsonify(response_object), 200)


@app.route('/api/weather/<city>', methods=['GET', 'POST'])
def weather_city_api(city):

    weather = api_input(city)
    answer = weather.to_dict()

    response_object = {
        'status': 'success',
        'weather': answer,
    }

    return make_response(jsonify(response_object), 200)
