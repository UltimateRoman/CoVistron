#include <Servo.h>
Servo servo1;
int trigPin = 9;
int echoPin = 8;
int distance;
int duration;
 
void setup() 
{
servo1.attach(7); 
 pinMode(trigPin, OUTPUT);
 pinMode(echoPin, INPUT);
}
 
void loop() {
  ultra();
  servo1.write(0);
  if(distance <= 10){
  servo1.write(90);
  delay(1000)
  }
}
 
void ultra(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration*0.034/2;
  }
