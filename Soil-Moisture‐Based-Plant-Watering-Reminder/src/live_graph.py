import spidev
import matplotlib.pyplot as plt
from datetime import datetime

DRY_VALUE = 800
WET_VALUE = 400

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

times, values = [], []
plt.ion()
fig, ax = plt.subplots()

try:
    while True:
        r = spi.xfer2([1, 128, 0])
        raw = ((r[1] & 3) << 8) + r[2]
        pct = max(0, min(100, ((DRY_VALUE - raw) / (DRY_VALUE - WET_VALUE)) * 100))

        times.append(datetime.now().strftime("%H:%M:%S"))
        values.append(pct)

        ax.clear()
        ax.plot(times, values, color="green", marker="o")
        ax.set_ylim(0, 100)
        ax.set_title("Soil Moisture")
        plt.pause(1)

except KeyboardInterrupt:
    spi.close()
