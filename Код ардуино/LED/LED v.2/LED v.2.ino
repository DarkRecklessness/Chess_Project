#define incorrectLedPin 12
#define timerMoveLedPin 3
#define voiceRepeatLedPin 7
#define voiceBeginLedPin 9

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
  pinMode(voiceRepeatLedPin, OUTPUT);
  pinMode(voiceBeginLedPin, OUTPUT);
}

void loop() 
{
  //Считывание значений с сериал порта
  if (Serial.available() > 0) {
  	incomingString = Serial.readString();
    Serial.println(incomingString);
  }
  
  //Лампочка начала голосового ввода
  if (incomingString == "Enter g") {
    digitalWrite(voiceBeginLedPin, HIGH);
  } else if (incomingString == "incorrect path") { //Лампочка incorrect path
    incomingString = "";
    digitalWrite(incorrectLedPin, HIGH);
    delay(2000);
    digitalWrite(incorrectLedPin, LOW);
  } else if (incomingString == "repeat pls") { //Ламочка repeat pls
    incomingString = "";
    digitalWrite(voiceRepeatLedPin, HIGH);
    delay(2000);
    digitalWrite(voiceRepeatLedPin, LOW);
  } else { //Ламочка repeat pls
    incomingString = "";
    digitalWrite(voiceBeginLedPin, LOW);
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










