/*
LM35 output connected to PA0. Reads ADC channel 0 in a loop. Connect heater control relay to PB0
Diplays the result on the LCD in Celcius. 
 ADC uses internal 2.56 volt reference.
*/

#include "mh-lcd-float.c"
#include "mh-adc.c"
#include "mh-utils.c"

#define   SPUPPER      30.5      // temperature set point upper and lower
#define   SPLOWER     30.0     //  a window is needed to avoid relay chattering

int main()
{
uint16_t    data;
float            mv, temp;
DDRB = 1;

lcd_init();
adc_enable();
adc_set_ref(REF_INT);          // Set to use the internal reference 2.56V

while(1)
    {
    data = read_adc(0);   		// Read voltage at PA0
    mv = 2560.0/1023 * data ;   // convert to millivolts.  2560  millivolts corresponds to 1023
    lcd_clear();                // write data to LCD
    temp = 0 + mv / 10;         // 10 mV / deg C, LM35 is calibrated in C
    lcd_put_float(temp,1);      // one decimal place
    lcd_put_char('C');
    if (temp > SPUPPER)          // switch off the heater 
             PORTB = 0;
    else 
    if (temp < SPLOWER)         // switch on the heater
             PORTB = 1;
    delay_ms(500);              // every 500 milliseconds
    }
}
