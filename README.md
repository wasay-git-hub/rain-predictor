# 🌧️ Rain Predictor SMS Alert System

An automated practical Python project that predicts rain for the next 12 hours using a weather API and sends an SMS alert via Twilio if rain is expected. Deployed and scheduled using PythonAnywhere to run daily at 9:00 AM.

---

## 📌 Features

- Retrieves 5-day weather forecast data (3-hour intervals)
- Filters and analyzes the next 12 hours of weather
- Detects if rain is forecasted
- Sends an SMS alert using Twilio:
  > *"It might rain today. Make sure to carry an umbrella!"*
- Automatically runs every morning via PythonAnywhere scheduler

---

## 🚀 How It Works

1. **Weather Forecast API**  
   Uses a weather API (e.g., OpenWeatherMap) to fetch forecast data based on your location (latitude & longitude).

2. **Rain Detection Logic**  
   Checks 4 forecast entries (each 3 hours apart) to cover the next 12 hours. If any entry forecasts rain, it triggers the SMS alert.

3. **Twilio SMS**  
   Sends an SMS to your phone number using Twilio’s API.

4. **Automation**  
   Hosted on PythonAnywhere and scheduled to run daily at 9:00 AM.

---

## 🛠️ Tech Stack

- Python 3
- [`requests`](https://docs.python-requests.org/en/latest/) – For making HTTP requests
- [`twilio`](https://www.twilio.com/docs/sms) – For sending SMS messages
- [PythonAnywhere](https://www.pythonanywhere.com/) – For hosting & scheduling the script
- Weather API (e.g., [OpenWeatherMap](https://openweathermap.org/api))

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rain-predictor-alert.git
cd rain-predictor-alert
```

### 2. Set environment variables

```bash
WEATHER_API_KEY=your_weather_api_key
LATITUDE=your_latitude
LONGITUDE=your_longitude
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone
RECIPIENT_PHONE_NUMBER=your_phone_number
```

### 3. Run the script

```bash
python rain_predictor.py
```
