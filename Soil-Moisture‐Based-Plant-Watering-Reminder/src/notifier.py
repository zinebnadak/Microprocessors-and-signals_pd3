import spidev
import time
import requests
from datetime import datetime

TELEGRAM_TOKEN   = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

DRY_VALUE = 800
WET_VALUE = 400
THRESHOLD = 80

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def calculate_moisture(raw):
    percentage = ((DRY_VALUE - raw) / (DRY_VALUE - WET_VALUE)) * 100
    return max(0, min(100, round(percentage, 1)))

def notify(msg):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    )

try:
    print("Starting IoT Soil Monitor...")
    while True:
        raw_value = read_channel(0)
        moisture_pct = calculate_moisture(raw_value)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} | Moisture: {moisture_pct}%")

        if moisture_pct < THRESHOLD:
            print("ALERT: Soil is dry! Sending notification...")
            notify(f"Water your plant! Moisture: {moisture_pct}%")

        time.sleep(10)

except KeyboardInterrupt:
    spi.close()
    print("\nProgram stopped by user.")