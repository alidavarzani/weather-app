from flask import Flask, render_template, request, jsonify
import requests
import psycopg2
from datetime import datetime

app = Flask(__name__, static_url_path="/static")  # Serve static files from /static

# Weather API configuration
API_KEY = "f5b99cad1071fc0904f92681a192a193"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Database configuration
DB_CONFIG = {
    "dbname": "weather_db",
    "user": "weatheradmin",
    "password": "1234",
    "host": "db",
    "port": "5432"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.json.get("city")
    weather_data = fetch_weather(city)
    if weather_data:
        save_to_db(weather_data)
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Failed to fetch weather data"}), 400

def fetch_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"]["deg"],
            "humidity": data["main"]["humidity"],
            "weather_condition": data["weather"][0]["main"],
            "weather_description": data["weather"][0]["description"]
        }
    else:
        return None

def save_to_db(data):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query = """
        INSERT INTO weather_data (city, temperature, feels_like, wind_speed, wind_deg, humidity, weather_condition, weather_description, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data["city"],
        data["temperature"],
        data["feels_like"],
        data["wind_speed"],
        data["wind_deg"],
        data["humidity"],
        data["weather_condition"],
        data["weather_description"],
        datetime.now()
    ))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
