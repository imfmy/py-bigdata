# 来源：https://www.cnblogs.com/zhende/archive/2023/06/02/17451601.html

# 一次定义多个变量
declare  -a student=(1 2 3 4 5 6)
echo "${student[*]}"
# 1 2 3 4 5 6
echo "${student[@]}"
# 1 2 3 4 5 6

# 用索引定义数组
declare -a num=([0]=10 [2]=13 [3]=8 [2]=0 [1]=6)
echo "${num[*]}"
# 10 6 0 8

# 通过一组数据直接定义数组
declare  alp1="a c d e"
declare -a arr1=(${alp1})
echo "arr1:${arr1[*]},len:${#arr1[@]}"
# arr1:a c d e, len:4

# 遍历数组元素
# array[@]与array[*]的区别：
#    ${array[@]}：这会将数组的每个元素作为独立的参数传递。这意味着数组中的每个元素都被视为一个单独的参数，可以在命令中通过参数位置引用。
#    ${array[*]}：这将数组中的所有元素视为一个单独的字符串，并将它们作为单个参数传递。这意味着整个数组被视为一个字符串，并作为一个参数传递。
declare -a my_array=("a" "b" "c" "d")
for item in ${my_array[@]};do
  echo "${item}"
done
# apple
# banana
# cherry

for item1 in "${my_array[@]}";do
  echo "${item1}"
done
# apple
# banana
# cherry

for item2 in "${my_array[*]}";do
  echo "${item2}"
done
# apple banana cherry

for item3 in ${my_array[*]};do
  echo "${item3}"
done
# apple
# banana
# cherry

# 直接打印指定位置的数
# 不写下标时默认第一个元素
echo "${my_array}"
# apple
echo "${my_array[0]}"
# apple

# 打印数组所有元素
echo "${my_array[@]}"
# apple banana cherry
echo "${my_array[*]}"
# apple banana cherry

# 打印数组长度
echo "${#my_array[@]}"
# 3
echo "${#my_array[*]}"
# 3

# 打印最后一个元素
echo "${my_array[${#my_array[*]}-1]}"
# cherry

# 数组切片，${数组名[@或*]}:起始位置(起始索引):长度，取数组中的某一段的元素的值
declare  -a nums=(1 3 5 7 9 2 4 6)
echo ${nums[*]:0:2}
# 1 3
echo "${nums[@]:2:3}"
# 5 7 9

# 数组替换
declare  -a nums=( 2 4 6 8 10 1 3 5)
echo ${nums[*]}
# 2 4 6 8 10 1 3 5
echo "${nums[*]/2/55}"
# 55 4 6 8 10 1 3 5
echo "${nums[@]/2/55}"
# 55 4 6 8 10 1 3 5
# 永久替换
nums1=(${nums[@]/2/55})
echo "${nums1[*]}, ${#nums1[*]}"
nums1=("${nums[*]/2/55}")
echo "${nums1[*]}" " len:" ${#nums1[*]}

# 数组删除
declare  -a arr_del=(1 2 3 7 9 0)
echo "${arr_del[@]}"
# 1 2 3 7 9 0
# 删除指定位置数，后面数自动补上
unset 'arr_del[2]'
echo "${arr_del[@]}"
# 1 2 7 9 0
# 删除数组
unset arr_del
echo "${arr_del[@]}"
# 什么都没有


