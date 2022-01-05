from network import WLAN
import time
import pycom
import machine

WifiName='OnePlus 6'                        #datos del fifi: Nombre y contraseña
WifiPassword='Miau2323'

def purpleLed(T):
    pycom.heartbeat(False)
    pycom.rgbled(0xFF33FF)  # Red
    time.sleep(T)
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

def connectWifi(name,Password):                 #Conecta el wifi dando red y contraseña como entrada. Modificar red al principio de este codigo.
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()
    print('Entrando en el método de conexion a wifi', 'n')
    for net in nets:

        ssid_= name
        password_= Password

        purpleLed(1)                            #Purple = Entered in this module
        i=0
        if net.ssid == ssid_:
            print('Network found!')    
            redLed(1)                           # red = network found
            wlan.connect(net.ssid, auth=(net.sec, password_), timeout=5000)
            while not wlan.isconnected():
                i=i+1
                print('intento de Conexión número: ', i)
                machine.idle() # save power while waiting
                time.sleep(1)
            print('WLAN connection succeeded!')
            greenLed(1)                         # Green = wlan conected

            break
    print('Saliendo del método de conexion a wifi', '\n')

connectWifi(WifiName,WifiPassword)
