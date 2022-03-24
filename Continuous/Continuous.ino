/*
This example shows how to take simple range measurements with the VL53L1X. The
range readings are in units of mm.
*/

#include <Wire.h>
#include "VL53L1X.h"
#include <Bridge.h>
#include <Process.h>
#include <Console.h>


VL53L1X sensor;
int count = 0;
int red_light_pin= 9;
int green_light_pin = 10;
int blue_light_pin = 11;

void setup()
{
  while (!Serial) {}
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(400000); // use 400 kHz I2C
  
  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1);
  }

  // Use long distance mode and allow up to 50000 us (50 ms) for a measurement.
  // You can change these settings to adjust the performance of the sensor, but
  // the minimum timing budget is 20 ms for short distance mode and 33 ms for
  // medium and long distance modes. See the VL53L1X datasheet for more
  // information on range and timing limits.
  sensor.setDistanceMode(VL53L1X::Long);
  sensor.setMeasurementTimingBudget(50000);

  // Start continuous readings at a rate of one measurement every 50 ms (the
  // inter-measurement period). This period should be at least as long as the
  // timing budget.
  sensor.startContinuous(50);
   
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
}

void loop()
{
  int distance = sensor.read();
  if (distance > 200 && distance < 300) {
    ++count;
  }
  else {
    count = 0;
    RGB_color(255, 0, 0); // Red
    Serial.println("stop");  

  }
  if (count == 15) {
//    Serial.println();
//    Serial.print("Object detected at: ");
//    Serial.print(distance);
    Serial.print("run");
    Serial.println();
    RGB_color(0, 0, 255); // Blue
  }
  else if (count > 0 && count < 15) {
    //Serial.print(".");
    RGB_color(255,255,255); //White
  }

  
  
//  Serial.print(sensor.read());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  
  delay(100);
}

void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}
