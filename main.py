import requests
import smtplib

MY_MAIL = "gokultesting1234@gmail.com"
PASSWORD = "zqqaczptxxvoekdx"

# Give your mail id
TO_MAIL = """ Your mail """

api_key = "15da6e1c77de02d417cce7321f4ea03d"
parameters = {
    "lat": 12.153000,
    "lon": 77.105904,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get("https://api.openweathermap.org/data/2.8/onecall?", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for rain_p in range(0, 12):
    check = data["hourly"][rain_p]["weather"][0]["id"]
    if check < 700:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_MAIL, PASSWORD)
    connection.sendmail(from_addr=MY_MAIL,
                        to_addrs=TO_MAIL,
                        msg="Subject:Rainy Day\n\nit's going to rain today take umbrella with you.!")
    print("Result 1 executed")

else:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_MAIL, PASSWORD)
    connection.sendmail(from_addr=MY_MAIL,
                        to_addrs=TO_MAIL,
                        msg="Subject:Weather is clear\n\nYou don't wanna carry an umbrella with you.!")
    print("Result 2 executed")


