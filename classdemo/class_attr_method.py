# encoding:UTF-8

"""
类的私有属性:     __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
                        在类内部的方法中使用时 self.__private_attrs。
类的方法:       在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，
                     类方法必须包含参数 self,且为第一个参数
类的私有方法:     __private_method：两个下划线开头，声明该方法为私有方法，
                         不能在类的外部调用。在类的内部调用 self.__private_methods

单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
"""

class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

    def getSecretCount(self):
        return self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print counter.__secretCount  # 报错，实例不能访问私有变量

# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性，
'''
for i in dir(counter):
    print(i)
使用以上查找私有属性被改成什么样的名字,在调用,可直接访问私有属性
但不推荐
'''
print(counter._JustCounter__secretCount)

# 推荐写法, 使用get/set访问设置私有属性
print(counter.getSecretCount())