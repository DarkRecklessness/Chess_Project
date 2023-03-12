#include <AccelStepper.h>

// For RAMPS 1.4
#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN           2

#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          15

AccelStepper Stepper1(1, X_STEP_PIN, X_DIR_PIN); // 1 - режим "external driver" (A4988)

int dir = 1; //используется для смены направления

void setup() {

Stepper1.setMaxSpeed(1000); //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
Stepper1.setSpeed(200);

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
