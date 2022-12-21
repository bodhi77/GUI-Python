//#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>
//LiquidCrystal_I2C lcd(0x27, 20, 4);
SoftwareSerial mySerial(15, 14);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  mySerial.begin(115200);
//  lcd.init();
//  lcd.backlight();
}
//
void loop() {
  String msg = mySerial.readStringUntil('\r');
//  lcd.setCursor(0,0);
//  lcd.print("Received: ");
//  lcd.print(msg);
  if(mySerial.available()>0){
    Serial.println("Hallo ");
    Serial.print(msg);
  }
//  
//  Serial.println(14);
//  delay(500);
}

//void setup(){
//  Serial.begin(9600);
//  while(!Serial);
//  Serial.println("Gasss");
//}
//
//void loop(){
//  if(Serial.available()>0){
//    int state = Serial.parseInt();
//    Serial.println("Hola");
//    Serial.println(state);
//  }
//}
