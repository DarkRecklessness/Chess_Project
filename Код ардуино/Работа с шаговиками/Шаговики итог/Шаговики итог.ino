#include <AccelStepper.h>

#define EN 8 // stepper motor enable , active low
#define X_DIR 5 // X -axis stepper motor direction control
#define Y_DIR 6 // y -axis stepper motor direction control
#define X_STP 2 // x -axis stepper control
#define Y_STP 3 // y -axis stepper control

#define stepsForOneTurn 200 // Это у nema 17
#define stepByOneCell 200 // Высчитать длину шага и обмотки - [сторона клетки(3,5см) / длина окружности(шкива) * кол-во шагов за оборот(stepsForOneTurn) ]

#define constantSteppersSpeed 200

// Матрица 10 на 16

int stepsArrayX[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9, stepByOneCell * 10, stepByOneCell * 11, stepByOneCell * 12, stepByOneCell * 13, stepByOneCell * 14, stepByOneCell * 15 };
int stepsArrayY[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9 };


AccelStepper StepperX(1, X_STP, X_DIR); // 1 - режим "external driver" (A4988)
AccelStepper StepperY(1, Y_STP, Y_DIR); // 1 - режим "external driver" (A4988)


int inputX = 0; // Тут подаётся индекс для шаговика х
int inputY = 0; // Тут подаётся индекс для шаговика y

String incomingString;

void setup() {
  Serial.begin(9600);

  StepperX.setCurrentPosition(0);
  StepperY.setCurrentPosition(0);  
  
  StepperX.setMaxSpeed(1000); //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperX.setSpeed(constantSteppersSpeed); //устанавливаем ускорение (шагов/секунду^2)

  StepperY.setMaxSpeed(1000); //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperY.setSpeed(constantSteppersSpeed); //устанавливаем ускорение (шагов/секунду^2)

  pinMode (EN, OUTPUT);
  digitalWrite (EN, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    incomingString = Serial.readString();
    Serial.println(incomingString.length());

    char charY = incomingString.charAt(1);
    inputY = charY - '0'; // мощный перевод из char в int
    Serial.println(inputY);
    
    if (incomingString.length() == 7) {
      char charX = incomingString.charAt(4);
      inputX = charX - '0';
    } else if (incomingString.length() == 8) {
      char charX1 = incomingString.charAt(4);
      Serial.println(charX1);
      char charX2 = incomingString.charAt(5);
      Serial.println(charX2);
      inputX = (charX1 - '0') * 10 + (charX2 - '0');
      Serial.println(inputX);
    } else {
      Serial.println("Чухня происходит какая-то");
    }
    if (StepperX.distanceToGo() == 0) {
      StepperX.moveTo(stepsArrayX[inputX]); //moveTo
      StepperY.moveTo(stepsArrayY[inputX]);
      StepperX.setSpeed(constantSteppersSpeed);
      StepperY.setSpeed(constantSteppersSpeed);
    }
    
  }

  /*
  if(StepperX.distanceToGo()==0) //проверка, отработал ли двигатель предыдущее движение
  {
      StepperX.move(1600*dir); //устанавливает следующее перемещение на 1600 шагов (если dir равен -1 будет перемещаться -1600 -> противоположное направление)
      dir = dir*(-1); //отрицательное значение dir, благодаря чему реализуется вращение в противоположном направлении
      delay(1000); //задержка на 1 секунду
  }
  */
  
  StepperX.runSpeedToPosition();
  StepperY.runSpeedToPosition();
} // (2, 5)




