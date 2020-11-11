import math


def my_func(funX, y):
    if funX > 0:
        print(y)
    else:
        print(-y)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    # b**2 == math.pow(b, 2)
    fac = math.pow(b, 2) - 4 * a * c
    r1 = -b + math.sqrt(fac)
    r2 = -b - math.sqrt(fac)
    bc = 2 * a
    return r1 / bc, r2 / bc


# 默认参数(位置参数)、可变参数、关键字参数/命名关键字参数必须传入参数名
# 如果有可变参数，默认参数就必须放到可变参数后面，被称为命名关键字参数
# tuple可作为可变参数不全默认参数和必选参数 、 dict可补全命名关键字参数

def enroll(name, gender, age=6, city='Beijing', *properties, **other):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    print(properties)
    print(other)


def enroll2(name, gender, age=6, *, city='Beijing', **other):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

    print(other)


def add_end(L=None):
    L.append('END')
    return L


# enroll('Sarah', 'F')
enroll("nn", "dd", *[28, "tianjin", 3], s="key")
# my_func(1, 20)
# my_func(1, 20)
# my_func(-1, 20)
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))
