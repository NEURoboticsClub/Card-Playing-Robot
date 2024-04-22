// The goal of this code is to test the motion of the robot
// It goes to a full cycle of picking up a card, flipping it and putting it back down
// Controls arm, flipper and suction cup


#include <Servo.h>

Servo arm1;
Servo arm2;
Servo arm3;
Servo flipperSmall;
Servo flipperBig;
int motorPin = 8; // Define the pin connected to the motor
int valvePin = 7;

void setup() {
  arm1.attach(3); // Attach arm 1 to pin 9
  arm2.attach(4); // Attach arm 2 to pin 10
  arm3.attach(11); // Attach arm 3 to pin 11
  flipperSmall.attach(12); // Attach small servo to pin 12
  flipperBig.attach(13); // Attach big servo to pin 13
  pinMode(motorPin, OUTPUT); // Set the motor pin as an output
  pinMode(valvePin, OUTPUT); // Set the valve pin as an output

  // Starting suction
  digitalWrite(motorPin, LOW);
  digitalWrite(valvePin, LOW);

  // Motor position
  arm1.write(65); // Move servo 1
  arm2.write(70); // Move servo 2
  arm3.write(0);

}

void loop() {

  // Turn on suction
  // digitalWrite(motorPin, HIGH);


  // Move the arm down to pick up the card
  for (int i = 65; i >= 40; i--) {
    arm1.write(i); 
    delay(15); 
  }
   for (int i = 70; i <= 120; i++) {
    arm2.write(i); 
    delay(15); 
  }
  for (int i = 40; i <= 110; i++) {
    arm1.write(i); 
    delay(15); 
  }

  // Wait to pick up card
  delay(60);

  // Move the arm to the flipper
  for (int i = 110; i >= 80; i--) {
    arm1.write(i); 
    delay(15); 
  }
  for (int i = 120; i >= 90; i--) {
    arm2.write(i); 
    delay(15); 
  }

  // Close flipper
  flipperSmall.write(90);  // Move the servo to 90 degrees

  // Turn off suction
  digitalWrite(valvePin, HIGH);
  digitalWrite(motorPin, LOW);

  // Move up the arm
  for (int i = 80; i >= 60; i--) {
    arm1.write(i); 
    delay(15); 
  }
  
  // Flip the flipper

  // Turn on the suction
  digitalWrite(valvePin, LOW);
  digitalWrite(motorPin, HIGH);

  // Arm picks up card from flipper
  for (int i = 60; i <= 80; i++) {
    arm1.write(i); 
    delay(15); 
  }

  // Move arm to table
  for (int i = 90; i <= 120; i++) {
    arm2.write(i); 
    delay(15); 
  }
  for (int i = 80; i <= 100 ; i++) {
    arm1.write(i); 
    delay(15); 
  }
  
  // Turn off suction
  digitalWrite(valvePin, HIGH);
  digitalWrite(motorPin, LOW);


  // Arm goes to rest
  for (int i = 110; i >= 40; i--) {
    arm1.write(i); 
    delay(15); 
  }

   for (int i = 120; i >= 70; i--) {
    arm2.write(i); 
    delay(15); 
  }
  for (int i = 40; i <= 65; i++) {
    arm1.write(i); 
    delay(15); 
  }
  // Return flipper to original position

  // Wait for a moment before repeating the process
  delay(1000);
}