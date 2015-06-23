/*
LM35 output connected to PA0. Reads ADC channel 0 in a loop and diplays the result on the LCD in Celcius.   ADC uses internal 2.56 volt reference.
*/

#include "mh-lcd-float.c"
#include "mh-adc.c"
#include "mh-utils.c"

int main()
{
uint16_t    data;
float            mv, temp;

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
    delay_ms(500);              // every 500 milliseconds
    }
}
