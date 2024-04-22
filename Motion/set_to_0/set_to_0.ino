#include <Servo.h>

Servo servo1;  // Define Servo object

void setup() {
  servo1.attach(9);  // Attach servo to pin 9
}

void loop() {
  servo1.write(190);  // Set servo position to 0 degrees
  delay(1000);      // Wait for 1 second
}
