import spidev
import csv
from datetime import datetime

DRY_VALUE = 800
WET_VALUE = 400

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

try:
    while True:
        raw_value = read_channel(0)
        moisture_pct = calculate_moisture(raw_value)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} | Moisture: {moisture_pct}%")
        with open('moisture_log.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, raw_value, moisture_pct])

except KeyboardInterrupt:
    spi.close()
    print("\nStopped.")