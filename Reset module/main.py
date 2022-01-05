import pycom
import time

print('Pycom is reset')

pycom.heartbeat(False)
pycom.rgbled(0xff0000)
time.sleep(1)
pycom.rgbled(0x00ff00)
time.sleep(1)
pycom.rgbled(0x0000ff)
time.sleep(1)
pycom.heartbeat(True)
