/* 
Три типа ошибок: Программная ошибка, неисправное оборудование, кривые руки (неправильное подключение) 
Возможные ошибки:
1. Проверить с помощью другой программы (Check_one_stepper_CNC) или крайним вариантом прямой подачей сигналов (Golaya_proverka_shagovikov)
2. Неисправная аппаратура
Решение: проверить простыми программами, если окажется так, поменять двигатель или драйвер
    После решения основной проблемы: 
1. Неправильно считывает из строки
Решение: добавил вывод в Serial полученных значений, если ошибка в этом поменять в длине 6 и 7 на 7 и 8
2. Неправильные команды для шаговиков
Решение: попробывать прогу прямо как из примера (про концевики)
*/


#include <AccelStepper.h>

#define EN 8     // stepper motor enable , active low
#define X_DIR 5  // X -axis stepper motor direction control
#define Y_DIR 6  // y -axis stepper motor direction control
#define X_STP 2  // x -axis stepper control
#define Y_STP 3  // y -axis stepper control
#define home_switch_x 9 // концевик X_ENDSTOP
#define home_switch_y 10 // концевик Y_ENDSTOP


#define electroMagnetPin 13 // поменять


#define stepsForOneTurn 200  // Это у nema 17
#define stepByOneCell 159    // Высчитать длину шага и обмотки - [сторона клетки(3,5см) / длина окружности(шкива)(диаметр - 1,4см) * кол-во шагов за оборот(stepsForOneTurn) ]

#define constantSteppersSpeed 200
#define homingSteppersSpeed 100

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

  pinMode(electroMagnetPin, OUTPUT);

  pinMode(home_switch_x, INPUT_PULLUP);
  pinMode(home_switch_y, INPUT_PULLUP);

  delay(5);  // Wait for everything wake up

  StepperX.setCurrentPosition(0);
  StepperY.setCurrentPosition(0);

  StepperX.setMaxSpeed(1000);                //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperX.setSpeed(homingSteppersSpeed);  //устанавливаем скорость вращения ротора двигателя (шагов/секунду) для хоминга

  StepperY.setMaxSpeed(1000);                //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
  StepperY.setSpeed(homingSteppersSpeed);  //устанавливаем скорость вращения ротора двигателя (шагов/секунду) для хоминга

  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);

  /*
  // Begin of homing
  
  //                                    StepperX
  
  Serial.println("StepperX is Homing . . . . . . . . . . . ");
  while (digitalRead(home_switch_x)) {  // Make the Stepper move CCW until the switch is activated
    StepperX.move(-1);  // Set the position to move
    StepperX.setSpeed(homingSteppersSpeed);
    StepperX.runSpeedToPosition();  // Start moving the stepper
    delay(5);
  }
  
  // Кнопка нажата, двигаем пока не разомкнётся
  while (!digitalRead(home_switch_x)) {  // Make the Stepper move CW until the switch is deactivated
    StepperX.move(1);  // Set the position to move
    StepperX.setSpeed(homingSteppersSpeed);
    StepperX.runSpeedToPosition();  // Start moving the stepper
    delay(5);
  }

  StepperX.setCurrentPosition(0);
  Serial.println("StepperX Homing Completed");
  Serial.println("");

  ///*
  //                                    StepperY

  Serial.println("StepperY is Homing . . . . . . . . . . . ");
  while (digitalRead(home_switch_y)) {  // Make the Stepper move CCW until the switch is activated
    StepperY.move(-1);  // Set the position to move
    StepperY.setSpeed(homingSteppersSpeed);
    StepperY.runSpeedToPosition();  // Start moving the stepper
    delay(5);
  }
  
  // Кнопка нажата, двигаем пока не разомкнётся
  while (!digitalRead(home_switch_y)) {  // Make the Stepper move CW until the switch is deactivated
    StepperY.move(1);  // Set the position to move
    StepperY.setSpeed(homingSteppersSpeed);
    StepperY.runSpeedToPosition();  // Start moving the stepper
    delay(5);
  }

  StepperY.setCurrentPosition(0);
  Serial.println("StepperY Homing Completed");
  Serial.println("");
  */

  StepperX.setSpeed(constantSteppersSpeed);
  StepperY.setSpeed(constantSteppersSpeed);
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
        Serial.print("InputY: ");
        Serial.println(inputY);
        Serial.print("InputX: ");
        Serial.println(inputX);

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

  if ((StepperX.distanceToGo() != 0)) {
    StepperX.runSpeedToPosition();
  }

  if ((StepperY.distanceToGo() != 0)) {
    StepperY.runSpeedToPosition();
  }

}
