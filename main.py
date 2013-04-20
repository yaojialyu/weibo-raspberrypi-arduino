# coding: utf8

__version__ = '1.0'
__author__ = 'Lvyaojia  lvyaojia@gmail.com'

import time

from lib.arduino import Arduino
from auth import client, apply_access_token, get_new_mentions
from config import ARDUINO_ADDRESS, RELAY_PIN, TEM_PIN

if __name__ == '__main__':
    arduino = Arduino(ARDUINO_ADDRESS)
    arduino.output([RELAY_PIN, TEM_PIN])
    # apply_access_token()
    # while 1:
    #     mentions = get_new_mentions()
    #     if mentions:
    #         for mention in mentions:
    #             command = mention['text'].split()[1]
    #             if command == u'开门':
    #                 client.statuses.update.post(status=u'树莓开门！')
    #                 arduino.setHigh(RELAY_PIN)
    #             elif command == u'关门':
    #                 client.statuses.update.post(status=u'树莓关门！')
    #                 arduino.setLow(RELAY_PIN)
    #     else:
    #         print '亲，木有新命令。。。'
    #     time.sleep(5)
    for i in range(10):
        tem = arduino.analogRead(TEM_PIN)
        print tem
        time.sleep(4)
        