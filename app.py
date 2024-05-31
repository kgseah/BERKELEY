import os
from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
DECODE_RESPONSES = os.environ.get('DECODE_RESPONSES', 'True').lower() \
                   in ['true', '1']

# Connect to Redis
redis_client = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=DECODE_RESPONSES
)


@app.route('/')
def index():
    # Increment the counter
    count = redis_client.incr('visitor_count')
    return f'This is the {count} visitor.'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
