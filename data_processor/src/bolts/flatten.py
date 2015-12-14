from __future__ import absolute_import, print_function, unicode_literals

dir = "/data/ProductMeasures"

class ParseMessage (Bolt):
    def initialize(self, conf, ctx):
        connection = Connection("localhost")
        #get today's date
        #try to see if it is already created
        #if yes, do nothing
        #if no, create a file with today's date
        #save the file name as outfilename
	self.outfile = open(dir,'w')

    def process(self, tup):
	measure = tup.values[0] # extract the messages
	# Emit to the 'log' file, which is the hive table
        # check if we are at a new date
        # if not, go on
        # if yes, close the file and open a new one, update outfilename
	self.outfile.write(measure)
        self.emit([measure])
        self.log('%s' % (measure)) 
