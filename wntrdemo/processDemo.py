'''
   G = wn.get_graph()
   Degree = G.degree()
   k2 = []
   for k, v in Degree.items():
       if v > 2:
           k2.append(k)
   print(len(k2))
   print(k2)
   wnList = [k2[i:i+610] for i in range(0, len(k2), 610)]
   print(len(wnList[0]), len(wnList[1]), len(wnList[2]), len(wnList[3]), len(wnList[4]), len(wnList[5]))

   from concurrent.futures import ProcessPoolExecutor
   from fileRead import computeNode

   filepath = 'F:\\AWorkSpace\\data\\data\\'
   list1 = computeNode(filepath)
   newlist = wnList[0] + wnList[1] + wnList[2] + wnList[3]
   print("wnList: ", len(newlist))
   l = []
   count = 0
   for i in list1:
       for j in newlist:
           if j == i:
               newlist.remove(j)
               count += 1
   print(count, len(newlist))
   newlist = [newlist[i:i + 150] for i in range(0, len(newlist), 150)]
   print(newlist[0], newlist[1])
   print(len(newlist[0]), len(newlist[1]), len(newlist[2]))


   px = ProcessPoolExecutor(3)
   for i in range(3):
       px.submit(poolDemo, wn, newlist[i])
   px.shutdown(wait=True)'''

'''
wnList = [k2[i:i + 910] for i in range(0, len(k2), 910)]
print(wnList)

from concurrent.futures import ProcessPoolExecutor
px = ProcessPoolExecutor(4)
for i in range(4):
    px.submit(poolDemo, wn, wnList[i])
px.shutdown(wait=True)'''

''''
from concurrent.futures import ProcessPoolExecutor
px = ProcessPoolExecutor(4)
for i in range(4):
    px.submit(poolDemo1, "ky8.inp", wnList[i])
   #px.submit(demo3, wnList[i])
px.shutdown(wait=True)'''
'''
# 并行代码
p = Pool(4)
for i in range(4):
    p.apply_async(poolDemo, args=(wnL[i], wnList[i],))
print('Waiting for all subprocesses done...')
p.close()
p.join()
print('All subprocesses done.')'''

'''
pr0 = []
for i in range(4):
    p = Process(target=poolDemo, args=(wn, wnList[i]))
    pr0.append(p)
    p.start()
for p in pr0:
    p.join()'''
