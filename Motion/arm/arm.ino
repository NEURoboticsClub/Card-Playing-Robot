#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

int pos1 = 90;  // Initial position for servo 1
int pos2 = 90;  // Initial position for servo 2
int pos3 = 90;  // Initial position for servo 3

void setup() {
  servo1.attach(9); // Attach servo 1 to pin 9
  servo2.attach(10); // Attach servo 2 to pin 10
  servo3.attach(11); // Attach servo 3 to pin 11
}

void loop() {
  // Move the arm down to pick up the card
  for (int i = 90; i <= 180; i++) {
    servo1.write(i); // Move servo 1
    servo2.write(i); // Move servo 2
    servo3.write(i); // Move servo 3
    delay(15); // Delay for smooth motion
  }

  // Wait for a moment to simulate picking up the card
  delay(1000);

  // Move the arm up
  for (int i = 180; i >= 90; i--) {
    servo1.write(i); // Move servo 1
    servo2.write(i); // Move servo 2
    servo3.write(i); // Move servo 3
    delay(15); // Delay for smooth motion
  }

  // Wait for a moment before repeating the process
  delay(1000);
}
