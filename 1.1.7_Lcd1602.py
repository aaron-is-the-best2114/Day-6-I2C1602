#!/usr/bin/env python3
import LCD1602
import time

def setup():
    # LCD1602.init(0x27, 1)	# init(slave address, background light)
    # LCD1602.init(0x3f, 1)	# the i2c address for some LCD1602 is 0x3f
    LCD1602.init()	# auto check and select i2c address; background light default is 1

    LCD1602.write(0, 0, 'Greetings!')
    LCD1602.write(1, 1, 'From SunFounder')
    time.sleep(2)

def destroy():
    LCD1602.clear()

if __name__ == "__main__":
    try:
        setup()
    except KeyboardInterrupt:
        destroy()
