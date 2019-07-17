import wntr
import threading
import time
import pandas as pd
import os
import json


def initwnModel(inp, timeDuration = 12*3600, reportTimeStep = 600, reportStart = 0):
    """
    初始化管网模型
    :param inp:  管网inp文件
    :param timeDuration:  水力时间
    :param reportTimeStep:  报告间隔
    :param reportStart:  报告初始时间
    :return:  wntr的管网对象
    """
    try:
        wnModel = wntr.network.WaterNetworkModel(inp)   # 加载管网inp文件
        for i in wnModel.node_name_list:
            wnModel.nodes._data[i]._initial_quality = 0  # 设置初始节点的水质都为0

        wnModel.options.quality.mode = 'CHEMICAL'   # 设置污染物为CHEMICAL
        wnModel.options.time.duration = timeDuration       # 设置水力时间
        wnModel.options.time.report_timestep = reportTimeStep   # 设置报告间隔
        wnModel.options.time.report_start = reportStart     # 设置报告初始时间
        return wnModel
    except:
        print("初始化管网模型发生异常")


def waterQuality(wnModel, nodeName, startTime = 0, endTime = 12*3600, quality = 10000, rptFile = "F:\AWorkSpace\datatemp\ Node_"):
    """
    特定节点污染物注入模拟
    :param wnModel:  simulation 水力模型对象
    :param nodeName:   节点名称
    :param startTime:   污染开始时间
    :param endTime:     污染结束时间
    :param quality:  污染注入克数
    :param rptFile:  报告路径
    :return:  所有节点的间隔报告时间内的污染状况
    """
    try:
        start = time.time()
        # 设置源模式
        source_pattern = wntr.network.elements.Pattern.binary_pattern('SourcePattern',
                                                                      start_time = startTime,
                                                                      end_time = endTime,
                                                                      duration = wnModel.options.time.duration,
                                                                      step_size = wnModel.options.time.pattern_timestep)
        wnModel.add_pattern('SourcePattern', source_pattern)        # 添加模式
        wnModel.add_source('Source1', nodeName, 'MASS', quality,
                           'SourcePattern')  # name, node_name, source_type, quality, pattern=None'     # 源注入的参数
        epanet_sim = wntr.sim.EpanetSimulator(wnModel)      # 加载wntr水力模型
        #rpt = "F:\AWorkSpace\datatemp\ Node_%s" % nodeName      # 设置输出文件位置
        rpt = rptFile + str(nodeName)   # 设置输出文件位置
        epanet_sim_results = epanet_sim.run_sim(file_prefix=rpt)    # 水质模拟
        wnModel.remove_source('Source1')        #除去现有源模式
        wnModel.remove_pattern('SourcePattern')     # 除去现有模式
        # 三个输出文件位置
        #rptfile = "F:\AWorkSpace\datatemp\ Node_%s.rpt"% nodeName
        # binfile = "F:\AWorkSpace\datatemp\ Node_%s.bin"% nodeName
        # inpfile = "F:\AWorkSpace\datatemp\ Node_%s.inp"% nodeName
        rptfile = rpt + ".rpt"
        binfile = rpt + ".bin"
        inpfile = rpt + ".inp"
        if os.path.exists(rptfile) and os.path.exists(binfile) and os.path.exists(inpfile):
            # 计算完成, 删除目标文件
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
    """
    从水质模拟结果计算污染事件发生 所有其他节点第一次发现污染的时间
    :param wnModel:  wntr水力模型对象
    :param epaDataFrame:  某节点水质模拟结果
    :return:  {节点名:  初次发生污染时间}
    """
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
    return ContaminationDirt


def computeTimeDirt(wnModel, nodeNumList, rptFile = "F:\AWorkSpace\data\ " ):
    """
    计算管网所有事件的污染节点以及首次发生污染的时间
    :param wnModel:  wntr水力模型
    :param nodeNumList:  污染事件发生的节点集合
    :param rptFile:  保存的文件路径
    :return:  单个时间的csv文件, 所有事件的总的json文件
    """
    Qdirt={}
    for nodeName in nodeNumList:
        try:
            nodeWaterQualityDataFrame = waterQuality(wnModel, nodeName)
            nodeDirt = computeTime(wnModel, nodeWaterQualityDataFrame)
            print(nodeDirt)
            pPd = pd.DataFrame([nodeDirt])      # 将字典转换为DataFrame类型
            # print(nodeName)
            #Qdirt[nodeName] = qDirt
            csvFile = rptFile + str(nodeName) + ".csv"
            pPd.to_csv(csvFile, index=None, columns=None)
            Qdirt[nodeName] = nodeDirt  # 所有节点模拟的字典
        except:
            print("Node %s 发生异常" % nodeName)
    # 将总的节点污染数据作为一个json文件存储起来
    jsonQDirt = json.dumps(Qdirt)
    jsonFileName = rptFile + "waterQuality.json"
    with open(jsonFileName, "w") as f:
        json.dump(jsonQDirt, f)

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
