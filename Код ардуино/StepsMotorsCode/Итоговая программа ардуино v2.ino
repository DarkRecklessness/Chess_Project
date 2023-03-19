#include <AccelStepper.h>

#define EN 8     // stepper motor enable , active low
#define X_DIR 5  // X -axis stepper motor direction control
#define Y_DIR 6  // y -axis stepper motor direction control
#define X_STP 2  // x -axis stepper control
#define Y_STP 3  // y -axis stepper control

#define electroMagnetPin 13 // поменять

#define stepsForOneTurn 200  // Это у nema 17
#define stepByOneCell 200    // Высчитать длину шага и обмотки - [сторона клетки(3,5см) / длина окружности(шкива) * кол-во шагов за оборот(stepsForOneTurn) ]

#define constantSteppersSpeed 200

// Матрица 10 на 16

int stepsArrayX[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9, stepByOneCell * 10, stepByOneCell * 11, stepByOneCell * 12, stepByOneCell * 13, stepByOneCell * 14, stepByOneCell * 15 };
int stepsArrayY[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9 };


AccelStepper StepperX(1, X_STP, X_DIR);  // 1 - режим "external driver" (A4988)
AccelStepper StepperY(1, Y_STP, Y_DIR);  // 1 - режим "external driver" (A4988)


// int inputX = 0; // Тут подаётся индекс для шаговика х
// int inputY = 0; // Тут подаётся индекс для шаговика y

String incomingString;

#define masLength 50 //максимальная очередь

int masX[masLength];
int masY[masLength];

int crutchCounter = 0;

bool magnetFlag = false;

void setup() {
  Serial.begin(9600);

  StepperX.setCurrentPosition(0);
  StepperY.setCurrentPosition(0);

  StepperX.setMaxSpeed(1000);                //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperX.setSpeed(constantSteppersSpeed);  //устанавливаем скорость вращения ротора двигателя (шагов/секунду)

  StepperY.setMaxSpeed(1000);                //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperY.setSpeed(constantSteppersSpeed);  //устанавливаем скорость вращения ротора двигателя (шагов/секунду)

  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);

  pinMode(electroMagnetPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String incomingString = Serial.readString();
    Serial.println(incomingString);
    //Serial.println(incomingString.length());
    
    int index1;
    for (int i = 0; i < (incomingString.length()); i++) {  // Т.к. sizeof возвращает вес, а не размер массива
      if (incomingString.charAt(i) == '(') { index1 = i; }
      if (incomingString.charAt(i) == ')') {
        String moveString;
        for (int j = index1; j < i + 1; j++) {
          moveString.concat(incomingString.charAt(j));
        }

        int inputX = 0;  // Тут подаётся индекс для шаговика х
        int inputY = 0;  // Тут подаётся индекс для шаговика y

        char charY = moveString.charAt(1);
        inputY = charY - '0';  // мощный перевод из char в int

        if (moveString.length() == 6) { // 7 при ошибках
          char charX = moveString.charAt(4);
          inputX = charX - '0';
        } else if (moveString.length() == 7) { // 8 при ошибках
          char charX1 = moveString.charAt(4);
          char charX2 = moveString.charAt(5);
          inputX = (charX1 - '0') * 10 + (charX2 - '0');
        } else {
          Serial.println("Чухня происходит какая-то");
          return;
        }

        masX[crutchCounter] = inputX;
        masY[crutchCounter] = inputY;

        crutchCounter++;
      }
    }
  }

  if (crutchCounter != 0 && StepperX.distanceToGo() == 0 && StepperY.distanceToGo() == 0) {
    if (magnetFlag) {
      digitalWrite(electroMagnetPin, HIGH);
    } else {
      digitalWrite(electroMagnetPin, LOW);
    }
    magnetFlag = !magnetFlag;
    
    StepperX.moveTo(stepsArrayX[masX[0]]);
    StepperY.moveTo(stepsArrayY[masY[0]]);
    StepperX.setSpeed(constantSteppersSpeed);
    StepperY.setSpeed(constantSteppersSpeed);
    for (int i = 0; i < (masLength - 1); i++) {
      byte temp = masX[i];
      masX[i] = masX[i + 1];
      masX[i + 1] = temp;
      temp = masY[i];
      masY[i] = masY[i + 1];
      masY[i + 1] = temp;
    }
    crutchCounter--;

    // for (int i = 0; i < masLength; i++) {
    //   Serial.print(i);
    //   Serial.print(": ");
    //   Serial.print(masX[i]);
    //   Serial.print(", ");
    //   Serial.println(masY[i]);
    // }
  }

  StepperX.runSpeedToPosition();
  StepperY.runSpeedToPosition();
}
