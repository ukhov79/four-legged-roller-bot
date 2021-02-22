from flask import Flask
import os
from sys import argv

import struct
import smbus
import sys
import time
from datetime import datetime

def readVoltage(bus):

        "This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
        address = 0x36
        read = bus.read_word_data(address, 0X02)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        voltage = swapped * 1.25 /1000/16
        return voltage


def readCapacity(bus):
        "This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object"
        address = 0x36
        read = bus.read_word_data(address, 0X04)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        capacity = swapped/256
        return capacity


def QuickStart(bus):
        address = 0x36
        bus.write_word_data(address, 0x06,0x4000)
      

def PowerOnReset(bus):
        address = 0x36
        bus.write_word_data(address, 0xfe,0x0054)

# Получение ip адреса для запуска
script, ip = argv
# Инициализация i2c 
# 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
bus = smbus.SMBus(0)
PowerOnReset(bus)
QuickStart(bus)

app = Flask(__name__)


@app.route('/')
def hello():
    then = datetime.now()
    txt = "Voltage:%5.2fV " % readVoltage(bus)
    txt+= "Battery:%5i%% " % readCapacity(bus)
    now = datetime.now()
    duration = now - then
    txt+= "Duration:%5imks" % duration.microseconds
    return txt

    
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host=ip, threaded=True, port=80)
