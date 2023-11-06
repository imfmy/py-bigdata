#! /bin/bash
# declare命令是Linux中的一个内建命令，用于声明变量的属性和类型。
# 定义变量的作用域：使用declare命令可以将变量定义为局部变量，即只在当前的shell脚本中有效。这样可以避免变量的命名冲突，提高脚本的可维护性。
# 设置变量的类型：使用declare命令可以设置变量的类型，包括整数型、字符串型、数组型等。这样可以限制变量的取值范围，提高程序的健壮性。
# 设置变量的属性：使用declare命令可以设置变量的属性，包括只读属性、可写属性、引用属性等。这样可以保护变量的值不被修改，提高程序的安全性。
# 为变量赋值：使用declare命令可以为变量赋初值。这样可以在声明变量的同时为其赋值，简化代码的编写。
# 原文链接：https://blog.csdn.net/qq_21438461/article/details/131432786

# 语法格式：declare [+-参数] [-p] [name[=value] ...]，声明变量时，变量名和等号之间不能有空格

# -a：将变量声明为数组类型。如果赋值时为非数组类型，则被认为包含一个元素的数组。
# -A：将变量声明为关联数组类型。
# -f：将变量声明为函数。
# -F：将变量声明为函数，但不会覆盖已存在的同名函数。
# -g：将变量声明为全局变量。
# -i：将变量声明为整数类型。如果复制非整数值，则该值将被设置为0。
# -l：将变量声明为小写字母类型。
# -n：将变量声明为引用类型。
# -r：将变量声明为只读类型。
# -t：将变量声明为跟踪类型。
# -u：将变量声明为大写字母类型。
# -x：将变量声明为环境变量。
# -p：显示已声明的变量列表。

# Example：
# 查看当前shell下定义的所有变量和函数
declare
# ……

# 查看变量属性
declare -p  PATH
# declare -x PATH="/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:……

# 转换普通变量为环境变量，效果同export
# 查找环境变量中是否有msg，declare -x 效果等同与 env
declare -x|grep "msg"
env|grep "msg"
# 没有查到msg
#声明环境变量msg
declare -x msg="Hello Linux"
# 再次查找环境变量中是否有msg
env|grep "msg"
# msg=Hello Linux
# 取消变量msg的属性
declare +x msg
# 取消后从环境变量中查找
declare -x|grep "msg"
# 没有找到



# 在同一行声明多个变量时，变量之间需要用空格分隔
declare var1='value1' var2='value2'
echo ${var1} $var2
# value1 value2

# 声明一个整数变量并为其赋初值
declare -i num=10
echo ${num}
# 10
declare -i result=$((5 + 3))
echo ${result}
# 8

# 声明一个只读变量
declare -r ro_var="it is read only"
echo "${ro_var}"
# it is read only
# 对只读变量做修改
ro_var="modify"
# -bash: ro_var: readonly variable
# 只读变量不仅无法修改其值，而且还不能用 +r 取消其只读的属性
declare +r ro_var
# -bash: declare: ro_var: readonly variable



# 声明一个数组变量,linux数组只能用空格隔开
declare -a arr=("apple" "pear" "orange")
echo "${arr[*]}"
# apple pear orange
echo "${arr[@]}"
# apple pear orange
declare -a arr1='([0]="张三" [1]="孙悟空" [2]="李四" [3]="唐僧")'
echo "${arr1[@]}"

# 声明一个小写字母类型变量,即使值为大写，也会转为小写
declare -l l_var="A1B2C3"
echo "${l_var}"
# a1b2c3

# 声明一个大写字母类型变量，即存在小写字母时会将小写字母转换为大写
declare -u u_var='a1b2c3'
echo "${u_var}"
# A1B2C3
