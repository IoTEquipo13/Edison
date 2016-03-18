# pot_touch_led_lcd.py
 
import pyupm_i2clcd as lcd
import mraa
import time
import sys
 
# analog input - pot
potPin = 0
pot = mraa.Aio(potPin)
potVal = 0
 
# digital output - led
ledPin = mraa.Gpio(4)
ledPin.dir(mraa.DIR_OUT)
ledPin.write(0)
 
# digital input - touch
touchPin = mraa.Gpio(3)
touchPin.dir(mraa.DIR_IN)
 
# display - lcd
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
 
while 1:

    while touchPin.read() == 1:   

        # turn led on
        ledPin.write(1)
       
        # read pot/print/convert to string/display on lcd
        potVal = float(pot.read())
        #print potVal   
        #potStr = str(potVal)
        if potVal:
            lcdDisplay.setCursor(0, 0)
            lcdDisplay.setColor(255, 0, 0)
            lcdDisplay.write("No parking space")

        lcdDisplay.setCursor(0, 0)
        lcdDisplay.setColor(0, 255, 0)
        lcdDisplay.write("Available parking spaces") 


        time.sleep(1)

    # turn led off
    ledPin.write(0)
