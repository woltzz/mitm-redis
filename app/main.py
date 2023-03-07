import json
import os
import uuid
import redis
import configparser
import logging

logging.basicConfig(level=logging.DEBUG)

cf = configparser.ConfigParser()
cf.read('config/config.ini')

redis_host = cf.get('redis', 'host')
redis_port = cf.get('redis', 'port')
client = redis.Redis(host=redis_host, port=redis_port, db=0)

filter_url_list = cf.items('filter')

key_prefix=cf.get('redis', 'key_prefix')


logging.info('\n\n')
logging.info("redis_url=[%s]\n", redis_host)
logging.info("redis_port=[%s]\n\n", redis_port)
for key, url in filter_url_list:
    logging.info("key=[%s] url=[%s]\n", key , url)
logging.info('\n\n')

def response(flow):
    if(flow.response.status_code != 200):
        return
    for key, url in filter_url_list:
        if url in flow.request.url:
            text = flow.response.text
            msg = dict(content=text)
            try:
                client.xadd(key_prefix + key, msg)
            except Exception as e:
                logging.error("Error:", e)
            continue
