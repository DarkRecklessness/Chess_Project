#include <AccelStepper.h>

// For CNC v.3
#define EN 8     // stepper motor enable , active low

#define X_DIR 5  // X -axis stepper motor direction control
#define X_STP 2  // x -axis stepper control

#define Y_DIR 6  // y -axis stepper motor direction control
#define Y_STP 3  // y -axis stepper control


AccelStepper Stepper1(1, X_STP, X_DIR); // 1 - режим "external driver" (A4988)

int dir = 1; //используется для смены направления

void setup() {

Stepper1.setMaxSpeed(1000); //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
Stepper1.setSpeed(200);

pinMode(EN, OUTPUT);
digitalWrite(EN, LOW);
// Stepper1.setAcceleration(200); //устанавливаем ускорение (шагов/секунду^2)

}

void loop() {

if(Stepper1.distanceToGo()==0){ //проверка, отработал ли двигатель предыдущее движение

Stepper1.move(1600*dir); //устанавливает следующее перемещение на 1600 шагов (если dir равен -1 будет перемещаться -1600 -> противоположное направление)

dir = dir*(-1); //отрицательное значение dir, благодаря чему реализуется вращение в противоположном направлении

delay(1000); //задержка на 1 секунду

}

Stepper1.runSpeedToPosition(); //запуск шагового двигателя. Эта строка повторяется вновь и вновь для непрерывного вращения двигателя. Без ускорения.

}
