import time, sys, signal, atexit
import pyupm_grovegsr as upmGrovegsr
import pyupm_i2clcd as lcd

# Tested with the GroveGSR Galvanic Skin Response Sensor module.

# Instantiate a GroveGSR on analog pin A0
myGSR = upmGrovegsr.GroveGSR(0)


## Exit handlers ##
# This stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
	raise SystemExit

# This lets you run code on exit, including functions from myGSR
def exitHandler():
	print "Exiting"
	sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

# display - lcd
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)

print "Calibrating...."
myGSR.calibrate()

while (1):
	print myGSR.value()

	if(myGRS.value() != 0)
		flag = 1

	while myGSR.value() != 0:

		lcdDisplay.setCursor(0, 0)
	    lcdDisplay.setColor(255, 0, 0)
	    lcdDisplay.write("No parking space")

    lcdDisplay.setCursor(0, 0)
    lcdDisplay.setColor(0, 255, 0)
    lcdDisplay.write("Available parking spaces") 

time.sleep(.5)