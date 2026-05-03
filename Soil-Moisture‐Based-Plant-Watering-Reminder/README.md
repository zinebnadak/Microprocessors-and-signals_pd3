# Soil Moisture-Based Plant Watering Reminder
**Microprocessors & Signals Project** &nbsp;·&nbsp; Raspberry Pi 5 · Capacitive Soil Moisture Sensor · MCP3008 ADC · Logisim

---

## What It Does

A capacitive soil moisture sensor measures the water content in soil as an analog voltage. The MCP3008 ADC chip converts that analog signal into a digital value (0–1023) and sends it to the Raspberry Pi via SPI. The Pi logs every reading to a CSV file, plots them as a live graph, and sends a real-time notification to your phone when the plant needs watering.

---

## Course Coverage

| Learning Goal | How It's Addressed |
|---|---|
| Analog & digital signals, sampling, quantization | Sensor outputs analog voltage → MCP3008 samples at fixed intervals → ADC quantizes to 0–1023 |
| Sensors | Capacitive soil moisture sensor as input |
| Microprocessor architecture & programming | Raspberry Pi 5 (ARM) runs Python; MCP3008 handles ADC conversion |
| Operating systems for microprocessors | Raspberry Pi runs Raspberry Pi OS — Linux on microprocessor-class hardware |
| Digital circuit design | ADC circuit designed and simulated in Logisim before wiring |
| Development project | Full working system from sensor to live display and mobile alert, end to end |

---

## Hardware

- Raspberry Pi 5 (4GB)
- Capacitive Soil Moisture Sensor v1.2 (analog output)
- MCP3008 ADC chip — converts analog sensor signal to digital for the Pi
- DHT11/DHT22 temperature & humidity sensor — optional, for richer data
- LED + resistor — optional visual indicator (red = dry, green = ok)
- Active buzzer — optional audible alert
- Breadboard, jumper wires (M-M, M-F), USB-C power supply
- MicroSD card (32GB) with Raspberry Pi OS

---

## Software

- **Logisim Evolution** — simulates ADC circuit
- **Python 3 on Raspberry Pi** — `pip install spidev gpiozero matplotlib requests`
- **Raspberry Pi OS** — Linux-based OS running on the Pi

---

## Build Status

| Part | Task | Tool | Status |
|---|---|---|---|
| 1 | Simulate ADC circuit | Logisim | ✓ |
| 2 | Wire capacitive sensor to MCP3008 | Raspberry Pi | ✓ |
| 3 | Read SPI data from MCP3008 in Python | Raspberry Pi | ✓ |
| 4 | Log data to CSV | Pi + Python | ✓ |
| 5 | Live graph with matplotlib | Pi + Python | ✓ |
| 6 | Send phone notification when dry | Pi + Python | ✓ |
| 7 | Polish, test end to end | All | ✓ |

---

## Notes












???



### Why Raspberry Pi over Arduino?

The Raspberry Pi was chosen over Arduino for this project because of its built-in Wi-Fi and Linux OS. This makes it straightforward to send real-time mobile notifications using Python libraries and web services — something an Arduino Uno would need extra hardware shields to do. The tradeoff is higher power consumption and a ~30–60 second boot time, but for a plant monitor that runs continuously from a wall outlet, this is acceptable.

**Disadvantage worth noting:** The Raspberry Pi has no built-in analog pins, so an external MCP3008 ADC chip is required — unlike Arduino which has built-in ADC. This adds one extra component but is the standard approach for Pi-based sensor projects.

### Why MCP3008 over ADS1115?

| Feature | MCP3008 | ADS1115 |
|---|---|---|
| Resolution | 10-bit (0–1023) | 16-bit (0–65535) |
| Channels | 8 | 4 |
| Protocol | SPI | I2C |
| Assembly | DIP — plugs straight into breadboard | Breakout board — requires soldering |

The MCP3008 was chosen because it plugs directly into a breadboard without soldering, supports up to 8 sensor channels, and is the more beginner-friendly option. Its 10-bit resolution is sufficient for detecting meaningful differences in soil moisture levels.

### Why Capacitive Sensor over Resistive?

Capacitive soil moisture sensors measure water content by detecting changes in electrical capacitance rather than passing current through the soil. This means they do not corrode over time the way resistive (metal-probe) sensors do when left in moist soil. For a long-running plant monitor, this makes them the practical choice.






















### Signal Flow (for Conceptual Understanding)

The soil moisture sensor generates an analog voltage based on the water content in the soil. Since the Raspberry Pi only understands digital signals, the MCP3008 ADC chip acts as a translator — converting the voltage into a digital number (0–1023) that the Python script can process, log, graph, and act on.

---

## How to Build

> ⚠️ Instructions added as each phase is completed.

### Part 1 — Simulate ADC circuit