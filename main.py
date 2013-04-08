# coding: utf8

import time

from lib.arduino import Arduino
from auth import *

PIN = 3

if __name__ == '__main__':
    arduino = Arduino('/dev/tty.usbmodem1421')
    arduino.output([PIN])
    apply_access_token()
    while 1:
        mentions = get_new_mentions()
        if mentions:
            for mention in mentions:
                print mention, mention['text']
                command = mention['text'].split()[1]
                if command == u'开门':
                    client.statuses.update.post(status=u'树莓开门！')
                    arduino.setHigh(PIN)
                elif command == u'关门':
                    client.statuses.update.post(status=u'树莓关门！')
                    arduino.setLow(PIN)
        else:
            print '亲，木有新命令。。。'
        time.sleep(5)
        