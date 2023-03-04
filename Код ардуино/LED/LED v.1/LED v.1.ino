#define incorrectLedPin 12
#define timerMoveLedPin 3

#define timeForExceedingTimeLimit 90000  
#define timeForOnlyOneMove 120000


bool flagStartMove = false; //true
bool flagTimerWasReset = false;

unsigned long int timerForMove = 0;
 

String incomingString;

void setup() 
{
  Serial.begin(9600);
  pinMode(incorrectLedPin, OUTPUT);
  pinMode(timerMoveLedPin, OUTPUT);
}

void loop() 
{
  //Считывание значений с сериал порта
  if (Serial.available() > 0) {
  	incomingString = Serial.readString();
    Serial.println(incomingString);
  }
  
  //Лампочка incorrect path
  if (incomingString == "incorrect path") {
    incomingString = "";
    digitalWrite(incorrectLedPin, HIGH);
    delay(2000);
    digitalWrite(incorrectLedPin, LOW);
  }

  // Лампочка timer
  if (flagStartMove && !flagTimerWasReset) {
    timerForMove = millis();
    flagTimerWasReset = true;
  }
  if (flagStartMove && (millis() - timerForMove >= timeForExceedingTimeLimit)) {
    if (millis() - timerForMove <= timeForOnlyOneMove) {
      digitalWrite(timerMoveLedPin, HIGH);
    } else {
      digitalWrite(timerMoveLedPin, LOW);
      flagStartMove = false;
      flagTimerWasReset = false;
      // Ещё дополнительный код в случае окончания времени
    }
  }
}










