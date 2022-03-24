""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
# GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]
GATEWAY_ID = WIFI_MAC[:6] + "FFFF" + WIFI_MAC[6:12]
SERVER = 'eu1.cloud.thethings.network'
#for TTS v3, use 'eu1.cloud.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'MOVISTAR_6CD0'
WIFI_PASS = 'b4RbUL5GCsCArvQ6wohn'
'''
WIFI_SSID = 'OnePlus 6'
WIFI_PASS = 'Miau2323'
'''

# for IN865
# LORA_FREQUENCY = 865062500
# LORA_GW_DR = "SF7BW125" # DR_5
# LORA_NODE_DR = 5

# for EU868
LORA_FREQUENCY = 867500000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5

# for US915
# LORA_FREQUENCY = 903900000
# LORA_GW_DR = "SF7BW125" # DR_3
# LORA_NODE_DR = 3