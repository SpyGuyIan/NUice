/** Thermistor Library
 * -  Author - Daniel McGann 2019
 */

#ifndef _THERMISTOR_H_
#define _THERMISTOR_H_

#include <Arduino.h>
#include "temp_sense.h"

class Thermistor : public TempSensor{
  public:
    // Constructor
    Thermistor(uint8_t pin, uint16_t b_coef, uint16_t therm_res,
              uint16_t series_res);

    // Reads and return temperature
    float read();

  private:
    /// Analogue in Pin
    uint8_t pin_;
    uint16_t b_coef_;
    uint16_t therm_res_;
    uint16_t series_res_;
};

#endif /* _THERMISTOR_H_ */
