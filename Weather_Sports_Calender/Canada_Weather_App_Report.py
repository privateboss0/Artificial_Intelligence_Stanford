import requests
import smtplib
from email.mime.text import MIMEText

# Your email address and Application password (example email and and password). This can be gotten from: 
# 'Manage Google Account' --> Security --> 2- Step verification --> App passwords

YOUR_EMAIL = "aolaxxxxx@gmail.com"
YOUR_PASSWORD = "xxxx xxxx xxxx xxxx"

# The city and country you want the weather for
CITY = "Toronto"
COUNTRY = "Canada"

# Get the weather data from the API
weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid=API KEY")
weather_data = weather_response.json()

# Get the air quality data from the API
air_quality_response = requests.get(f"https://api.airvisual.com/v2/latest?city={CITY},{COUNTRY}&token=API KEY")
air_quality_data = air_quality_response.json()

# Define the email variable
aolaxxxx = "aolaxxxxx@gmail.com"

weather = weather_data["weather"][0]["main"]
windspeed = weather_data["wind"]["speed"]
humidity = weather_data["main"]["humidity"]
temperature = weather_data["main"]["temp"] * 9/5 + 32

#Data pulled from the API is in Kelvin so we have to convert this to Fahrenheit
temperature_in_fahrenheit = (weather_data["main"]["temp"] - 273.15) * 9/5 + 32

# Check if the air quality data has a "current" key
if "current" in air_quality_data:
    # Get the air quality index
    air_quality_index = air_quality_data["data"]["current"]["aqi"]
else:
    # If the air quality data does not have a "current" key, set the air quality index to None
    air_quality_index = None

# Create the email message
message = MIMEText(f"HThe weather in {CITY}, {COUNTRY} is {weather}. The windspeed is {windspeed} m/s. The humidity is {humidity}%. The temperature is {temperature_in_fahrenheit} degrees Fahrenheit. The air quality index is {air_quality_index}.")
message["Subject"] = "Weather Report"
message["From"] = aolaxxxxx
message["To"] = aolaxxxxx

# Please use gmail forwarding rules if you want to forward this to another email address. Gmail is my usecase so that's what I used

# Send the email
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(YOUR_EMAIL, YOUR_PASSWORD)
smtp_server.sendmail(YOUR_EMAIL, YOUR_EMAIL, message.as_string())
smtp_server.quit()
