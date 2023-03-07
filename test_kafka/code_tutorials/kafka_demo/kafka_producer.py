from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import sys
import random

fake=Faker()

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

p=Producer({'bootstrap.servers':'192.168.160.19:9092'})

#####################

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)
        
#####################
print('Kafka Producer has been initiated...')

def main():
    for i in range(200):
        data={
            'name':fake.name(),
            'email':fake.email(),
            'address':fake.address()
           }
        m=json.dumps(data)
        p.poll(1)
        p.produce('test-topic',m.encode('utf-8'),callback=receipt)
        p.flush()
        time.sleep(3)
        
if __name__ == '__main__':
    main()
