# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# Python提供了pickle模块来实现序列化。
import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()
# 直接把对象序列化后写入一个file - like Object：

f = open('dump.txt', 'wb')
pickle.dump(d, f)  # 序列化
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)  # 反序列化
f.close()

# JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，
# 并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
import json

d = dict(name='Bob', age=20, score=88)
json.dumps(d)
# dumps()方法返回一个str 内容就是标准的JSON dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object。
#
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))