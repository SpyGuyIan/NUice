
#include <Arduino.h>
#include <NUros.h>

#include <NU_GPIO.h>
#include <NU_HallEffect.h>
#include <NU_Loadcell.h>


ros::NUNodeHandle nh;

NUGPIO led(nh, "led", PA9, OUTPUT);

NULoadcell lc(nh, "drill_loadcell", PB15, PC6, 2915.0f); //J5, Newtons
NUHallEffect he(nh, "drill_hall", PB8);//J10

void setup(){
    nh.getHardware()->setBaud(115200);
    nh.initNode();
    led.setup();
    lc.setup();
    he.setup();
}


void loop(){
    nh.spinOnce();
    led.update();
    lc.update();
    he.update();
}