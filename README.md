### Here is an Arduino code that turns the LED on or off depending on the command received via the serial port.

```
int ledPin = 13; // Pin for the built-in LED

void setup() {
  pinMode(ledPin, OUTPUT);  // Set LED pin as output
  Serial.begin(9600);       // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readString();  // Read the command from the serial port

    if (command == "on") {
      digitalWrite(ledPin, HIGH);  // Turn the LED on
    } else if (command == "off") {
      digitalWrite(ledPin, LOW);   // Turn the LED off
    }
  }
}


```
