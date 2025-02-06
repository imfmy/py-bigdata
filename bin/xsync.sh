#! /bin/bash
#1. 判断参数个数：如果小于等于一个参数则提示然后退出
if [ $# -lt 1 ]; then
  echo "Not Enough Argument!"
  exit
fi
#2. 如果参数个数合规，则遍历集群所有机器
for host in hadoop102 hadoop103 hadoop104; do
  echo ==================== $host ====================
  #3. 遍历所有目录，挨个发送
  for file in "$@"; do
    #4. 判断文件是否存在
    if [ -e "$file" ]; then
      #5. 若文件存在则获取父目录绝对路径
      pdir=$(
        cd -P $(dirname $file) || exit
        pwd
      )
      #6. 获取当前文件的名称
      file_name=$(basename "$file")
      #7. 在目的主机创建同名父目录
      ssh $host "mkdir -p $pdir"
      #8. 将本目录文件同步至目的主机同目录中
      rsync -av $pdir/$file_name $host:$pdir
    else
      #9. 若本机文件不存在则提示文件不存在
      echo $file does not exists!
    fi
  done
done
