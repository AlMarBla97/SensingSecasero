from network import WLAN
from network import LoRa
import binascii
import pycom
from network import LoRa
import ubinascii
from network import WLAN
import binascii

print()

lora = LoRa()
print("Device EUI (LoRa): %s" % (binascii.hexlify(lora.mac()).decode('ascii')))

wl = WLAN()
print("Device EUI (WLAN): {}",binascii.hexlify(wl.mac().sta_mac)[:6] + 'fffe' + binascii.hexlify(wl.mac().sta_mac)[6:])




pycom.heartbeat(False)
pycom.rgbled(0x009999)
pycom.heartbeat(True)

print('')
print('')

lora = LoRa()
print("Este es el DevEUI (Lora):   %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))

wl = WLAN()
print('Este es el EUI (Wlan):     ',binascii.hexlify(wl.mac().sta_mac)[:6] + 'ffff' + binascii.hexlify(wl.mac().sta_mac)[6:])

print('')
print('')
print('')
