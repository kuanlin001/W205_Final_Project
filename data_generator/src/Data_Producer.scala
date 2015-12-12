import org.apache.kafka.clients.producer.KafkaProducer
import org.apache.kafka.clients.producer.ProducerConfig
import org.apache.kafka.clients.producer.ProducerRecord

import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.rdd.RDD
import org.apache.spark.broadcast.Broadcast

import java.util.Properties
import java.io.File
import scala.io.Source

object Data_Producer {
  def main(args: Array[String]) {
    println("Starting data-generation simulation")
    
    val sparkConf = new SparkConf().setAppName("DataProducer")
    .setMaster("local[4]")    // comment out when submitting to spark cluster
    val sc = new SparkContext(sparkConf)
    
    /*
    val local_data_sources = Array(
        "C:\\Users\\kuanlin\\workspace\\W205_Final_Project\\W205_Final_Project_Exe\\W205_Final_Data_Source\\Product1\\",
        "C:\\Users\\kuanlin\\workspace\\W205_Final_Project\\W205_Final_Project_Exe\\W205_Final_Data_Source\\Product2\\",
        "C:\\Users\\kuanlin\\workspace\\W205_Final_Project\\W205_Final_Project_Exe\\W205_Final_Data_Source\\Product3\\",
        "C:\\Users\\kuanlin\\workspace\\W205_Final_Project\\W205_Final_Project_Exe\\W205_Final_Data_Source\\Product4\\"
    )
    */
    
    val local_data_sources = Array(
        "W205_Final_Data_Source/Product1/",
        "W205_Final_Data_Source/Product2/",
        "W205_Final_Data_Source/Product3/",
        "W205_Final_Data_Source/Product4/"
    )
    
    sc.parallelize(local_data_sources).foreach(ds => {
      val producer = newStringKafkaProducer     
      
      //println("Start streaming data source: " + ds.split("\\\\").last)
      println("Start streaming data source: " + ds.split("/").last)
      (new File(ds)).listFiles.filter(f => { f.isFile && f.getName.toLowerCase.endsWith(".txt") }).foreach( f => {
        Source.fromFile(f, "ISO-8859-1").getLines.foreach(line => {
            println("Sending message: " + line)
            //sendMsg(producer=producer, topic=ds.split("\\\\").last, value=line)
            sendMsg(producer=producer, topic=ds.split("/").last, value=line)
            Thread.sleep(1000)
          })
      })
      
      producer.close()
    })
    
    println("Data-generation simulation ends")
  }
  
  def sendMsg(producer: KafkaProducer[String, String] = null, topic: String, value: String):  KafkaProducer[String, String] = {
    var prod: KafkaProducer[String, String] = null
    if(producer == null)
      prod = newStringKafkaProducer
    else
      prod = producer
    
    val rec = new ProducerRecord[String, String](topic, value)
    prod.send(rec)
    return prod
  }
  
  def newStringKafkaProducer: KafkaProducer[String, String] = {
    val props = new Properties()
    props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    props.put("bootstrap.servers", "localhost:9092")
    props.put("metadata.broker.list", "localhost:9092")
    val producer = new KafkaProducer[String,String](props)
    return producer
  }
}

