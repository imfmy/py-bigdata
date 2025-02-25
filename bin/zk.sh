#!/bin/bash
if [ $# -lt 1 ]; then
  echo "No Args Input..."
  exit
fi
case $1 in
"start")
  for i in hadoop102 hadoop103 hadoop104; do
    echo "====  $i :zkServer.sh start===="
    ssh $i "source /etc/profile && /opt/module/zookeeper-3.5.7/bin/zkServer.sh start"
  done
  ;;
"stop")
  for i in hadoop102 hadoop103 hadoop104; do
    echo "====  $i :zkServer.sh stop===="
    ssh $i "source /etc/profile && /opt/module/zookeeper-3.5.7/bin/zkServer.sh stop"
  done
  ;;
"status")
  for i in hadoop102 hadoop103 hadoop104; do
    echo "====  $i :zkServer.sh status ===="
    ssh $i "source /etc/profile && /opt/module/zookeeper-3.5.7/bin/zkServer.sh status"
  done
  ;;
*)
  echo "Input Args Error..."
  ;;
esac
