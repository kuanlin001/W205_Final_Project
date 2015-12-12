#!/usr/local/bin/python

def generateData():
	sourceFile = '/Users/ericperkins/Downloads/W205_Final_Data_Source/Product1/data_file_0.txt'
	for line in open(sourceFile, 'r'):
		yield line

def dataCleansing(raw_input):
	data_array = raw_input.split(',')
	data_date = data_array[1].split(' ')[0]
	data_time = data_array[1].split(' ')[1]
	measured_data = {'date': data_date, 'time': data_time}
	if len(data_array) == 9:
		for data in data_array[6:]:
			data_tag = data.split(':')[0].strip()
			data_val = data.split(':')[1].split(' ')[1].strip()
			if data_val != 'N/A':
				data_unit = data.split(':')[1].split(' ')[2].strip()
				measured_data[data_tag] = [data_val, data_unit]
	elif len(data_array) == 8:
		data_tag = (data_array[6].strip() + '_' + data_array[7].split(':')[0].strip()).replace('.','_')
		data_vals = data_array[7].split(':')[1].strip().split(' ')
		if len(data_vals) == 2:
			measured_data[data_tag] = [data_vals[0], data_vals[1]]
	if len(measured_data) > 2:
		return measured_data
	else:
		return None

writeFile = open('/Users/ericperkins/Downloads/W205_Final_Data_Source/Product1/write_0.txt', 'w')
for line in generateData():
	measure_data = dataCleansing(line)
	if measure_data != None:
		writeFile.write(str(measure_data) + '\n')

writeFile.close()		
# print out the first 10 Power readings
