#!/usr/local/bin/python

from pymongo import MongoClient

def generateData():
	sourceFile = 'C:\\Users\\kuanlin\\workspace\\W205_Final_Project\\W205_Final_Project_Exe\\W205_Final_Data_Source\\Product1\\data_file_0.txt'
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

def persistToDb(client, db_name, measure_data):
	db = client[db_name]
	collection = db[measure_data['date'].replace('/','-')]
	inserted_id = collection.insert_one(measure_data).inserted_id
	return inserted_id
	
# open connection and persist to database
connection = MongoClient('localhost', 27017)
# data is append-only and immutable
for line in generateData():
	measure_data = dataCleansing(line)
	if measure_data != None:
		print dataCleansing(line)
		#print str(persistToDb(connection, 'Product1', dataCleansing(line)))
		
# print out the first 10 Power readings
#db = connection['Product1']
#collection = db['10-27-2015']
#rec_count = 0
#for rec in collection.find():
#	if 'Power' in rec:
#		print str(rec['time'] + ' | ' + str(rec['Power']))
#		rec_count += 1
#		if rec_count > 9: break
