# encoding:UTF-8
from Employee import Employee


"""
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""

print("Employee.__doc__:", Employee.__doc__)    #所有员工基类
print("Employee.__name__:", Employee.__name__)      #Employee
print("Employee.__module__:", Employee.__module__)      #Employee
print("Employee.__bases__:", Employee.__bases__)        #(<classdemo 'object'>,)
print("Employee.__dict__:", Employee.__dict__) 