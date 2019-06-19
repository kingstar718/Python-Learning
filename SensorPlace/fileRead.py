import os
import wntr
import json
import pandas as pd
import numpy as np

# 将污染节点的信息拿出来, 组成{node:}
def computeNodeDirt(filrpath):
    fileList = os.listdir(filrpath)
    NodeDirt = {}
    for i in range(len(fileList)):
        fileName = fileList[i]
        f = open(filepath+fileName, 'r')
        arr = []
        for lines in f.readlines():
            lines = lines.replace("\n", "").split(",")
            arr.append(lines)
        Dirt = {}
        for i in range(len(arr[0])):
            Dirt[arr[0][i]] = arr[1][i]
        # print(Dirt)
        NodeDirt[fileName[:len(fileName) - 4]] = Dirt
        f.close()
        print("已完成: " , i)
    '''
    jsonNode = json.dumps(NodeDirt)
    with open("F:\\AWorkSpace\\data\\node.json", "w") as f:
        json.dump(jsonNode, f)
        '''
    return NodeDirt


# 计算路径下的所有文件的节点列表
def computeNode(filrpath):
    fileList = os.listdir(filrpath)
    nodeList=[]
    for i in range(len(fileList)):
        fileName = fileList[i]
        nodeList.append(fileName[:len(fileName)-4])
    print("nodeList ", nodeList)
    print("len nodeList", len(nodeList))
    return nodeList

# 将矩阵转换为字典形式
class computeMatrix():
    def __init__(self, matrixpath):
        self.matrixpath = matrixpath
        self.matrix = pd.read_csv(self.matrixpath, header=None)
        self.timematrix = np.array(self.matrix)

    def computeNodeDirt(self):
        nodeDirt = {}
        for i in range(self.timematrix.shape[1]):
            #print(self.timematrix[:, i])
            nodeName = []
            nodeTime = []
            twoList = []
            for n,m in enumerate(self.timematrix[:, i]):
                # print(n,m)
                if m!=0:
                    nodeName.append(n)
                    nodeTime.append(m)
            #print("节点%d"%i , nodeName, nodeTime)
            if len(nodeTime)==0:
                timeSum = 0
            else:
                timeSum = sum(nodeTime) / len(nodeTime)
            twoList.append(nodeName)
            twoList.append(timeSum)
            nodeDirt[i] = twoList
            #print(i, twoList)
        print(nodeDirt)
        return nodeDirt


# 将节点管长/全管长作为概率  加入到json文件中
def nodeCP():
    matrixpath = 'F:\\AWorkSpace\\data\\max.csv'
    nodeDirt = computeMatrix(matrixpath).computeNodeDirt()
    importantNode = "F:\\AWorkSpace\\Python-Learning-Data\\datamining2.csv"
    p = pd.read_csv(importantNode)
    p = p[['nodeName', 'pipeLen']]
    p.index = p['nodeName']
    nodelist = computeNode('F:\\AWorkSpace\\data\\DataCsDegree3\\')
    lenSum = 0
    # 计算3628个点的管长总和
    for i in nodelist:
        lenSum = lenSum + p.loc[i, 'pipeLen']
    print(lenSum)
    psum = 0
    for i, j in enumerate(nodelist):
        #print(p.loc[i, 'pipeLen'])
        #print(nodeDirt[i], j, float(p.loc[j, 'pipeLen']))
        #print( j, float(p.loc[j, 'pipeLen']))
        nodeCp = (p.loc[j, 'pipeLen'])/lenSum
        nodeCp = '{:.8f}'.format(nodeCp)        # 如何对科学计数法保留小数位
        nodeDirt[i].append(nodeCp)
    #print(p['nodeName'][25])    # 取列值的node
    #print(p.loc[25, 'pipeLen'])         # 取索引号的管长
    nodeJson = json.dumps(nodeDirt)  # 转换为json
    with open("F:\\AWorkSpace\\data\\3628node.json", "w") as f:     # 保存为json文件
        json.dump(nodeJson, f)
    return nodeDirt


#新的计算方法 将平均管径*管长/所有节点的平均管径*管长作为新的概率
def nodeCp2():
    # 打开原有的json文件
    with open("F:\\AWorkSpace\\data\\3628node.json", "r") as f:
        data = json.load(f)
    nodeDirt  = json.loads(data)
    importantNode = "F:\\AWorkSpace\\Python-Learning-Data\\datamining2.csv"
    p = pd.read_csv(importantNode)
    p = p[['nodeName', 'DiaLen']]
    p.index = p['nodeName']
    diaLen = 0
    nodelist = computeNode('F:\\AWorkSpace\\data\\DataCsDegree3\\')
    for i in nodelist:
        diaLen = diaLen + p.loc[i, 'DiaLen']    # 计算所有节点的管径*管长之和
    print(diaLen)
    for i, j in enumerate(nodelist):
        nodeCp2 = (p.loc[j, 'DiaLen']) / diaLen
        nodeCp2 = '{:.8f}'.format(nodeCp2)  # 如何对科学计数法保留小数位
        nodeDirt[str(i)].append(nodeCp2)
    nodeJson = json.dumps(nodeDirt)  # 转换为json
    with open("F:\\AWorkSpace\\data\\3628node2.json", "w") as f:  # 保存为json文件
        json.dump(nodeJson, f)
    return nodeDirt


if __name__=="__main__":
    filepath = 'F:\\AWorkSpace\\data\\DataCsDegree3\\'

    # nodedirt = computeNodeDirt(filepath)
    #print(nodedirt["1434"])
    #p = nodeCP()
    #p = nodeCp2()



    #nodeList = computeNode(filepath)

    #with open("F:\\AWorkSpace\\data\\node.json", "r") as f:
        #data = json.load(f)
    #nodedirt = json.loads(data)
    #print(nodedirt["10012"])
    '''
    wn = wntr.network.WaterNetworkModel("cs11021.inp")
    G = wn.get_graph()
    Degree = G.degree()
    k2 = []
    for k, v in Degree.items():
        if v > 2:
            k2.append(k)
    print("len k2 ", len(k2))
    #print(k2)
    wnList = [k2[i:i + 610] for i in range(0, len(k2), 610)]
    print(len(wnList[0]), len(wnList[1]),  len(wnList[2]), len(wnList[3]), len(wnList[4]), len(wnList[5]))
    list1 = computeNode(filepath)
    newlist = wnList[4]+wnList[5]
    print("wnList: ", len(newlist))
    l = []
    count = 0
    for i in list1:
        for j in newlist:
            if j == i:
                newlist.remove(j)
                count +=1
    print(count, len(newlist))'''

    '''
        # 从全部节点中拿到那3628个节点的权值
    path = "F:\\AWorkSpace\\Python-Learning-Data\\json_node_weight.json"
    with open(path, "r") as f:
        data = json.load(f)
    #print(data)
    nodeList = computeNode(filepath)
    node_json = {}
    for i in nodeList:
        node_json[i] = data[i]
    print(node_json)
    path = "F:\\AWorkSpace\\Python-Learning-Data\\json_node3628_weight.json"
    with open(path, "w") as f:
        json.dump(node_json, f)
        '''