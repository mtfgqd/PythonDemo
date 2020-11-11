# 定义类是通过class关键字
class Student(object):

    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去，init类似于构造函数，
    # self类似于this，类中的方法第一个参数都是self
    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，类中不会定义成员变量，是dynamic的，
# 可以给类的实例随时加一个变量，即便是同一个类的两个实例变量，虽然它们都是同一个类的不同实例，
# 但他们拥有的变量名称和个数都可能不同
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()


# 在Class内部，可以有属性和方法，属性没有显示的声明，而外部代码可以通过直接调用实例变量的方法来操作数据
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，只有内部可以访问，外部不能访问
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），private prop <=> __prop

class Teacher(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


tom = Teacher('Tom', 100)
tom.set_name('To')
tom.get_name()
tom.print_score()
