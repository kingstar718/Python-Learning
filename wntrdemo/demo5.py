import wntr
import threading
import time
import pandas as pd
import os

# 初始化管网模型
def initwnModel(inp):
    try:
        start = time.time()
        wnModel = wntr.network.WaterNetworkModel(inp)
        for i in wnModel.node_name_list:
            wnModel.nodes._data[i]._initial_quality = 0  # 设置初始节点的水质都为0
        wnModel.options.quality.mode = 'CHEMICAL'
        wnModel.options.time.duration = 12 * 3600
        wnModel.options.time.report_timestep = 600
        wnModel.options.time.report_start = 0
        #print("加载管网已完成,  用时 : ", time.time() - start)
        return wnModel
    except:
        print("初始化管网模型发生异常")


# 给特定的节点注入污染
def waterQuality(wnModel, nodeName):
    try:

        start = time.time()
        source_pattern = wntr.network.elements.Pattern.binary_pattern('SourcePattern',
                                                                      start_time=0,
                                                                      end_time=12 * 3600,
                                                                      duration=wnModel.options.time.duration,
                                                                      step_size=wnModel.options.time.pattern_timestep)
        wnModel.add_pattern('SourcePattern', source_pattern)
        wnModel.add_source('Source1', nodeName, 'MASS', 10000,
                           'SourcePattern')  # name, node_name, source_type, quality, pattern=None'
        epanet_sim = wntr.sim.EpanetSimulator(wnModel)
        rpt = "F:\AWorkSpace\datatemp\ Node_%s" % nodeName
        epanet_sim_results = epanet_sim.run_sim(file_prefix=rpt)
        wnModel.remove_source('Source1')
        wnModel.remove_pattern('SourcePattern')
        rptfile = "F:\AWorkSpace\datatemp\ Node_%s.rpt"% nodeName
        binfile = "F:\AWorkSpace\datatemp\ Node_%s.bin"% nodeName
        inpfile = "F:\AWorkSpace\datatemp\ Node_%s.inp"% nodeName
        if os.path.exists(rptfile) and os.path.exists(binfile) and os.path.exists(inpfile):
            os.remove(rptfile)
            os.remove(binfile)
            os.remove(inpfile)
        else:
            print("文件不存在")
        print("节点 %s 的污染模拟已完成" % nodeName, "模拟用时: ", time.time() - start)
        return epanet_sim_results.node['quality']
    except:
        print("水质模拟发生异常")

def computeTime(wnModel, epaDataFrame):
    start = time.time()
    ContaminationList= []
    # 将受到污染的节点拿出来
    for i in wnModel.node_name_list:
        if epaDataFrame.loc[43200, i] != 0:
            ContaminationList.append(i)
    ContaminationDirt = {}  # 键存节点名称 值存节点首次发生污染的时间
    for conNode in ContaminationList:
        count = 0
        for quality in epaDataFrame[conNode]:
            if quality == 0:
                count = count+1
            else:
                ContaminationDirt[conNode] = count*10
                break
    #print("单节点计算用时 : ", time.time() - start)
    return ContaminationDirt

def computeTimeDirt(wnModel):
    timeDirt = {}
    for node in wnModel.node_name_list:
        nodeQulityList = waterQuality(wnModel, node)
        nodeDirt = computeTime(wnModel, nodeQulityList)
        p = pd.DataFrame([nodeDirt])
        p.to_csv("F:\AWorkSpace\data\ %s.csv" % node, index=None, columns=None)
        #timeDirt[node] = nodeDirt
    #return timeDirt

def poolDemo(wnModel, nodeNumList):
    #Qdirt={}
    exList = []
    for nodeName in nodeNumList:
        try:
            qList = waterQuality(wnModel, nodeName)
            qDirt = computeTime(wnModel, qList)
            print(qDirt)
            pPd = pd.DataFrame([qDirt])
            # print(nodeName)
            #Qdirt[nodeName] = qDirt
            pPd.to_csv("F:\AWorkSpace\data\ %s.csv" % nodeName, index=None, columns=None)
        except:
            print("Node %s 发生异常" % nodeName)
            exList.append(nodeName)
            continue
    print(exList)
    '''
        for node in exList:
        try:
            # wnModel = copy.copy(wnModel1)
            qList = waterQuality(wnModel1, node)
            qDirt = computeTime(wnModel1, qList)
            pPd = pd.DataFrame([qDirt])
            # print(nodeName)
            # Qdirt[nodeName] = qDirt
            pPd.to_csv("F:\AWorkSpace\data\ %s.csv" % node, index=None, columns=None)
        except:
            print("Node %s 仍然失败" % node)
            continue'''


if __name__ == "__main__":
    inp1 = "Net3.inp"
    inp2 = "ky8.inp"
    inp3 = "cs11021.inp"
    wn = initwnModel(inp3)
    #timexin = waterQuality(wn, '91')
    #print(timexin)
    #timeDirt = computeTime(wn, timexin)
    #print(timeDirt)
    from multiprocessing import Process,Pool

    '''
    wnList = wn.node_name_list
    print(len(wnList))
    wnList = [wnList[i:i+350] for i in range(0, len(wnList), 350)]
    print(len(wnList[0]), len(wnList[1]), len(wnList[2]), len(wnList[3]))'''

    # 除去已模拟的节点
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
