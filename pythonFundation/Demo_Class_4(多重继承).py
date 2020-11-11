# 动物基类
class Animal(object):
    pass


# 跑的动作
class Runnable(object):
    def run(self):
        print('Running...')


# 飞的动作
class Flyable(object):
    def fly(self):
        print('Flying...')


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass
