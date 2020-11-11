# collections是Python内建的一个集合模块，提供了许多有用的集合类

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
from collections import deque, defaultdict, OrderedDict, namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
Circle = namedtuple('Circle', ['x', 'y', 'r'])  # namedtuple('名称', [属性list]):

# deque deque是为了高效实现插入和删除操作的双向列表,适合用于队列和栈：
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')  # q = deque(['y', 'a', 'b', 'c', 'x'])
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
key1 = dd['key1']  # key1存在
key2 = dd['key2']  # key2不存在，返回默认值

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])  # dict的Key是无序的
# OrderedDict的Key是有序的 OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

