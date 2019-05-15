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