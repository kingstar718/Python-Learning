import wntr
import networkx as nx
import pandas as pd
import numpy as np
# networkX图

# Create a water network model
inp1 = "Net3.inp"
inp2 = "cs11021.inp"
#wn = wntr.network.WaterNetworkModel(inp1)

#G = wn.get_graph()
'''
node_name = '123'
# 该图存储为嵌套字典。可以使用以下方法访问节点和链接（请注意，NetworkX 中的链接称为边缘）
print(G.node[node_name])
print(G.adj[node_name])'''

#rint(G.order())  # 返回管网节点数
#print(len(G.terminal_nodes()))
#nxG = nx.DiGraph(G)


'''
k2 = []
for k,v in kvdegree.items():
    if v>2:
        k2.append(k)
print(len(k2))
print(k2)'''


def computeDegree(wnModel):
    G = wnModel.get_graph()
    kvdegree = G.degree()
    k3 = []
    for k in kvdegree.keys():
        if kvdegree[k] > 2:
            k3.append(k)
    #print(k3)
    return k3


#wn = wntr.network.WaterNetworkModel(inp1)
#print(wn.nodes._data['10']._coordinates)
# n
def computeInpCoor(inp):
    wn = wntr.network.WaterNetworkModel(inp)
    nodeInpDirt = {}
    for i in wn.node_name_list:
        #print(type(wn.nodes._data[i]._coordinates))
        nodeInpDirt[i] = wn.nodes._data[i]._coordinates
    return nodeInpDirt


# 拿出已有监测点的坐标数据
def computeCoor():
    wqmonitorfile = "D:\\Git\\Python-Learning\\wntrdemo\\wqmonitors.csv"
    pfile = pd.read_csv(wqmonitorfile, header=None)
    p = np.array(pfile)
    nodeDirt = {}
    for i in range(p.shape[0]):
        coorList = []
        coorList.append(p[i][3])
        coorList.append(p[i][4])
        nodeDirt[p[i][0]] = tuple(coorList)
    return nodeDirt




if __name__=="__main__":
    import math
    #nodeCoor = computeCoor()
    inp2 = "F:\AWorkSpace\Python-Learning-Data\cs11021.inp"
    #nodeInpCoor = computeInpCoor(inp2)