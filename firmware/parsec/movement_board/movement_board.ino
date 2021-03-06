
#include <Arduino.h>
#include <NUros.h>
#include <NU_GPIO.h>
#include <NU_DCMotor_DRV8701.h>
#include <NU_QuadratureEncoder.h>


ros::NUNodeHandle nh;

NUGPIO led(nh, "led", PA9, OUTPUT);
NUDRV8701Driver carosel_mot(nh, "carosel", 2);//M2
NUDRV8701Driver brake1(nh, "brake1", 3);//M3
// NUDRV8701Driver brake2(nh, "brake2", 1);//M1

// NUGPIO led(nh, "carosel_lim", PA10, OUTPUT);
// NUQuadratureEncoder carosel_enc(nh, "carosel", a, b);

void setup(){
    nh.getHardware()->setBaud(115200);
    nh.initNode();
    led.setup();
    carosel_mot.setup();
    brake1.setup();
}


void loop(){
    nh.spinOnce();
    led.update();
    carosel_mot.update();
    brake1.update();
}