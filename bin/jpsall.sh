#! /bin/bash
for host in hadoop102 hadoop103 hadoop104
do
        echo -e "\033[1;32m==== ssh $host jps|grep -v Jps====\033[0m"
        ssh $host jps "$@" | grep -v Jps
done
