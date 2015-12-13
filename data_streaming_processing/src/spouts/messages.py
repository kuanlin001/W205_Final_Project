# coding: UTF-8
from __future__ import absolute_import, print_function, unicode_literals
from kafka import SimpleConsumer
from kafka import KafkaClient
import codecs

import itertools
from streamparse.spout import Spout

class Messages(Spout):

    def initialize(self, stormconf, context):
	kafka = KafkaClient('localhost:9092')
	self.messages1 = iter(SimpleConsumer(kafka, 'e', 'Product1'));
	self.messages2 = iter(SimpleConsumer(kafka, 'e', 'Product2'));
	self.messages3 = iter(SimpleConsumer(kafka, 'e', 'Product3'));
	self.messages4 = iter(SimpleConsumer(kafka, 'e', 'Product4'));

    def next_tuple(self):
	message1 = u"Product1:"+next(self.messages1).message.value.decode('utf-8')
	message2 = u"Product2:"+next(self.messages2).message.value.decode('utf-8')
	message3 = u"Product3:"+next(self.messages3).message.value.decode('utf-8')
	message4 = u"Product4:"+next(self.messages4).message.value.decode('utf-8')
        self.emit([message1])
        self.emit([message2])
        self.emit([message3])
        self.emit([message4])
