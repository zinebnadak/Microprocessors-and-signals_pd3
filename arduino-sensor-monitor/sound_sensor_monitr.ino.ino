// Sound Sensor Monitor
// Reads analog value from KY-038 on pin A0.

void setup() {
  Serial.begin(9600); // start serial communication at 9600 baud (speed of data transfer)
}

void loop() {
  int soundValue = analogRead(A0); // read sensor value (0-1023)
  Serial.println(soundValue);      // send value to PC
  delay(100);                      // wait 100ms before next reading
}
