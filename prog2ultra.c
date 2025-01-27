#include<WIRE.h>
#include<Adafruit_GFX.h>
#include<Adafruit_SSD1306.h>

#define trigpin 12
#define echopin 13
#define buzzerpin 14

Adafruit_SSD1306(128,64,&WIRE,-1);

#define threshold 10
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
  pinMode(buzzerpin,OUTPUT);
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.display();
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigpin,LOW);
  delayMicroSeconds(2);
  digitalWrite(trigpin,HIGH);
  delayMicroseconds(2);
  digitalWrite(trigpin,LOW);

  long duration=pulseIn(echopin,HIGH);
  float distance=duration*0.034/2;
  display.clearDisplay();
  display.setCursor(0,0);
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.display();

  }
