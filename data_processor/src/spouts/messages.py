# coding: UTF-8
from __future__ import absolute_import, print_function, unicode_literals
from kafka import SimpleConsumer
from kafka import KafkaClient
import codecs

import itertools
from streamparse.spout import Spout
group_id = "w205"
pid = ['pid1', 'pid2', 'pid3', 'pid4']

class Messages(Spout):

    def initialize(self, stormconf, context):
	kafka = KafkaClient('localhost:9092')
	self.messages1 = iter(SimpleConsumer(kafka, group_id, 'Product1'));
	self.messages2 = iter(SimpleConsumer(kafka, group_id, 'Product2'));
	self.messages3 = iter(SimpleConsumer(kafka, group_id, 'Product3'));
	self.messages4 = iter(SimpleConsumer(kafka, group_id, 'Product4'));

    def next_tuple(self):
	message1 = next(self.messages1).message.value.decode('utf-8')
	message2 = next(self.messages2).message.value.decode('utf-8')
	message3 = next(self.messages3).message.value.decode('utf-8')
	message4 = next(self.messages4).message.value.decode('utf-8')
        self.emit([pid[0]+','+message1])
        self.emit([pid[1]+','+message2])
        self.emit([pid[2]+','+message3])
        self.emit([pid[3]+','+message4])
