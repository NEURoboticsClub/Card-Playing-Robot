#include <Servo.h>
//#include <iostream>
using namespace std;
Servo myservo;
int val;
int pos = 0;
void setup() {
  // put your setup code here, to run once:
myservo.attach(11);
}

void loop() {
  // put your main code here, to run repeatedly:
for (pos = 0; pos <= 45; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 45; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
