import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=15, password='***')
r = redis.StrictRedis(connection_pool=pool)
while True:
    inputs = input("publish:")
    r.publish('spub', 'hello')
    if inputs == 'over':
        print('停止发布')
        break
