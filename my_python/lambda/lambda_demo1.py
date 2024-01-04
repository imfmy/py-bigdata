"""
lambda关键字用于定义 Python 中的匿名函数。
lambda 函数可以不返回值；
lambda 函数可以有多个入参；
lambda 函数可以多个动态参数；
lambda 函数可以没有入参；
可以声明一个 lambda 函数，并以匿名函数的形式调用它，而无需将其赋给变量如：(lambda x: x*x)(5)
可以将 lambda 函数作为匿名函数传递给另一个函数
"""
square = lambda x: x * x
print(square(5))


def square2(x):
    return x * x


# lambda 表达式可以不返回值
greet = lambda name: print("hello", name)


def greet2(name):
    print("hello", name)


# lambda 表达式可以有多个入参；
multi_input = lambda x, y, z: x + y + z


def multi_input2(x, y, z):
    return x + y + z


# lambda 函数可以多个动态参数
var_input = lambda *x: print(type(x), x)


def var_input2(*x):
    print(type(x), x)


no_input = lambda: print("hello no_input")


def no_input2():
    print("hello no_input")


def do_something(lam_fun):
    print("开始执行匿名函数：")
    lam_fun()


def do_greet_name(lam_fn, name):
    print("开始执行匿名函数lam_fn：")
    lam_fn(name)


if __name__ == '__main__':
    print(square(3))
    # 9
    print(square2(3))
    # 9
    print(greet("zhangSan"))
    # hello zhangSan
    # None
    print(greet2("zhangSan"))
    # hello zhangSan
    # None
    print(multi_input(1, 2, 3))
    # 6
    print(multi_input2(1, 2, 3))
    # 6
    var_input(1, 2, 3, 4)
    # <class 'tuple'> (1, 2, 3, 4)
    var_input2(1, 2, 3, 4)
    # <class 'tuple'> (1, 2, 3, 4)
    no_input()
    # hello no_input
    no_input2()
    # hello no_input

    # 直接执行匿名函数
    (lambda: print("lambda表达式执行了"))()
    # lambda表达式执行了
    (lambda x, y: print(f'{x}+{y}={x + y}'))(1, 2)
    # 1+2=3

    do_something(no_input)
    # 开始执行匿名函数：
    # hello no_input

    do_greet_name(greet, "王五")
    # 开始执行匿名函数lam_fn：
    # hello 王五
