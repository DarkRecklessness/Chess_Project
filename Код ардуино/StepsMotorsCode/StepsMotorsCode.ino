#define GS_NO_ACCEL                         // отключить модуль движения с ускорением (уменьшить вес кода)
#define DRIVER_STEP_TIME 1  // меняем задержку на 1 мкс для a4988

#include "GyverStepper2.h"




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

#define steps_nema_17 200 

GStepper2< STEPPER2WIRE> stepper1(steps_nema_17, X_STEP_PIN , X_DIR_PIN, X_ENABLE_PIN);
//GStepper2< STEPPER2WIRE> stepper2(steps_nema_17, Y_STEP_PIN , Y_DIR_PIN, Y_ENABLE_PIN);


bool dir = 1;


void setup() {
  Serial.begin(9600);

  stepper1.setMaxSpeed(300); // 1,5 оборота шкива - 540 градусов шаговика
  //stepper2.setMaxSpeed(300);
  stepper1.enable();
  //stepper2.enable();

  /*
  pinMode(X_STEP_PIN  , OUTPUT);
  pinMode(X_DIR_PIN   , OUTPUT);
  pinMode(Y_STEP_PIN  , OUTPUT);
  pinMode(Y_DIR_PIN   , OUTPUT);
  */
}

void loop() {
  // Надо сделать ещё проверку на шаговики, пример в самом низу

  stepper1.tick();
  //stepper2.tick();

  if (stepper1.ready()) {
    dir = !dir;
    stepper1.setTarget(dir * 300);
  }

  static uint32_t tmr;
  if (millis() - tmr >= 30) {
    tmr = millis();
    Serial.println(stepper1.pos);
  }


}

/*
http://arduino.on.kg/forum/post/61/#p61
*/
