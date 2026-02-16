import requests

api_key = 'https://api.openweathermap.org/data/2.5/weather?q=Patna&appid=6ef51e492f55d7e1707a7b64038055b6'

params = {
    "units": "metric"
}
response = requests.get(api_key, params=params)

data1 = response.json()

if response.status_code == 200:
    print("Data retrieved successfully!")
    print("city:", data1['name'])
    print(f"Temperature: {data1['main']['temp']}°C")
    print(f"Feels like: {data1['main']['feels_like']}°C")
    print(f"Weather: {data1['weather'][0]['description']}")

    print(f"Humidity: {data1['main']['humidity']}%")
    print(f"Wind Speed: {data1['wind']['speed']} m/s")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather in {data1['name']}</title>
</head>
<body>
    <h1>Weather in {data1['name']}</h1>
    <p>Temperature: {data1['main']['temp']}°C</p>
    <p>Feels like: {data1['main']['feels_like']}°C</p>
    <p>Weather: {data1['weather'][0]['description']}</p>
    <p>Humidity: {data1['main']['humidity']}%</p>
    <p>Wind Speed: {data1['wind']['speed']} m/s</p>
</body>
</html>"""

with open("weather"
".html", "w") as file:
    file.write(html)

print("HTML file 'weather.html' has been created with the weather data.")
