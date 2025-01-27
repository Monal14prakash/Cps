#include<DHT.h>
#include<Adafruit_SSD1306.h>
#define DHTPIN 4
#define DHTTYPE DHT11
Adafruit_SSD1306 display(128,64,&Wire,-1);
DHT dht(DHTPIN,DHTTYPE);

void setup() {
// put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
  if(!display.begin(SSD1306_SWITCHCAPVCC,0X3C))
  {
    Serial.println("oled init failed");
    while(true)
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
}

void loop() {
// put your main code here, to run repeatedly:
float humidity=dht.readHumidity();
float temperature=dht.readTemperature();
Serial.print("temperature: ")
Serial.println(temperature)
Serial.print("humidity: ")
display.clearDisplay();
display.setCursor(0,0);
display.print("temp:");
display.println(temperature);
display.print("humi");
display.println(humidity);
display.display();
delay(200);
}
