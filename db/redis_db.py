import redis

pool = redis.ConnectionPool(
    host="localhost",
    port="6379",
    password="123456",
    db=1
)