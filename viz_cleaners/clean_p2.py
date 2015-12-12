#!/usr/local/bin/python

import os

def generateData():
	sourceFile = '/Users/ericperkins/Berkeley/w205/FinalProject/W205_Final_Data_Source/Product2/data_file_2.txt'
	for line in open(sourceFile, 'r'):
		yield line

def dataCleansing(raw_input):
	data_array = raw_input.split(',')
	data_date = 'N\A'
	data_time = 'N\A'
	data_voltage = 'N\A'
	data_current = 'N\A'
	data_power = 'N\A'
	if len(data_array) == 8:
		data_date = data_array[1].split(' ')[0]
		data_time = data_array[1].split(' ')[1]
		data_voltage = data_array[5].split()[1]
		data_current = data_array[6].split()[1]
		data_power = data_array[7].split()[1]
		return "Product2," + str(data_date) + "," + str(data_time) + "," + str(data_voltage) + "," + str(data_current) + "," + str(data_power)
	else:
		return None

#os.mknod('/Users/ericperkins/Berkeley/w205/FinalProject/write_files/write1.txt', 777)
writeFile = open('/Users/ericperkins/Berkeley/w205/FinalProject/write_files/write1.txt', 'a')
for line in generateData():
	measure_data = dataCleansing(line)
	if measure_data != None:
		writeFile.write(str(measure_data) + '\n')

writeFile.close()		
# print out the first 10 Power readings
