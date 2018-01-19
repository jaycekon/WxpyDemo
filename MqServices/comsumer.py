import redis
from wechat_sender import *

sender = Sender(token='test', receivers='监控报警')

pool = redis.ConnectionPool(host='***', port=6379, db=4, password='***')
r = redis.StrictRedis(connection_pool=pool)
p = r.pubsub()
p.subscribe('monitor')
for item in p.listen():
    print(item)
    if item['type'] == 'message':
        data = item['data']
        print("消息队列中接收到信息：", data)
        sender.send(message=data)
        if item['data'] == 'over':
            break
p.unsubscribe('monitor')
print('取消订阅')
