import sys

print('The command lines arguments are:')

for i in sys.argv:
    print(i)

print('\n\n the Python path is',sys.path)

#这里，当我们执行python using_sys.py we are arguments的时候，我们使用python命令运行using_sys.py模块，后面跟着的内容被作为参数传递给程序。
# Python为我们把它存储在sys.argv变量中。