from __future__ import absolute_import, print_function, unicode_literals
from streamparse.bolt import Bolt
import time
import os.path

dir = '/data/ProductMeasures/'

out_name = dir+str(time.strftime("%Y%m%d"))
if os.path.isfile(out_name): #already opened before open with append
    out_file = open(out_name, 'a')
else:
    out_file = open(out_name, 'w')

out_file.close()
