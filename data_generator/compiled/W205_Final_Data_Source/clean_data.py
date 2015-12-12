import os

work_dir = 'C:\\Users\\kuanlin\\Desktop\\W205_Final_Data_Source\\Product4'

for i, f in enumerate(os.listdir(work_dir)):
	if not f.endswith('.log'): continue
	output_name = 'data_file_' + str(i) + '.txt'
	writer = open(os.path.join(work_dir, output_name), 'w')
	for line in open(os.path.join(work_dir, f)):
		if 'BCM' not in line and 'Measure' in line:
			writer.write(line)
	writer.close()
	