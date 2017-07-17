# coding: utf-8
from wechat_sender import Sender

sender = Sender(token='test')

sender.send('hello world!')
