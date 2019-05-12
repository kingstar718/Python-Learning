# encoding:UTF-8


#self指向的是类的实例
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


if __name__ == "__main__":
    t = Test()
    t.prt()
    """
    <__main__.Test object at 0x000001D58525B278>
    <classdemo '__main__.Test'>
    从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。
    self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
    """