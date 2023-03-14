int data;
String mas;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(53, OUTPUT);
  pinMode(12, OUTPUT);
  //digitalWrite(53, LOW);
  Serial.println("hghgh");

}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()){
    data = Serial.read();
    //Serial.println(data);
    mas += data;
    mas += " ";
    if (data == '+'){
      digitalWrite(53, HIGH);
      mas = "";
    }
    else if (data == '!'){
      digitalWrite(12, HIGH);
      delay(1500);
      digitalWrite(12, LOW);
    }
    else if (data == '-'){
      digitalWrite(53, LOW);
      Serial.println(mas);
      mas = "";
    }
    
  }
    
}
