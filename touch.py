import time, sys, signal, atexit
import pyupm_grovegsr as upmGrovegsr

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


print "Calibrating...."
myGSR.calibrate()

while (1):
	print myGSR.value()
	time.sleep(.5)
