# __str__   __iter__    __next__    __getitem__
class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))


class Student2(object):
    def __init__(self, name):
        self.name = name

    # 自定义类的字符串，类似重写toString()
    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student2('Michael'))


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个_iter__()方法，该方法返回一个迭代对象，然后，
# # Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个_值，直到遇到StopIteration错误时退出循环。
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，
# 不需要强制继承某个接口。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素,
    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
#
class Student5(object):

    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':  # 返回值
            return 99
        if attr == 'age':  # 返回函数
            return lambda: 25
        raise AttributeError('\'Student5\' object has no attribute \'%s\'' % attr)  # 其他参数报错

    # 定义一个__call__() 方法，就可以直接对实例进行调用
    def __call__(self):
        print('My name is %s.' % self.name)


s5 = Student5("Mi")
s5()  # 直接对实例进行调用
print(s5.name)
print(s5.score)  # 返回99 如果不加 __getattr__ 会报错
print(s5.age)  # __getattr__ 会报错

# 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
callable(Student())  # true
callable([1, 2, 3])  # false


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
