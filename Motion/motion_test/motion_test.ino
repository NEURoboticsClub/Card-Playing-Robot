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
int RPWM_Output = 5; // Arduino PWM output pin 5; connect to IBT-2 pin 1 (RPWM)
int LPWM_Output = 6; // Arduino PWM output pin 6; connect to IBT-2 pin 2 (LPWM)

int pos_res_1 = 60;
int pos_res_2 = 50;
int pos_card_1 = 92;
int pos_card_2 = 120;
int pos_flip_1 = 61; 
int pos_flip_2 =  84; 
int off_set = 20; // Hos much to move the motors to avoid colliding
int pos_small_flip_close = 20;
int pos_small_flip_open = 150;
int pos_suction = 120;


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
  arm1.write(50); // Move servo 1
  arm2.write(70); // Move servo 2
  arm3.write(pos_suction);

  flipperBig.write(0);
  flipperSmall.write(pos_small_flip_open);

  // Suction
  pinMode(RPWM_Output, OUTPUT);
  pinMode(LPWM_Output, OUTPUT);
  analogWrite(RPWM_Output, 0);

}

void loop() {

  // Turn on suction
  // digitalWrite(motorPin, HIGH);
  analogWrite(LPWM_Output, 100);

  // Turn on at resting for a bit
  for (int i = 0 ; i <= 20; i++) {
    arm1.write(pos_res_1); 
    arm2.write(pos_res_2);
    arm3.write(pos_suction);
    delay(10); 
  }

  // Move the arm down to pick up the card
  for (int i = pos_res_1; i >= pos_res_1 - off_set; i--) {
    arm1.write(i); 
    arm2.write(pos_res_2);
    arm3.write(pos_suction); 
    delay(15); 
  }
  
   for (int i = pos_res_2; i <= pos_card_2; i++) {
    arm1.write(pos_res_1 - off_set);
    arm2.write(i);
    arm3.write(pos_suction); 
    delay(15); 
  }

  for (int i = pos_res_1 - off_set; i <= pos_card_1; i++) {
    arm1.write(i); 
    arm2.write(pos_card_2);
    arm3.write(pos_suction);
    delay(15); 
  }

  // Delay to pick up card and turns on motor
  for (int i = 0 ; i <= 10; i++) {
    arm1.write(pos_card_1); 
    arm2.write(pos_card_2);
    arm3.write(pos_suction);
    delay(10); 
  }

  // Move the arm to the flipper
  for (int i = pos_card_1; i >= pos_flip_1; i--) {
    arm1.write(i); 
    arm2.write(pos_card_2);
    arm3.write(pos_suction);
    delay(15); 
  }
  for (int i = pos_card_2; i >= pos_flip_2; i--) {
    arm1.write(pos_flip_1);
    arm2.write(i); 
    arm3.write(pos_suction);
    delay(15); 
  }

  // Close flipper
  for (int i = pos_small_flip_open ; i >= pos_small_flip_close; i--) {
    arm1.write(pos_flip_1); 
    arm2.write(pos_flip_2);
    arm3.write(pos_suction);
    flipperSmall.write(i);
    delay(15); 
  }


  // Turn off suction
  //digitalWrite(valvePin, HIGH);
  //digitalWrite(motorPin, LOW);

  // Move up the arm
  for (int i = pos_flip_1; i >= pos_flip_1 - off_set; i--) {
    arm1.write(i); 
    arm2.write(pos_flip_2);
    arm3.write(pos_suction); 
    delay(15); 
  }
  

  // Flipper faces down
  for (int i = 0; i <= 180; i++) {
    arm1.write(pos_flip_1 - off_set); 
    arm2.write(pos_flip_2);
    arm3.write(pos_suction);
    flipperBig.write(i);
    delay(15); 
  }
/*
  // Turn on the suction
  digitalWrite(valvePin, LOW);
  digitalWrite(motorPin, HIGH);
*/
  // Arm picks up card from flipper
  for (int i = pos_flip_1 - off_set; i <= pos_flip_1; i++) {
    arm1.write(i); 
    arm2.write(pos_flip_2);
    arm3.write(pos_suction);
    delay(15); 
  }

  // Move arm to table
  for (int i = pos_flip_2; i <= pos_card_2; i++) {
    arm1.write(pos_flip_1);
    arm2.write(i);
    arm3.write(pos_suction);
    delay(15); 
  }
  for (int i = pos_flip_1; i <= pos_card_1 ; i++) {
    arm1.write(i); 
    arm2.write(pos_card_2); 
    arm3.write(pos_suction);
    delay(15); 
  }
  /*
  // Turn off suction
  digitalWrite(valvePin, HIGH);
  digitalWrite(motorPin, LOW);
*/

  // Arm goes to rest
  for (int i = pos_card_1; i >= pos_res_1 - off_set; i--) {
    arm1.write(i); 
    arm2.write(pos_card_2);
    arm3.write(pos_suction);
    delay(15); 
  }

   for (int i = pos_card_2; i >= pos_res_2; i--) {
    arm2.write(i);
    arm1.write(pos_res_1 - off_set); 
    arm3.write(pos_suction);
    delay(15); 
  }
  for (int i = pos_res_1 - off_set; i <= pos_res_1; i++) {
    arm1.write(i); 
    arm2.write(pos_res_2);
    arm3.write(pos_suction);
    delay(15); 
  }
  // Flipper faces up
  flipperBig.write(5);
  delay(1000);  // Wait for 1 second

  // Wait for a moment before repeating the process
  delay(1000);
}