import pycom
import time

pycom.heartbeat(False)
pycom.rgbled(0xff0000)
time.sleep(4)
pycom.rgbled(0x00ff00)
time.sleep(4)
pycom.rgbled(0x0000ff)
time.sleep(4)
pycom.heartbeat(True)
