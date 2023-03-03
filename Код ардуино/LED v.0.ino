#define incorrectLedPin 12
#define timerMoveLedPin A0

bool flagIncorrectMove = true;

unsigned long int timer = 0;
unsigned long int timerForMove = 0;
unsigned long const timeForOneMove = 4000;

void setup() 
{
  Serial.begin(9600);
  pinMode(incorrectLedPin, OUTPUT);
  pinMode(timerMoveLedPin, OUTPUT);
}

void loop() 
{
  if (millis() - timer >= 1000) {
    flagIncorrectMove = !flagIncorrectMove;
    timer = millis();
  }
  if (flagIncorrectMove) {
    digitalWrite(incorrectLedPin, HIGH);
  } else {
    digitalWrite(incorrectLedPin, LOW);
  }

  if (millis() - timerForMove >= timeForOneMove) {
    timerForMove = millis();
  }
  int x = map((millis() - timerForMove), 0, timeForOneMove, 0, 255);
  Serial.println(x);
  analogWrite(timerMoveLedPin, 255 - x);

}