#! /bin/bash
cat -n ${0}
for i in {1..5};do
  if [ $((i%2))  -eq 0 ];then
    echo "${i}为偶数，跳过"
    continue
  else
    echo "${i}"
  fi

done
##############
