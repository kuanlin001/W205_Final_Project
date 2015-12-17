===========Dependencies============
The following dependencies must be setup before running the code

1.) Kafka server is running
2.) A mongoDB instance is running and listening to localhost on port 27017 (mongoDB default)
3.) Python2.7 is the default python version
4.) pymongo2.7.2 is installed in Python library (sudo pip install pymongo==2.7.2)
    * pymongo verion is important.  Newer pymongo version may not be compatible with the API we use.
5.) streamparse is installed
6.) Spark is installed, and the Spark library file is located in /home/w205/spark15/lib/spark-assembly-1.5.0-hadoop2.6.0.jar
    If the Spark library is in a different location, modify <cloned directory>/data_generator/compiled/run.sh to point to the right location
7.) Hadoop/Hive is installed and running
8.) Python Kafka client is installed (pip install kafka-python)
	
==========Running the code==========
This program uses Spark to generate data which is pushed into Kafka
A streamparse program consumes data from Kafka and persists data into MongoDB as well as produces a serving layer on Hive

* Start the data generator (Spark and Kafka):
  1.) Make sure that Kafka server is running and <cloned directory>/data_generator/compiled/run.sh points to the right location for the Spark library
  2.) Make sure that <cloned directory>/data_generator/compiled/run.sh is executable
  3.) Navigate to directory <cloned directory>/data_generator/compiled/, and execute ./run.sh  It is important the current directory is changed to 'compiled' as the script is looking for subdirectories using relative path.
  
* Start the data consumer (Kafka, Sparse, MongoDB, and Hive):

  1.) Make sure the streamparse directory data_streaming is properly installed (copied)
  2.) Make sure MongoDB is up and running with the minimal initialization covered
  3.) Execute hive_ddl.sql in Hive to setup data schema definition.
  4.) Make sure, as in one of the W205 AMI convention, the directory /data exists
  5.) Create a directory /data/ProductMeasures/ if it does not already exist
  6.) Make sure the Kafka Zookeeper and Server are up and running
  7.) Make sure the remote process connects to hive2 properly (server id at 'hive2.connection')
  8.) When 1-5 is ready, navigate to <cloned directory>/data_processor and execute 'sparse run'  
  
* Data visualization:
  
  Note: While this process is almost entirely the same for both HDFS connection and mongoDB, the expense of a mongoDB driver
  led us to only connect to Hiveserver2, so the following instructions are for connection to the Hive server

  1) Open Tableau, and connect to a server by clicking "Cloudera Hadoop"
  2) Enter server IP, select User Name, and enter root
  3) Select default, and select full table and drag to upper right hand corner
  4) Click on 
