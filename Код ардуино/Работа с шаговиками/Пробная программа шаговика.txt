// Простой Arduino-код для проверки шагового двигателя

//простое подключение A4988

//пины reset и sleep соединены вместе

//подключите VDD к пину 3.3 В или 5 В на Arduino

//подключите GND к Arduino GND (GND рядом с VDD)

//подключите 1A и 1B к 1 катушке шагового двигателя

//подключите 2A и 2B к 2 катушке шагового двигателя

//подключите VMOT к источнику питания (9В источник питания + term)

//подключите GRD к источнику питания (9В источник питания - term)

int stp = 13; //подключите 13 пин к step

int dir = 12; //подключите 12 пин к dir

int a = 0;

void setup()

{

pinMode(stp, OUTPUT);

pinMode(dir, OUTPUT);

}

void loop()

{

if (a < 200) // вращение на 200 шагов в направлении 1

{

a++;

digitalWrite(stp, HIGH);

delay(10);

digitalWrite(stp, LOW);

delay(10);

}

else { digitalWrite(dir, HIGH);

a++;

digitalWrite(stp, HIGH);

delay(10);

digitalWrite(stp, LOW);

delay(10);

if (a>400) // вращение на 200 шагов в направлении 2

{

a = 0;

digitalWrite(dir, LOW);

}

}

}
