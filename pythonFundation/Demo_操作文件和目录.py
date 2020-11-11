# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作
# 系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os
import shutil

osname = os.name  # 操作系统类型 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数
os_version = os.environ  # 在操作系统中定义的环境变量
pathStr = os.environ.get('PATH')  # 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(pathStr)

# 操作文件和目录
os.path.abspath('.')  # 查看当前目录的绝对路径
os.path.join('demo_mat', 'testdir')  # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('demo_mat/testdir')  # 然后创建一个目录:
os.rmdir('demo_mat/testdir')  # 删掉一个目录:
os.path.split('demo_mat/testdir/file.txt')  # 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
os.path.splitext('demo_mat/file.txt')  # 可以直接让你得到文件扩展名
os.rename('test.txt', 'test.py')  # 对文件重命名
os.remove('test.py')  # 删掉文件:
# 复制文件的函数居然在os模块中不存在
# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

files = [x for x in os.listdir('.') if os.path.isdir(x)]