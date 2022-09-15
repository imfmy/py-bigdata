#!/bin/bash

case $1 in
"start") {
  for i in hadoop102 hadoop103 hadoop104; do
    echo " ----启动Kafka:ssh $i kafka-server-start.sh ...'----"
    ssh $i "/opt/module/kafka/bin/kafka-server-start.sh -daemon /opt/module/kafka/config/server.properties "
  done
} ;;
"stop") {
  for i in hadoop102 hadoop103 hadoop104; do
    echo " ---停止Kafka:'ssh $i kafka-server-stop.sh'----"
    ssh $i "/opt/module/kafka/bin/kafka-server-stop.sh"
  done
} ;;
esac
