import redis

r = redis.Redis(host='10.201.3.18', port=6379, db=15, password='kntest%pw_@dk2')

r.set('name', 'Jaycekon')

value = r.get('name')

print(value)
