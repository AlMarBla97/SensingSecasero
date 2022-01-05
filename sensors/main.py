import machine
import utime
import time
import pycom
from pycoproc_2 import Pycoproc

from MPL3115A2 import MPL3115A2,PRESSURE,ALTITUDE
from SI7006A20 import SI7006A20



py = Pycoproc()

WifiName='OnePlus 6'                        #datos del fifi: Nombre y contraseña
WifiPassword='Miau2323'

'''Conectar wifi y tomar hora'''

def redLed(T):
    pycom.heartbeat(False)
    pycom.rgbled(0xff0000)  # Red
    time.sleep(T)
def blueLed(T):
    pycom.heartbeat(False)
    pycom.rgbled(0x0000ff)  # Red
    time.sleep(T)
def greenLed(T):
    pycom.heartbeat(False)
    pycom.rgbled(0x00ff00)  # Red
    time.sleep(T)
def purpleLed(T):
    pycom.heartbeat(False)
    pycom.rgbled(0xFF33FF)  # Red
    time.sleep(T)


print("Entrando a sincronizar el tiempo...")

rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
while not rtc.synced():
    machine.idle()
print("RTC synced with NTP time")
#adjust your local timezone, by default, NTP time will be GMT
time.timezone(2*60**2) #we are located at GMT+2, thus 2*60*60
print('Hora del servidor:  ', rtc.now)
print('Hora local:         ', time.localtime())


'''FUNCIÓNES PARA LOS SENSORES'''

def getTemp2():                             #Obtiene la temperatura a partir del sensor de Presión (No ol)
    mote = MPL3115A2(py,mode=PRESSURE)      #llamar a la clase del sensor de presión en sus distintos modos: Altitud, Presion, Temp
    Tempetature2 = str(mote.temperature())
    return Tempetature2

def getPres():                              #Obtiene la Presion a partir del sensor de Presión
    mopre = MPL3115A2(py,mode=PRESSURE)     #llamar a la clase del sensor de presión en sus distintos modos: Altitud, Presion, Temp
    Presure = str(mopre.temperature())
    return Presure

def getAlti():
    moalt = MPL3115A2(py,mode=ALTITUDE)     #llamar a la clase del sensor de presión en sus distintos modos: Altitud, Presion, Temp
    Altitude = str(moalt.altitude())
    return Altitude

def getHum():
    si = SI7006A20(py)                      #Lllamar al sensor de humedad y temp (SI7006-A20) con 'si'
    HumRelativa = str(si.humidity())
    return HumRelativa

def getTemp():
    si = SI7006A20(py)                      #Lllamar al sensor de humedad y temp (SI7006-A20) con 'si'
    Temperature = str(si.temperature())
    return Temperature

    
def printWData():                             #llama a los sensores y muestra sus valores por pantalla.
    print('Datos tomados el: ',  str(utime.localtime()))
    print('Humedad igual a: ' , getHum())
    print('Temperatura igual a: ' , getTemp())
    print('Temperatura2 igual a: ' , getTemp2())
    print('Presion igual a: ' , getPres())
    print('altura igual a: ' , getAlti())

printWData()
pycom.heartbeat(True)