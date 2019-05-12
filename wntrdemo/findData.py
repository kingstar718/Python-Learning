import wntr
import numpy as np
import pandas as pd
import networkx

def computeWaterData(inp):
    wn = wntr.network.WaterNetworkModel(inp)
    sim = wntr.sim.EpanetSimulator(wn)
    result = sim.run_sim()
    demand = result.node['demand']
    head = result.node['head']
    pressure = result.node['pressure']
    return result

def diffCal(list):
    list = sorted(list)
    listLen = len(list)
    return abs(list[0]-list[listLen-1])


def waterdatamining(inp):
    wn = wntr.network.WaterNetworkModel(inp)
    wn.options.time.duration = 24 * 3600        # 设置水力时间为24小时
    sim = wntr.sim.EpanetSimulator(wn)
    result = sim.run_sim()

    waterData = pd.DataFrame()      # 收集数据的pandas类,
    waterData['nodeName'] = wn.node_name_list   # 第一列为节点名

    demand = result.node['demand']
    pressure = result.node['pressure']
    # 计算需水量  水压24小时差值
    demList = []
    preList = []
    for i in wn.node_name_list:
        print(i)
        dem_Diff = diffCal(demand[i])
        pre_Diff = diffCal(pressure[i])
        # print(i, dem_Diff,  pre_Diff)
        demList.append(dem_Diff)
        preList.append(pre_Diff)

    waterData['demDiff'] = demList  # 第二列为需水量极差
    waterData['perDiff'] = preList      # 第三列为压力极差

    AveDia = []
    diaDiff = []
    pipeLen = []
    for i in wn.node_name_list:
        print(i)
        pipeList = wn.get_links_for_node(i)     # 通过节点名找到其连接的管道
        dialist = []
        lenlist = []
        for j in pipeList:
            pipelist = wn.pipe_name_list
            if j in pipelist:  # 需要判断节点连接的是不是管道, 有可能是阀门, 没有长度
                dia = wn.links._data[j].diameter
                nodelen = wn.links._data[j].length
                dialist.append(dia)
                lenlist.append(nodelen)
        dialist = sorted(dialist)
        if len(dialist)<=1:
            diadiff = 0
        else:
            diadiff = dialist[len(dialist)-1]-dialist[0]
        if len(dialist)==0:
            avedia = 0
        else:
            avedia = sum(dialist) / (len(dialist))
        pipelen = sum(lenlist)
        AveDia.append(avedia)
        diaDiff.append(diadiff)
        pipeLen.append(pipelen)

    waterData['AveDia'] = AveDia
    waterData['diaDiff'] = diaDiff
    waterData['pipeLen'] = pipeLen

    pdfile = "F:\\AWorkSpace\\Python-Learning-Data\\datamining.csv"
    waterData.to_csv(pdfile)
    return waterData



#print(wn.links._data['20'].diameter)
#print(wn.links._data['10'].diameter)


if __name__=="__main__":
    inp = "F:\\AWorkSpace\\Python-Learning-Data\\cs11021.inp"
    #r = computeWaterData(inp)
    #w =waterdatamining(inp)
    pdfile = "F:\\AWorkSpace\\Python-Learning-Data\\datamining.csv"
    p = pd.read_csv(pdfile)
    #pd.set_option('display.float_format', lambda x: '%.8f' % x)
    # 保存时, 设置float_format 可取消科学计数法, 并设置小数位数
    p.to_csv("F:\\AWorkSpace\\Python-Learning-Data\\datamining2.csv", float_format='%.6f',  encoding='utf-8', index=False)

    pass