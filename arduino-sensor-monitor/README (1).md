# Environment Data Logger
**Microprocessors & Signals Project**
`Arduino Uno` · `KY-038 Sound Sensor` · `Raspberry Pi` · `Logisim`

---

## What It Does

The KY-038 sound sensor captures ambient sound as an analog voltage. The Arduino Uno samples it, converts it to a number (0–1023) via its built-in ADC (analog-to-digital converter), and streams the values over USB serial to a Raspberry Pi. The Pi logs every reading to a CSV file and plots them as a live graph. A buzzer fires when sound crosses a set threshold.

```
Sound → KY-038 → Arduino (ADC + Serial) → Raspberry Pi → Graph & Log
```

---

## Course Coverage

| Learning Goal | How It's Addressed |
|---|---|
| Analog & digital signals, sampling, quantization | Sensor outputs analog voltage → Arduino samples at fixed intervals → ADC quantizes to 0–1023 |
| Sensors & actuators | KY-038 sound sensor as input, buzzer as output actuator |
| Microprocessor architecture & programming | Arduino Uno (ATmega328P) in C++; Raspberry Pi (ARM) runs Python |
| Operating systems for microprocessors | Raspberry Pi runs Raspberry Pi OS — Linux on microprocessor-class hardware |
| Digital circuit design | ADC circuit designed and simulated in Logisim before wiring |
| Development project | Full working system from sensor to live display, end to end |

---

## Hardware
- Arduino Uno
- KY-038 sound sensor (analog output)
- Buzzer — actuator, reacts to sound threshold
- LED + resistor — optional visual indicator
- Raspberry Pi with Raspberry Pi OS
- Breadboard, jumper wires, USB cable

## Software
- Arduino IDE — uploads C++ sketch to Arduino
- Logisim Evolution — simulates ADC circuit
- Python 3 on Raspberry Pi — `pip install pyserial matplotlib`

---

## Build Status

| Days | Task | Tool | Status |
|---|---|---|---|
| 1–2 | Simulate ADC circuit | Logisim | ⬜ |
| 3–4 | Wire KY-038, read analog values | Arduino | ⬜ |
| 5–6 | Send data over USB serial | Arduino | ⬜ |
| 7–8 | Set up Pi OS, receive data in Python | Raspberry Pi | ⬜ |
| 9–10 | Log data to CSV | Pi + Python | ⬜ |
| 11–12 | Live graph with matplotlib | Pi + Python | ⬜ |
| 13–14 | Add buzzer actuator on threshold | Arduino + Pi | ⬜ |
| 15–18 | Polish, test end to end | All | ⬜ |

---

## How to Run
> ⚠️ Instructions added as each phase is completed.

---

*Built for Microprocessors & Signals*
