from __future__ import absolute_import, print_function, unicode_literals

dir = "/data/ProductMeasures"

class ParseMessage (Bolt):
    def initialize(self, conf, ctx):
        connection = Connection("localhost")
	self.outfile = open(dir,'w')

    def process(self, tup):
	measure = tup.values[0] # extract the messages
	# Emit to the 'log' file, which is the hive table
	self.outfile.write(measure)
        self.emit([measure])
        self.log('%s' % (measure)) 
