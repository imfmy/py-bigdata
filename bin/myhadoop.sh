#! /bin/bash
if [ $# -lt 1 ]; then
  echo "No Args Input..."
  exit
fi
case $1 in
"start")
  echo " ==== 启动 hadoop集群 ====="

  echo " ---- hadoop102上启动hdfs: sbin/start-dfs.sh----"
  ssh hadoop102 "/opt/module/hadoop-3.1.3/sbin/start-dfs.sh"
  echo " ---- hadoop103上启动yarn: start-yarn.sh----"
  ssh hadoop103 "/opt/module/hadoop-3.1.3/sbin/start-yarn.sh"
  echo " ---- hadoop102上启动historyserver:mapred --daemon start historyserver---"
  ssh hadoop102 "/opt/module/hadoop-3.1.3/bin/mapred --daemon start historyserver"
  ;;
"stop")
  echo " ===== 关闭 hadoop集群 ====="

  echo " ---- 关闭 historyserver ---------------"
  ssh hadoop102 "/opt/module/hadoop-3.1.3/bin/mapred --daemon stop historyserver"
  echo " ---- 关闭 yarn ----"
  ssh hadoop103 "/opt/module/hadoop-3.1.3/sbin/stop-yarn.sh"
  echo " ---- 关闭 hdfs ----"
  ssh hadoop102 "/opt/module/hadoop-3.1.3/sbin/stop-dfs.sh"
  ;;
*)
  echo "Input Args Error..."
  ;;
esac
