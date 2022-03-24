#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

from network import LoRa
import socket
import binascii
import struct
import ustruct
import time
import config

# LORA_FREQUENCY = 867500000          #these two lines substitute the #import config
# LORA_NODE_DR = 5


# initialize LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('260B9241'))[0]
nwk_swkey = binascii.unhexlify('265C8705FE124399397F9FF757A0FB4D')
app_swkey = binascii.unhexlify('897BF6ACA6D15E611BC4BF9D306FD492')

# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# set the 3 default channels to the same frequency
lora.add_channel(0, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

# make the socket non-blocking
s.setblocking(False)

for i in range (200):                                   #Envia el valor de value, pero no desenpaqueta bien. Solo me devuelve el primer valor de la tupla. Pero si que envia los datos por LOra
    value = 2.7+i                                       #
    pkt = struct.pack('f', value, 2.1+i )

    print('Sending:', pkt)
    Upkt= struct.unpack('f', pkt)
    print('Long tupla: ', len(Upkt))
    print('Unpacked Packet 0: ', Upkt[0] )
  #  print('Unpacked Packet 1: ', Upkt[1] )
    s.send(pkt)
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(2)