from __future__ import absolute_import, print_function, unicode_literals

#from pymongo import MongoClient
#connection = MOngoClient("localhost", 27017)
from streamparse.bolt import Bolt
from pymongo import Connection
connection = Connection("localhost")
mdbName = 'Products'
 
db = connection[mdbName]
 
import re 
from streamparse.bolt import Bolt

class ParseMessage(Bolt):

    def initialize(self, conf, ctx):
        connection = Connection("localhost")
	self.db = connection.Products

    def process(self, tup):
        #an out_tuple is of 6 field <pid>,<tag>,<value>,<unit><date>,<time>
        out_tuples = []
	
	# Split the message into fields
	raw_fields = tup.values[0].split(',') # extract the messages by ','

        # common columns for all out_tuples
	col_pid = raw_fields[0]
        col_date = raw_fields[2].split(' ')[0]
        col_time = raw_fields[2].split(' ')[1]

        # <tag>,<value>,<unit> are one per tuple

        if len(raw_fields) == 10: #1 to 3 measures for 1 to 3 out tuples

            for field in raw_fields[7:]: #up to 3 of them
                #col_type = field.split(':')[0].strip()
                col_value = field.split(':')[1].split(' ')[1].strip()
                if col_value != 'N/A':
                    col_unit = field.split(':')[1].split(' ')[2].strip()
                    out_tuples.append({'pid':col_pid, 'value': col_value, 'unit':col_unit, 'date': col_date, 'time': col_time})

        elif len(raw_fields) == 9: #only one measure for 1 out tuple
                #col_type = (raw_fields[7].strip() + '_' + raw_fields[8].split(':')[0].strip()).replace('.','_')
                col_value_unit = raw_fields[8].split(':')[1].strip().split(' ')
                if len(col_value_unit) == 2:
                   col_value, col_unit = col_value_unit[0], col_value_unit[1]
                   out_tuples.append({'pid':col_pid, 'value': col_value, 'unit':col_unit, 'date': col_date, 'time': col_time}) 


	# Emit all out_tuples and save them to the mongodb
	for out_tuple in out_tuples:
	    self.db.Products.save({"measure":out_tuple});
            self.emit([out_tuple])
	    self.log('%s' % out_tuple) 
