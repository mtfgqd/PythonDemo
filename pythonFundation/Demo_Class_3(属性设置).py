from types import MethodType


class Student(object):
    pass


def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


s = Student()
s.name = "Mi"
print(s.name)

# 给实例绑定一个方法 注意是个s这个实例绑定的方法
# 所以其他实例没有这个方法
s.set_age = MethodType(set_age, s)
s.set_age(25)  # 调用实例方法
print(s.age)  # 正常打印25
s2 = Student()  # 创建新的实例

# s2.set_age(25)  # 尝试调用方法 抛出异常
##############################################################################################


# 为了给所有实例都绑定方法，可以给class绑定方法
# 给class绑定方法后，所有实例均可调用
# 动态绑定允许我们在程序运行的过程中动态给class加上功能
Student.set_score = set_score
s.set_score(100)
s2.set_score(99)

print(s.score)
print(s2.score)


##############################################################################################
# 为了达到限制动态给class加功能的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Student2(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称,也就是说Student2最多允许有两个属性


ss = Student2()  # 创建新的实例
ss.name = 'Michael'  # 绑定属性'name'
ss.age = 25  # 绑定属性'age'


# ss.score = 99  # 尝试绑定属性'score',抛出异常

##############################################################################################
class Student3(object):
    # Python内置的@property装饰器负责把一个方法变成属性调用,相当于一个getter()
    @property
    def score(self):
        return self._score

    # 显示的加一个setter把一个方法变成属性设置
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    # score是个可读写属性 age是个只读属性
    @property
    def age(self):
        return 2015 - self._birth


s3 = Student3()
s3.score = 60  # OK，实际转化为s.set_score(60)
s3.score  # OK，实际转化为s.get_score()
print(s3.score)
