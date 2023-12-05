#!/bin/bash

case $1 in
"start"){
    for i in hadoop102 hadoop103 hadoop104
    do
        echo " ----启动Kafka:ssh $i kafka-server-start.sh ...'----"
        ssh $i "${KAFKA_HOME}/bin/kafka-server-start.sh -daemon ${KAFKA_HOME}/config/server.properties"
    done
};;
"stop"){
    for i in hadoop102 hadoop103 hadoop104
    do
        echo " ---停止Kafka:'ssh $i kafka-server-stop.sh'----"
        ssh $i "${KAFKA_HOME}/bin/kafka-server-stop.sh"
    done
};;
esac

