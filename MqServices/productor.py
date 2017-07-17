import redis

pool = redis.ConnectionPool(host='10.201.3.18', port=6379, db=15, password='kntest%pw_@dk2')
r = redis.StrictRedis(connection_pool=pool)
while True:
    inputs = input("publish:")
    r.publish('spub', 'hello')
    if inputs == 'over':
        print('停止发布')
        break
