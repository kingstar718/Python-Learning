import redis

pool = redis.ConnectionPool(host='111.230.32.207', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')
print(r.get('gender'))