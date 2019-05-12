# encoding:UTF-8
"""
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
            语法:
            classdemo   派生类(基类名):
                ...
在python中继承中的一些特点：
1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。
        详细说明可查看：python 子类继承父类构造函数说明。
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。
        区别在于类中调用普通函数时并不需要带上 self 参数
3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。
        （先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
            派生类的声明:
            classdemo SubClassName (ParentClass1[, ParentClass2, ...]):
                ...
"""

class Parent:
    parentAttr  = 100
    def __init__(self):
        print("调用父类的构造函数")
    def parentMethod(self):
        print("调用父类的方法")
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self,):
        print("父类属性: ", Parent.parentAttr)
    def myMethod(self):
        print("调用父类myMethod")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("调用子类的构造函数")
    def childMethod(self):
        print("调用子类的方法")
    def myMethod(self):
        print("改写父类myMethod")


if __name__ == "__main__":
    c = Child()     # 实例化子类
    c.childMethod()     # 调用子类的方法
    c.parentMethod()        # 调用父类方法
    c.setAttr(200)      # 再次调用父类的方法 - 设置属性值
    c.getAttr()     # 再次调用父类的方法 - 获取属性值

    # issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
    print(issubclass(Child, Parent))
    #isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
    print(isinstance(c, Child))
    print(isinstance(c, Parent))

    c.myMethod()    #  子类调用重写方法