@echo off
E:/Projects/apacheStuff/kafka/bin/windows/kafka-topics.bat --create --topic dataflow --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
pause
