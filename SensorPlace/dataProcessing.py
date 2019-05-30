# encoding:utf-8
import json
import wntr
from json import load, loads, dump, dumps


def readNodeJson(jsonPath):
    """
    读取所有节点的污染数据 并转为dirt
    :param jsonPath:  json文件路径
    :return:  dirt结构的数据
    """
    with open(jsonPath, "r") as f:
        nodeJson = load(f)
    nodeJson = loads(nodeJson)
    return nodeJson


def computeNode(nodeJson, nodeList):
    """
    将污染数据解析到所有点, 即所有节点都有能监测到的污染事件编号和时间
    :param nodeJson:  json文件路径
    :param nodeList:  管网所有节点列表  可能需要wntr的功能
    :return:  管网所有节点能监测到的事件编号及该事件的监测时间
    """
    nodeDirt = {}
    for node in nodeList:
        #node = str(node)
        nodedirt={}
        for i in nodeJson:
            if node in list(nodeJson[i].keys()):
                #nodelist.append(i)
                qualityNum = str(i)
                qualityTime = str(nodeJson[i][node])
                nodedirt[qualityNum] = qualityTime
        nodeDirt[node] = nodedirt
        print("节点%s 已完成" % node )
    nodeJson = dumps(nodeDirt)
    with open("F:\\AWorkSpace\\Python-Learning-Data\\AllNode.json", "w") as f:
        dump(nodeJson, f)
    return nodeDirt


def computeNode2(jsonpath):
    """
    先行计算所有节点能监测到的事件编号和平均监测时间
    :param jsonpath: json文件路径
    :return:  json文件  包含所有节点的能监测到的事件编号和平均监测时间
    """
    d = readNodeJson(jsonpath)
    ddirt = {}
    for i in d.keys():
        l = []
        ikeys = list(d[i].keys())
        sumTime = 0
        for j in d[i].keys():
            sumTime = sumTime + int(d[i][j])
        if len(ikeys) != 0:
            averageTime = sumTime / len(ikeys)
        else:
            averageTime = 720  # 将无法监测到任何事件的节点的监测时间设为水力模拟时间720分钟
            print("节点 %s 不能监测到任何事件" % i)
        l.append(ikeys)
        l.append(averageTime)
        ddirt[i] = l
        # print("节点 %s 已修改" % i)
    ddjson = dumps(ddirt)
    with open("F:\\AWorkSpace\\Python-Learning-Data\\DDirtnode.json", "w") as f:
        dump(ddjson, f)

def changeNumber(jsonpath):
    wModel = wntr.network.WaterNetworkModel("F:\\AWorkSpace\\Python-Learning-Data\\cs11021.inp")
    nodeDirt = {}
    for i, j in enumerate(wModel.node_name_list):
        nodeDirt[j] = i

    newDirt = {}
    d  = readNodeJson(jsonpath)
    for i, j in enumerate(d.keys()):
        newDirt[i] = d[j]       # 将字典的key中的管网编号改成0-66383
    for i in d.values():
        for j in range(len(i[0])):
            k = i[0][j]
            v = nodeDirt[k]
            i[0][j] = v     # 将values里第一个所有节点的编号改为0-66383
    newJson = dumps(newDirt)
    with open("F:\\AWorkSpace\\Python-Learning-Data\\DDirtnode3.json", "w") as f:
        dump(newJson, f)
    return newDirt


if __name__=="__main__":
    jsonpath = "F:\\AWorkSpace\\Python-Learning-Data\\AllNode.json"
    jsonpath2 = "F:\\AWorkSpace\\Python-Learning-Data\\node.json"
    jsonpath3 = "F:\\AWorkSpace\\Python-Learning-Data\\DDirtnode3.json"
    jsonpath4 = "F:\\AWorkSpace\\data\\3628node2.json"

    p = readNodeJson(jsonpath3)
    for i in p.keys():
        print(p[i][1])



    '''
    # 将污染数据解析到所有点, 即所有节点都有能监测到的污染事件编号和时间
    json = {"1":{"1":"a", "2":"b", "3":"c"}, "2":{"1":"a", "2":"b", "3":"c"}, "3":{"1":"a", "2":"b", "3":"c"}}
    print("2" in list(json["2"].keys()))
    jdirt = {"4":"c"}
    jsonpath = "F:\\AWorkSpace\\Python-Learning-Data\\node.json"
    nodeJson = readNodeJson(jsonpath)
    wModel = wntr.network.WaterNetworkModel("F:\\AWorkSpace\\Python-Learning-Data\\cs11021.inp")
    nodeList = wModel.node_name_list
    nodeDirt = computeNode(nodeJson, nodeList)
    '''
