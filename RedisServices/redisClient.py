import redis

r = redis.Redis(host='**', port=6379, db=15, password='**')

r.set('name', 'Jaycekon')

value = r.get('name')

print(value)
