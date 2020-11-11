# 高级语言通常都内置了一套try...except...finally...的错误处理机制
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# 常见的错误类型和继承关系看这里：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()
# 调用foo()，foo() 调用bar()，结果bar()
# 出错了，这时，只要main()
# 捕获到了，就可以处理
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        logging.exception(e)  # 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
    finally:
        print('finally...')


class FooError(ValueError):
    pass


def foo2(s):
    n = int(s)
    if n == 0:
        # 如果要抛出错误，首先根据需要，可以定义一个错误的class，
        # 选择好继承关系，然后，用raise语句抛出一个错误的实例
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo2('0')


# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
# 尽量使用Python内置的错误类型。
def foo3(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar3():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
# 捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# 好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，
# 就一直往上抛，最终会抛给CEO去处理。

bar3()
