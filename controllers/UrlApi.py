from bottle import route, run
from random import randint
import random
import redis

#  configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

# API: used to generate tiny URL that respresents the original url and add these data into the redis data base
@route('/urls/add-url/<originalUrl:path>')
def add_Url(originalUrl):
    generatedVal = str(generate_random_no())
    add_url_redis(tinyUrl=generatedVal, originalUrl=originalUrl)
    return generatedVal

# API: used to get the original URL from the tiny URL
@route('/urls/get-url/<tinyUrl>')
def get_original_url(tinyUrl):
    r = redis.StrictRedis(host=redis_host, port=redis_port,
                              password=redis_password, decode_responses=True)
    return r.get(tinyUrl)



def generate_random_no():
    random.seed(a=None)
    return randint(0, 1000000)  # randint is inclusive at both ends


def add_url_redis(tinyUrl, originalUrl):
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port,
                              password=redis_password, decode_responses=True)

        # step 4: Set the data in Redis
        r.set(tinyUrl, originalUrl)
        print (r.get(tinyUrl))

        # step 5: Retrieve the data message from Redis
    except Exception as e:
        print(e)


run(host='localhost', port=8080, debug=True)
