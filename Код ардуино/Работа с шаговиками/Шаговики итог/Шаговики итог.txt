#include <AccelStepper.h>

#define stepper1DirPin 1
#define stepper1StepPin 2
#define stepper2DirPin 3
#define stepper2StepPin 4


#define stepsForOneTurn 200 // Это у nema 17
#define stepByOneCell 0 // Высчитать длину шага и обмотки - [сторона клетки(3,5см) / длина окружности(шкива) * кол-во шагов за оборот(stepsForOneTurn) ]


// Матрица 10 на 16

int stepsArrayX[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9, stepByOneCell * 10, stepByOneCell * 11, stepByOneCell * 12, stepByOneCell * 13, stepByOneCell * 14, stepByOneCell * 15 };
int stepsArrayY[] = { 0, stepByOneCell, stepByOneCell * 2, stepByOneCell * 3, stepByOneCell * 4, stepByOneCell * 5, stepByOneCell * 6, stepByOneCell * 7, stepByOneCell * 8, stepByOneCell * 9 };


AccelStepper StepperX(1, stepper1StepPin, stepper1DirPin); // 1 - режим "external driver" (A4988)
AccelStepper StepperY(1, stepper2StepPin, stepper2DirPin); // 1 - режим "external driver" (A4988)


int inputX = 0; // Тут подаётся индекс для шаговика х
int inputY = 0; // Тут подаётся индекс для шаговика y


void setup() {

    StepperX.setMaxSpeed(1000); //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
    StepperX.setAcceleration(200); //устанавливаем ускорение (шагов/секунду^2)

    StepperY.setMaxSpeed(1000); //устанавливаем максимальную скорость вращения ротора двигателя (шагов/секунду)
    StepperY.setAcceleration(200); //устанавливаем ускорение (шагов/секунду^2)

}

void loop() {

    /*
    if(StepperX.distanceToGo()==0) //проверка, отработал ли двигатель предыдущее движение
    {
        StepperX.move(1600*dir); //устанавливает следующее перемещение на 1600 шагов (если dir равен -1 будет перемещаться -1600 -> противоположное направление)
        dir = dir*(-1); //отрицательное значение dir, благодаря чему реализуется вращение в противоположном направлении
        delay(1000); //задержка на 1 секунду
    }

    StepperX.run(); //запуск шагового двигателя. Эта строка повторяется вновь и вновь для непрерывного вращения двигателя
    */

    StepperX.moveTo(stepsArrayX[inputX])
    StepperY.moveTo(stepsArrayY[inputX])




}
