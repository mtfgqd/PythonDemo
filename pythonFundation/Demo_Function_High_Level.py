from functools import reduce

# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
ls = [1, 2, -3, 4, 5, 6, -7, 8, 9]
mapValue = map(str, ls)
mapValue1 = map(abs, ls)
print(list(mapValue))
print(list(mapValue1))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把前两个参数计算结果继续和序列的下一个元素做累积计算
def add(x, y):
    return x + y


def combine(x, y):
    return str(x) + str(y)


def combine2(x, y):
    return x * 10 + y


ls = range(1, 5)
print(ls)
print(list(ls))
reValue = reduce(add, ls)
reValue1 = reduce(combine, ls)
reValue2 = reduce(combine2, ls)
print(reValue)
print(reValue1)
print(reValue2)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，
# 所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
def is_odd(n):
    return n % 2 == 1


filterValue = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
filterValue2 = list(filter(lambda x: x % 2 == 0, [1, 2, 4, 5, 6, 9, 10, 15]))
print(filterValue)
print(filterValue2)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。


# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum1


lazyFunc = lazy_sum(1, 3, 5, 7, 9)
print(lazyFunc)
print(lazyFunc())


def count():
    def f(i):
        def g():
            return i * i

        return g

    fs = []
    for j in range(1, 4):
        fs.append(f(j))
    return fs


print(count())
# 一个函数可以返回一个计算结果，也可以返回一个函数。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。


# 匿名函数lambda
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# decorator就是一个返回函数的高阶函数
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
# 直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。


# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。
int('12345', base=8)


def int2(x, base=2):
    return int(x, base)


# 下面的写法等价于上边的定义
int3 = functools.partial(int, base=2)
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
