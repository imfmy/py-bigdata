class Student:
    def __init__(self, name, age):
        self.name = name
        # 年龄不希望再类的外部使用,所以加了两个_
        self.__age = age
    def show(self):
        print(self.name,self.__age)

stu1 = Student('张三',13)
stu1.show()  # 张三 13
print(stu1.name)
