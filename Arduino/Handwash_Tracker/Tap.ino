int trigPin = 12;
int echoPin = 13;
int Buzzer = 8;
int duration, distance, dist;
void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(Buzzer, OUTPUT);
}

int checkDistance() {

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration*0.034/2;
  Serial.print(duration);
  Serial.print("\n");
    Serial.print(distance);
  Serial.print("\n");
  return distance;
}


void loop() {

  dist = checkDistance();
  if (distance <= 20)
  {
    for(int i=0; ; ++i) {
      delay(1000);
      dist = checkDistance();
      if(dist > 20 && i<20){
        tone(Buzzer, 400);
        delay(2000);
        noTone(Buzzer);
        break;
      }
      else if (dist > 20)
        break;
    }
  }
  else {
    noTone(Buzzer);
  }
}
