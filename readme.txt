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
9.) HiveServer2 service is running (hive --services hiveserver2 &).  We will use use Tabuleau to connect to Hive.
	
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
  5.) Make sure the Kafka Zookeeper and Server are up and running
  6.) Make sure the remote process connects to hive2 properly (server id at 'hive2.connection')
  7.) When 1-5 is ready, navigate to <cloned directory>/data_processor and execute 'sparse run'  
  
* Data visualization:
  
  Note: While this process is almost entirely the same for both HDFS connection and mongoDB, the expense of a mongoDB driver
  led us to only connect to Hiveserver2, so the following instructions are for connection to the Hive server

  1) Open Tableau, and connect to a server by clicking "Cloudera Hadoop"
  2) Enter server IP, select User Name, and enter root
  3) Select default, and select full table and drag to upper right hand corner
  4) Adjust measures to following types, if necessary:
      Date: Date
      Measure Type: String
      Pid (Product ID): String
      Time: Date & Time
      Measure Value: Numeric(Decimal)
  5) Drag Measure Value to Measures Pane, and change default aggregation from Sum to Avg
  6) All time-wise views:
      1) Optional: Drag Date to Columns section, and expand to "Day"
      2) Drag Time to Columns section, and expand to preferred granularity (likely "Hour" or "Minute")
  7) Product-focused view:
      1) Call the product(s) you want to investigate "P"
      2) Drag Pid to the rows field, and filter to only show P
      3) Drag the Measure Type field to the rows column, and filter to desired measure types
      4) Drag Measure Value to the rows column
      5) If desired, drag Measure Value to the rows column again and change Measure attribute to desired (e.g. Standard Deviation)
      6) Right click on Measure Value portion of the display, where the y-axis is, and select "Edit Axis". Change axis to "Independent axis ranges...", click Apply, and click OK
  8) Measure-Focused view:
      1) Call the measure(s) you want to investigate "M"
      2) Drag Measure Type to the rows field, and filter to only show M
      3) Drag the Pid field to the rows column, and filter to desired products
      4) Drag Measure Value to the rows column
      5) If desired, drag Measure Value to the rows column again and change Measure attribute to desired (e.g. Standard Deviation)
      6) Right click on Measure Value portion of the display, where the y-axis is, and select "Edit Axis". Change axis to "Independent axis ranges...", click Apply, and click OK
  9) Hollistic view:
      1) Drag Measure Type to rows field, and filter to desired measures
      2) Drag Measure Value to rows field, as many times as desired, selecting desired Measure attribute each time
      3) Drag Pid to the Color Pane under "All"
      4) Right click on Measure Value portion of the display, where the y-axis is, and select "Edit Axis". Change axis to "Independent axis ranges...", click Apply, and click OK

