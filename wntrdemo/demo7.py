l = [[1,2,3,4,5,6,7,8,9,1],[1,2,3,4,5,6,7,8,9,1],[1,2,3,4,5,6,7,8,9,1]]
l2 = [1,2,3,4,5,6,7,8,9,1]
l3 = [1,2,3,4,5,6,7,8,9,1]
import  numpy as np


n = np.vstack((l2,l3))
from itertools import chain
n1 = set(list(chain(*l)))
ddd = {1:'2', 2:'22'}
print(len(ddd))
print(n1)

nodeName = 1
file = "F:\AWorkSpace\datatemp\ Node_"
inpfile = file + str(nodeName) +".inp"
print(inpfile)

l = [[1,2,3,4,5,6,7],[1,2,5,6,7,8,9,1],[1,2,3,4,5,6,7,8,9,1]]
l1 = np.array(l)
l2 = np.array(l)
l3 = np.vstack((l1, l2))
l4 = np.vstack((l,l))
print(l3)
print(l4)