===========Dependencies============
The following dependencies must be setup before running the code

1.) Kafka server is running
2.) A mongoDB instance is running and listening to localhost on port 27017 (mongoDB default)
3.) Python2.7 is the default python version
4.) pymongo is installed in Python library
5.) streamparse is installed
6.) Spark is installed, and the Spark library file is located in /home/w205/spark15/lib/spark-assembly-1.5.0-hadoop2.6.0.jar
    If the Spark library is in a different location, modify <cloned directory>/data_generator/compiled/run.sh to point to the right location
	
==========Running the code==========
This program uses Spark to generate data which is pushed into Kafka
A streamparse program consumes data from Kafka and persists data into MongoDB as well as produces a serving layer on Hive

* Start the data generator (Spark and Kafka):
  1.) Make sure that Kafka server is running and <cloned directory>/data_generator/compiled/run.sh points to the right location for the Spark library
  2.) Make sure that <cloned directory>/data_generator/compiled/run.sh is executable
  3.) Navigate to directory cloned directory>/data_generator/compiled/, and execute ./run.sh.  It is important the current directory is changed to 'compiled' as the script is looking for subdirectories using relative path.
  
* Start the data consumer (streamparse):
  <<streamparse instruction goes here>>
  
* Data visualization:
  <<data visualization instruction goes here>>
