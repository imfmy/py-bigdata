#! /bin/bash
for host in hadoop102 hadoop103 hadoop104
do
        echo ===='ssh' $host 'jps|grep -v Jps'====
        ssh $host jps $@ | grep -v Jps
done
