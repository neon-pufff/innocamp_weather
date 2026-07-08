from flask import Flask, session, render_template, request, url_for, redirect

import random
import requests


def f(city):
    key = "5638fc1947fe49c283c92135260707"
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"

    response = requests.get(url)
    if response.status_code != 200:
        return "Ошибка"
    data = response.json()
    return str(data['current']['temp_c']) + "°C"


app = Flask(__name__)
app.secret_key = "key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        if request.method == "POST":
            city = request.form.get("city", "").strip()
            result = random.randint(15, 32)
            if city != "":
                result = f(city)

    return render_template("forecast.html", result=result)


@app.route("/info", methods=["GET", "POST"])
def info():
    return render_template("contacts.html")


app.run(debug=True)
