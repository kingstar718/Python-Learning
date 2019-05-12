# encoding:UTF-8


"""
1.  empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。
        你可以在内部类或外部类使用 Employee.empCount 访问。
2.  第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，
        当创建了这个类的实例时就会调用该方法
3.  self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
"""
class Employee:
    '所有员工基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


if __name__ == "__main__":
    # 类的实例化类似函数调用方式。以下使用类的名称 Employee 来实例化，并通过 __init__ 方法接收参数。
    e = Employee("Faker","10000")  # 需要初始化值
    e.name = "Faker1"
    e.salary = "100020"
    e.displayEmployee()
    e.displayCount()
    print(Employee.empCount)