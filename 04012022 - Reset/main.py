import pycom
import time

pycom.heartbeat(False)
pycom.rgbled(0x999900)
time.sleep(4)
pycom.heartbeat(True)
