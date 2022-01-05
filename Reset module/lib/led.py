import pycom
import time

print('Enter in Led')
pycom.heartbeat(False)

def redled(t):
    print('Enter in led def')
    pycom.rgbled(0xff0000)
    time.sleep(t)

