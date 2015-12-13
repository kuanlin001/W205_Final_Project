from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
import time

kafka = KafkaClient('localhost:9092')
consumer = SimpleConsumer(kafka, 'f', 'product-1')
start = time.time()
count = 0
for msg in consumer:
    print "the msg: ", msg
    count += 1
    if count % 1000 == 0:
        dur = time.time() - start
        print 'Reading at {:.2f} messages/sec'.format(dur/1000)
        start = time.time()
