# encoding:UTF-8
from Employee import Employee

emp = Employee("faker",1000)
emp.displayCount()
emp.displayEmployee()

# 添加，删除，修改类的属性
emp.age = 22        # 添加一个 'age' 属性
emp.age = 12        # 修改 'age' 属性
del emp.age     # 删除 'age' 属性

"""
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
"""
print(hasattr(emp, 'age'))      # 如果存在 'age' 属性返回 True。
setattr(emp, 'age', 22)     # 添加属性 'age' 值为 8
print(hasattr(emp, 'age'))      # 如果存在 'age' 属性返回 True。
print(getattr(emp, 'age'))    # 返回 'age' 属性的值
delattr(emp, 'age')     # 删除属性 'age'
print(hasattr(emp, 'age'))      # 如果存在 'age' 属性返回 True。