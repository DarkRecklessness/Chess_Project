#include <AccelStepper.h>

#define stepper1DirPin 1
#define stepper1StepPin 2
#define stepper2DirPin 3
#define stepper2StepPin 4

#define enablePin 98237456987324568982347


#define stepsForOneTurn 200  // Это у nema 17

#define stepByOneCell 200  // Высчитать длину шага и обмотки - [сторона клетки(3,5см) / длина окружности(шкива) * кол-во шагов за оборот(stepsForOneTurn) ]
// для проверки выставил 200

// Матрица 10 на 16

int stepsArrayX[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9, stepByOneCell * 10, stepByOneCell * 11, stepByOneCell * 12, stepByOneCell * 13, stepByOneCell * 14, stepByOneCell * 15 };
int stepsArrayY[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9 };


AccelStepper StepperX(1, stepper1StepPin, stepper1DirPin);  // 1 - режим "external driver" (A4988)
AccelStepper StepperY(1, stepper2StepPin, stepper2DirPin);  // 1 - режим "external driver" (A4988)


int inputX = 0;  // Тут подаётся индекс для шаговика х
int inputY = 0;  // Тут подаётся индекс для шаговика y

String incomingString;

void setup() {
  Serial.begin(9600);

  StepperX.setMaxSpeed(1000);     //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperX.setSpeed(200);  

  StepperY.setMaxSpeed(1000);     //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperY.setSpeed(200);  

  pinMode(enablePin, OUTPUT);
  digitalWrite(enablePin, LOW); // По крайней мере для CNC шилда нужен LOW сигнал для начала работы
}

void loop() {
  if (Serial.available() > 0) {
    incomingString = Serial.readString();
    Serial.println(incomingString);

    checkingInput();
  }

  StepperX.runSpeedToPosition();
  StepperY.runSpeedToPosition();
}

void checkingInput() {
  char charY = incomingString.charAt(1);
  inputY = charY - '0';  // мощный перевод из char в int

  if (incomingString.length() == 6) {
      char charX = incomingString.charAt(4);
      inputX = charX - '0';
  } else if (incomingString.length() == 7) {
      char charX1 = incomingString.charAt(4);
      char charX2 = incomingString.charAt(5);
      inputX = (charX1 - '0') * 10 + (charX2 - '0');
  } else {
    Serial.println("Чухня происходит какая-то");
    return;
  }

  StepperX.moveTo(stepsArrayX[inputX])
  StepperY.moveTo(stepsArrayY[inputX])
}
