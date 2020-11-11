class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


print(type(Hello))
h = Hello()
h.hello()
print(type(h))


# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def fn(self, name='world'):  # 先定义函数
    print('Hello1, %s.' % name)


def fn2(self, age=23):  # 先定义函数
    print('Hello1, %s.' % age)


Hello1 = type('Hello1', (object,), dict(hello=fn, age=fn2))  # 创建Hello class
print(type(Hello1))
h1 = Hello1()
h1.hello()
h1.age(43)
print(type(h1))


# 先定义metaclass，就可以创建类，最后创建实例。
# metaclass允许你创建类或者修改类.你可以把类看成是metaclass创建出来的“实例”。