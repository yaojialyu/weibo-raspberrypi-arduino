# -*- coding: utf-8 -*-
#/usr/bin/env python

#App 设置
APP_KEY = '330457405'
APP_SECRET = 'fdf309bef2ec167668b6cde8688f0952'
CALLBACK_URL = 'http://lvyaojia.sinaapp.com/' 

#授权用户的账号密码
USERID = 'godtweet@sina.com'
USERPASSWD = 'godtweet'

#用于保存token， since_id 的plain text database
TOKEN_FILE = './token.txt'

#Arduino 的地址, Linux下通常是：/dev/ttyACMx 或 /dev/ttyUSBx
ARDUINO_ADDRESS = '/dev/tty.usbmodem1421'