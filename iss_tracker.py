import smtplib
import time

import requests
from datetime import datetime

MAIL_HOST = "smtp.your-email-provider.com"  # Replace with your email host, e.g., smtp.gmail.com
MAIL_USERNAME = "your-email@example.com"    # Replace with your actual email address
MAIL_PASSWORD = "your-email-password"       # Replace with your actual email password
MY_LAT = 37.7749  # Replace with your latitude
MY_LONG = -122.4194  # Replace with your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunrise or time_now <= sunset:
        print("Night")
        return True


def send_email():
    with smtplib.SMTP(MAIL_HOST) as connection:
        connection.starttls()
        connection.login(user=MAIL_USERNAME, password=MAIL_PASSWORD)
        connection.sendmail(
            from_addr=MAIL_USERNAME,
            to_addrs=MAIL_USERNAME,
            msg="Subject:The ISS is Above You!\n\n"
                 "The International Space Station (ISS) is currently passing overhead. This is your chance to witness something amazing!\n\n"
                "Step outside, look up, and enjoy the breathtaking view of humanity's orbital laboratory.\n\n"
                "Clear skies and happy stargazing!\n\n"
                "Best regards,\n"
                "Your ISS Tracker"
        )
        print("Email Sent")



while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()
