# coding: utf8

__version__ = '1.0'
__author__ = 'Lvyaojia  lvyaojia@gmail.com'

import time

from lib.arduino import Arduino
from auth import client, apply_access_token, get_new_mentions
from config import ARDUINO_ADDRESS, RELAY_PIN

if __name__ == '__main__':
    arduino = Arduino(ARDUINO_ADDRESS)
    arduino.output([RELAY_PIN])
    apply_access_token()
    while 1:
        mentions = get_new_mentions()
        if mentions:
            for mention in mentions:
                command = mention['text'].split()[1]
                if command == u'开灯':
                    client.statuses.update.post(status=u'开灯啦！')
                    arduino.setHigh(RELAY_PIN)
                    print '开灯'
                elif command == u'关灯':
                    client.statuses.update.post(status=u'关灯啦！')
                    arduino.setLow(RELAY_PIN)
                    print '关灯'
        else:
            print '亲，木有新命令。。。'
        time.sleep(5)

