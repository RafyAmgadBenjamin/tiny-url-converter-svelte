from bottle import route, run
from random import randint
import random
import redis
import json
from bottle import hook, request, response
from bottle import post, get, put, delete
#  configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

####
_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'


@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers


@route('/', method='OPTIONS')
@route('/<path:path>', method='OPTIONS')

# API: used to generate tiny URL that respresents the original url and add these data into the redis data base
@get('/urls/add-url/<originalUrl:path>')
def add_Url(originalUrl):
    generatedVal = str(generate_random_no())
    add_url_redis(tinyUrl=generatedVal, originalUrl=originalUrl)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'tinyUrl': generatedVal})

# API: used to get the original URL from the tiny URL and redirect to the original URL
@route('/<tinyUrl>')
def get_original_url(tinyUrl):
    r = redis.StrictRedis(host=redis_host, port=redis_port,
                          password=redis_password, decode_responses=True)
    response.status = 303
    response.set_header('Location', r.get(tinyUrl))


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
        print(r.get(tinyUrl))

        # step 5: Retrieve the data message from Redis
    except Exception as e:
        print(e)


run(host='localhost', port=8080, debug=True)
