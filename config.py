# -*- coding: utf-8 -*-
#/usr/bin/env python
#App 设置
APP_KEY = '4040337064'
APP_SECRET = 'd03b788d17b4763b0791ca79a18d1eeb'
CALLBACK_URL = 'http://lvyaojia.sinaapp.com'

#授权用户的账号密码
USERID = 'godtweet@sina.com'
USERPASSWD = 'a32046dd'

#用于保存token， since_id 的plain text database
TOKEN_FILE = './token.txt'

#Arduino 的地址, Linux下通常是：/dev/ttyACMx 或 /dev/ttyUSBx
#ARDUINO_ADDRESS = '/dev/tty.usbmodem1421'
ARDUINO_ADDRESS = '/dev/ttyACM0'

#继电器的PIN接口
RELAY_PIN = 3
