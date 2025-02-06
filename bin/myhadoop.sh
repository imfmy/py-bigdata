#! /bin/bash
if [ $# -lt 1 ]; then
  echo -e "\033[1;31mNo Args Input...\033[0m"
  exit
fi
HADOOP_HOME="/opt/module/hadoop-3.4.1"

case $1 in
"start")
  echo -e "\033[1;32m==== 启动 hadoop集群 =====\033[0m"
  echo -e "\033[1;32m---- hadoop102 上启动hdfs: sbin/start-dfs.sh----\033[0m"
  ssh hadoop102 "${HADOOP_HOME}/sbin/start-dfs.sh"
  echo -e "\033[1;32m---- hadoop103上启动yarn: start-yarn.sh----\033[0m"
  ssh hadoop103 "${HADOOP_HOME}/sbin/start-yarn.sh"
  echo -e "\033[1;32m---- hadoop102上启动historyserver:mapred --daemon start historyserver---\033[0m"
  ssh hadoop102 "${HADOOP_HOME}/bin/mapred --daemon start historyserver"
  ;;
"stop")
  echo -e "\033[1;32m===== 关闭 hadoop集群 =====\033[0m"

  echo -e "\033[1;32m---- 关闭 historyserver ---------------\033[0m"
  ssh hadoop102 "${HADOOP_HOME}/bin/mapred --daemon stop historyserver"
  echo -e "\033[1;32m---- 关闭 yarn ----\033[0m"
  ssh hadoop103 "${HADOOP_HOME}/sbin/stop-yarn.sh"
  echo -e "\033[1;32m---- 关闭 hdfs ----\033[0m"
  ssh hadoop102 "${HADOOP_HOME}/sbin/stop-dfs.sh"
  ;;
*)
  echo -e "\033[1;31mInput Args Error...\033[0m"
  ;;
esac
