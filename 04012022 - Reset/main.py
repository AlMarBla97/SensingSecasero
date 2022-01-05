import pycom
import time

pycom.heartbeat(False)
pycom.rgbled(0x999900)
time.sleep(4)
pycom.rgbled(0x00ff00)
time.sleep(4)
pycom.heartbeat(True)
#modifico en el ordenador y a ver si se me sube bien al github online.
#modifico esto en la ramav1, y a ver que pasa
#Meto esto en el master, a ver ha conflicto con diseñador.
#Esto lo meto desde Diseñador 2. 
