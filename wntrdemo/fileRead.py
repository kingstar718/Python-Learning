import os
import wntr


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
    print(NodeDirt)


def computeNode(filrpath):
    fileList = os.listdir(filrpath)
    nodeList=[]
    for i in range(len(fileList)):
        fileName = fileList[i]
        nodeList.append(fileName[:len(fileName)-4])
    print("nodeList ", nodeList)
    print("len nodeList", len(nodeList))
    return nodeList


if __name__=="__main__":
    filepath = 'F:\\AWorkSpace\\data\\data45\\'

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
    print(count, len(newlist))