import requests
import smtplib
from email.mime.text import MIMEText

# Your email address and password
YOUR_EMAIL = "cr7@gmail.com"
YOUR_PASSWORD = "xxxx xxxx xxxx xxxx"

# The city and country you want the weather for
CITY = "Toronto"
COUNTRY = "Ontario"

# Get the weather data from the API
weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid=INPUT API KEYS")
weather_data = weather_response.json()

# Get the air quality data from the API
air_quality_response = requests.get(f"https://api.airvisual.com/v2/latest?city={CITY},{COUNTRY}&token=INPUT API KEYS")
air_quality_data = air_quality_response.json()

# Define the email variable
cr7 = "cr7@gmail.com"
kipchoge = "Kipchoge@gmail.com"


weather = weather_data["weather"][0]["main"]
windspeed = weather_data["wind"]["speed"]
humidity = weather_data["main"]["humidity"]
temperature = weather_data["main"]["temp"]

# Check if the air quality data has a "current" key
if "current" in air_quality_data:
    # Get the air quality index
    air_quality_index = air_quality_data["data"]["current"]["aqi"]
else:
    # If the air quality data does not have a "current" key, set the air quality index to None
    air_quality_index = None

# Create the email message
message = MIMEText(f"The weather in {CITY}, {COUNTRY} is {weather}. The windspeed is {windspeed} m/s. The humidity is {humidity}%. The temperature is {temperature} degrees fahrenheit. The air quality index is {air_quality_index}.")
message["Subject"] = "Weather Report"
message["From"] = cr7
message["To"] = Kipchoge

# Send the email
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(YOUR_EMAIL, YOUR_PASSWORD)
smtp_server.sendmail(YOUR_EMAIL, YOUR_EMAIL, message.as_string())
smtp_server.quit()
