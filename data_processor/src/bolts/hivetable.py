from __future__ import absolute_import, print_function, unicode_literals
from streamparse.bolt import Bolt
import time
import os.path
dir = '/data/ProductMeasures/'

class HiveTable(Bolt):

    def initialize(self, conf, ctx):
        #get today's date
        self.out_name = str(time.strftime("%Y%m%d"))
        #try to see if it is already created
        #if yes, do nothing
        self.full_name = dir + self.out_name
        if os.path.isfile(self.full_name): #already opened before open with append
            self.out_file = open(self.full_name, 'a')
 
        else:
            #if no, create a file with today's date
            self.out_file = open(self.full_name, 'w')
        #save the file name as self.out_name

    def process(self, tup):
	m = tup.values[0] # extract the messages
        this_date = str(time.strftime("%Y%m%d"))
	# Emit to the 'log' file, which is the hive table
        # check if we are at a new date
        # if not, go on
        # if yes, close the file and open a new one, update outfilename
        if self.out_name != this_date:
            self.out_file.close()
            self.full_name = dir + this_date
            self.out_file = open(self.full_name, 'w') # new file
        rec  = ','.join([m['pid'],m['value'],m['unit'],m['date'],m['time']])+"\n"
	self.out_file.write(rec)
        self.emit([rec])
        self.log('%s' % rec)
