import pycom
import time

pycom.heartbeat(False)
pycom.rgbled(0x00ff00)
time.sleep(4)
pycom.heartbeat(True)