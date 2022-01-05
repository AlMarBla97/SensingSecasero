import pycom
from network import LoRa
import ubinascii
from network import WLAN
import binascii


pycom.heartbeat(False)
pycom.rgbled(0x009999)
pycom.heartbeat(True)

print('')
print('')

lora = LoRa()
print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))

print('')
print('')


wl = WLAN()
binascii.hexlify(wl.mac().sta_mac)[:6] + 'fffe' + binascii.hexlify(wl.mac().sta_mac)[6:]

print('')
print('')
print('')
