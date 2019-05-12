import time
import pandas as pd
import numpy as np

s = [[1,2,3],[1,4,4],[5,7,8]]
s = pd.DataFrame(data=s, columns=['a','b','c'], index=[10,20,30])

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d':4, 'f':3}
dict3 = {'s':{'a': 1, 'b': 2, 'c': 3}, 'z':{'d':4, 'f':3}}
for i in dict3.values():
    if 'a' in list(i.keys()):
        print('true')


'''
# 切分list
l = [1,2,3,4,5,6,7,8,9,1]
c = [l[i:i+3] for i in range(0, len(l), 3)]
print(c, len(c))'''

'''

for i in range(10):
    try:
        i = 2/(-4+i)
        print(i)
    except:
        continue

th_list = [[[1,2,3],[1,2,3],[2,3,4]],[[1,2,3],[1,2,3],[2,3,4,4]],[[1,2,3],[2,3,4]]]
th_list = np.array(th_list)
print(th_list)'''

m = pd.DataFrame(index=['2','q','w'])
m['data'] = [1,2,3]
print(m)