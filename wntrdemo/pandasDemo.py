import pandas as pd

p = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], columns=['a', 'b', 'c', 'd'])
print(p)

p1 = p['a']
print(p1.sum())  # 求一列的和
print(p1.mean())    # 求一列均值
# print(p.sum())
for i in p:
    # print(p[i])
    p[i] = p[i]/p[i].sum()
