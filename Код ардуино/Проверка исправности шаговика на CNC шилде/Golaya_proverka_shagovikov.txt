#define EN 8     // stepper motor enable , active low
#define X_DIR 5  // X -axis stepper motor direction control
#define Y_DIR 6  // y -axis stepper motor direction control
#define X_STP 2  // x -axis stepper control
#define Y_STP 3  // y -axis stepper control

int a = 0;

void setup()

{

  pinMode(X_DIR, OUTPUT);

  pinMode(X_STP, OUTPUT);

  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);  
}

void loop()

{

  if (a < 200)  // вращение на 200 шагов в направлении 1

  {

    a++;

    digitalWrite(stp, HIGH);

    delay(10);

    digitalWrite(stp, LOW);

    delay(10);

  }

  else {
    digitalWrite(dir, HIGH);

    a++;

    digitalWrite(stp, HIGH);

    delay(10);

    digitalWrite(stp, LOW);

    delay(10);

    if (a > 400)  // вращение на 200 шагов в направлении 2

    {

      a = 0;

      digitalWrite(dir, LOW);
    }
  }
}