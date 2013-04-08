# -*- coding: utf-8 -*-
#/usr/bin/env python

__version__ = '1.0'
__author__ = 'Lvyaojia  lvyaojia@gmail.com'

import shelve

import requests

from lib.weibo import APIClient
from lib.retry import *

APP_KEY = '330457405'
APP_SECRET = 'fdf309bef2ec167668b6cde8688f0952'
CALLBACK_URL = 'http://lvyaojia.sinaapp.com/' 
USERID = 'godtweet@sina.com'
USERPASSWD = 'godtweet'
TOKEN_FILE = './token.txt'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

def save_data(**kwargs):
    data = shelve.open(TOKEN_FILE)
    for key, value in kwargs.items():
        data[key] = value
    data.close()

def get_data(*args):
    data = shelve.open(TOKEN_FILE)
    result = []
    for arg in args:
        result.append(data.get(arg))
    return tuple(result)

def save_access_token(token):
    save_data(access_token=token['access_token'], expires_in=token['expires_in'])

def get_access_token_and_expires():
    return get_data('access_token', 'expires_in')

def save_since_id(since_id=None, mentions=None):
    '''保存最新的那条@我的微博的id'''
    if mentions:
        since_id = mentions[0]['id']
    save_data(since_id=since_id)

def get_since_id():
    '''
    第一次运行程序时，获取最新一条@我的微博，以后只监控比该微博时间要晚的@我的微博。
    若非第一次运行程序，则获取数据库保存的上一条查看过的mention的微博id。
    '''
    since_id = get_data('since_id')[0]
    if not since_id:
        mentions = client.statuses.mentions.get(count=1)['statuses']
        if len(mentions) == 0:
            since_id = 0
        else:
            since_id = mentions[0]['id']
        save_since_id(since_id)
    return since_id

def get_access_token_from_weibo():
    params = {'action':'submit', 'withOfficalFlag':0, 'ticket':'', 
        'isLoginSina':'', 'response_type':'code','state':'','from':''}
    params['redirect_uri'] = CALLBACK_URL
    params['client_id'] = APP_KEY
    params['userId'] = USERID
    params['passwd'] = USERPASSWD
    headers = {'Referer': client.get_authorize_url()}
    response = requests.post("https://api.weibo.com/oauth2/authorize", params=params, headers=headers)
    code = response.url.split('=')[1][0:-5]
    access_token = client.request_access_token(code)
    return access_token

@retry(1)
def apply_access_token():
    try:
        access_token, expires_in = get_access_token_and_expires()
        if not access_token:
            access_token = get_access_token_from_weibo()
            save_access_token(access_token)
            return False
        try:
            client.set_access_token(access_token, expires_in)
        except StandardError, e:
            if hasattr(e, 'error'): 
                if e.error == 'expired_token':
                    access_token = get_access_token_from_weibo()
                    save_access_token(access_token)
            else:
                pass
    except:
        access_token = get_access_token_from_weibo()
        save_access_token(access_token)
    return False
        
def get_new_mentions():
    '''只获取我关注的人的mention，并保存最新一条mention的id'''
    since_id = get_since_id()
    kwargs = {'filter_by_author':1, 'since_id':since_id}
    mentions = client.statuses.mentions.get(**kwargs)['statuses']
    if len(mentions) != 0:
        save_since_id(mentions=mentions)
    return mentions

if __name__ == '__main__':
    apply_access_token()
    client.statuses.update.post(status=u'测试一下。')
    mentions = get_new_mentions()
    if mentions:
        for mention in mentions:
            print mention['id'], mention['mid'], mention['text']
    else:
        print 'no new mentions yet'
    


