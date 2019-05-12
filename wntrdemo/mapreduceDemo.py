

def f(x):
    return x*x

m = map(f, [1,2,3,4,5,6,7,8])
print(list(m))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x, y):
    return x+y

r = reduce(add, [1,3,5,7,9])
print(r)