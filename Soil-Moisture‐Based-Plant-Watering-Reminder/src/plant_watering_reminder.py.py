import spidev
import time
import csv
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Telegram credentials — replace with your own 
TELEGRAM_TOKEN   = "YOUR_TELEGRAM_BOT_TOKEN"    # from @BotFather
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"       # your chat ID


DRY_VALUE = 800     # ADC reading in bone-dry soil 
WET_VALUE = 400     # ADC reading in water          
THRESHOLD = 30      # Moisture % below which a notification is sent


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

times, values = [], []
plt.ion()
fig, ax = plt.subplots()


def read():
    """Read raw 10-bit ADC value from MCP3008 channel 0."""
    r = spi.xfer2([1, 128, 0])
    return ((r[1] & 3) << 8) + r[2]


def moisture(raw):
    """Convert raw ADC value to moisture percentage (0–100)."""
    pct = ((DRY_VALUE - raw) / (DRY_VALUE - WET_VALUE)) * 100
    return max(0, min(100, round(pct, 1)))


def notify(msg):
    """Send a Telegram message."""
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    )


try:
    print("Starting Soil Monitor...")
    while True:
        raw = read()
        pct = moisture(raw)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"{now} | Raw: {raw} | Moisture: {pct}%")

        with open("moisture_log.csv", "a", newline="") as f:
            csv.writer(f).writerow([now, raw, pct])

        times.append(now[-8:])
        values.append(pct)
        ax.clear()
        ax.plot(times, values, color="green", marker="o")
        ax.set_title("Soil Moisture")
        ax.set_ylabel("Moisture %")
        ax.set_ylim(0, 100)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(0.1)

        if pct < THRESHOLD:
            print("ALERT: Dry! Sending notification...")
            notify(f"Water your plant! Moisture: {pct}%")

        time.sleep(10)

except KeyboardInterrupt:
    spi.close()
    print("Stopped")
