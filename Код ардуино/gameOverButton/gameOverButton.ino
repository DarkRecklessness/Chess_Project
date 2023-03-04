#define gameOverButtonPin 7

void setup()
{
  pinMode(gameOverButtonPin, INPUT_PULLUP);
  // Из-за INPUT_PULLUP подключения при разжатой кнопке считывается высокое напряжение
  pinMode(13, OUTPUT); // просто для проверки работоспособности программы
}

void loop()
{
  if (digitalRead(gameOverButtonPin) == LOW) { // Если кнопку нажали
  	 // Происходит запуск функции gameOver
    digitalWrite(13, HIGH);
  } else {
  	digitalWrite(13, LOW);  
  }
}