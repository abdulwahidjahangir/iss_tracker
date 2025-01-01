# ISS Tracker

This project tracks the International Space Station (ISS) and notifies you via email when it is passing overhead and the conditions are optimal (nighttime). The script uses the ISS API to get the ISS's current location and the Sunrise-Sunset API to determine whether it is nighttime at your location.

## Features
- Fetches the current location of the ISS using the [Open Notify API](http://open-notify.org/).
- Determines whether it is nighttime using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).
- Sends an email notification when the ISS is overhead and it is nighttime.

## Requirements
- Python 3.8+
- Libraries: `requests`, `smtplib`

## Setup

### 1. Clone the Repository

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install requests
```

### 3. Configure Environment Variables
Edit the following variables in the script:

- `MAIL_HOST`: Your email provider's SMTP server (e.g., `smtp.gmail.com` for Gmail).
- `MAIL_USERNAME`: Your email address.
- `MAIL_PASSWORD`: Your email password (or app-specific password if applicable).
- `MY_LAT`: Your latitude.
- `MY_LONG`: Your longitude.

### 4. Enable Less Secure Apps (If Necessary)
For Gmail users, you may need to enable less secure app access or create an app-specific password if two-factor authentication is enabled.

### 5. Run the Script
Run the script to start tracking the ISS:
```bash
python iss_tracker.py
```

## How It Works
1. The script checks the ISS's current location every minute using the ISS API.
2. It determines if the ISS is close to your location (within 5 degrees of latitude and longitude).
3. It checks the Sunrise-Sunset API to ensure it is nighttime at your location.
4. If both conditions are met, it sends an email notification to your configured email address.
