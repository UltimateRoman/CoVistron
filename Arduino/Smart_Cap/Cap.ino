int trigPin = 12;
int echoPin = 13;
int Buzzer = 8;
int duration, distance;
void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(Buzzer, OUTPUT);
}

void loop() {

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration*0.034/2;
  if (distance <= 25)
  {
    tone(Buzzer, 400);
  }
  else {
    noTone(Buzzer);
  }
}
