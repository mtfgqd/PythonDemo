class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型
isinstance(b, Animal)
isinstance(c, Dog)


# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……（子类）时，我们只需要接收Animal(父类)类型就可以了
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())

import types


def fn():
    pass


# 我们来判断对象类型，使用type()函数
print(types.FunctionType == type(fn))
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
print(isinstance(b, Animal))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir(Animal))
print(Animal.__module__)

# 在len()函数内部，它自动去调用该对象的__len__()方法
len('abc')


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class Student(object):
    name = 'Student'


s = Student()  # 创建实例s
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)  # 打印类的name属性
s.name = 'Michael'  # 给实例绑定name属性
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
