# coding: utf-8
from wechat_sender import Sender

sender = Sender(token='test', receivers='409')

sender.send('hello world!')
