# encoding:utf-8
import wntr
import time
import os
import json
import multiprocessing

# 水质模拟的类
class waterQualitySim:
    def __init__(self, inp):
        self.wnModel = self.initwnModel(inp)     # 管网模型对象
        self.nodeList = self.wnModel.node_name_list     # 管网所有节点
        self.simpleNodeResult = self.computeTimeDirt(self.wnModel, self.nodeList, rptFile="F:/AWorkSpace/data/test/")
        self.parallelNodeResult = self.parallelComputeTimeDirt(self.wnModel, self.nodeList, rptFile="F:/AWorkSpace/data/test/")

    def initwnModel(self, inp, timeDuration=12 * 3600, reportTimeStep=600, reportStart=0):
        """
        初始化管网模型
        :param inp:  管网inp文件
        :param timeDuration:  水力时间
        :param reportTimeStep:  报告间隔
        :param reportStart:  报告初始时间
        :return:  wntr的管网对象
        """
        try:
            wnModel = wntr.network.WaterNetworkModel(inp)  # 加载管网inp文件
            for i in wnModel.node_name_list:
                wnModel.nodes._data[i]._initial_quality = 0  # 设置初始节点的水质都为0

            wnModel.options.quality.mode = 'CHEMICAL'  # 设置污染物为CHEMICAL
            wnModel.options.time.duration = timeDuration  # 设置水力时间
            wnModel.options.time.report_timestep = reportTimeStep  # 设置报告间隔
            wnModel.options.time.report_start = reportStart  # 设置报告初始时间
            return wnModel
        except:
            print("初始化管网模型发生异常")

    def waterQuality(self, wnModel, nodeName, startTime=0, endTime=12 * 3600, quality=10000,
                     rptFile="F:\AWorkSpace\datatemp\ Node_"):
        """
        特定节点污染物注入模拟
        :param wnModel:  wntr 水力模型对象
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
                                                                          start_time=startTime,
                                                                          end_time=endTime,
                                                                          duration=wnModel.options.time.duration,
                                                                          step_size=wnModel.options.time.pattern_timestep)
            wnModel.add_pattern('SourcePattern', source_pattern)  # 添加模式
            wnModel.add_source('Source1', nodeName, 'MASS', quality,
                               'SourcePattern')  # name, node_name, source_type, quality, pattern=None'     # 源注入的参数
            epanet_sim = wntr.sim.EpanetSimulator(wnModel)  # 加载wntr水力模型
            # rpt = "F:\AWorkSpace\datatemp\ Node_%s" % nodeName      # 设置输出文件位置
            rpt = rptFile + str(nodeName)  # 设置输出文件位置
            epanet_sim_results = epanet_sim.run_sim(file_prefix=rpt)  # 水质模拟
            wnModel.remove_source('Source1')  # 除去现有源模式
            wnModel.remove_pattern('SourcePattern')  # 除去现有模式
            # 三个输出文件位置
            # rptfile = "F:\AWorkSpace\datatemp\ Node_%s.rpt"% nodeName
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

    def computeTime(self, wnModel, epaDataFrame):
        """
        从水质模拟结果计算污染事件发生 所有其他节点第一次发现污染的时间
        :param wnModel:  wntr水力模型对象
        :param epaDataFrame:  某节点水质模拟结果
        :return:  {节点名:  初次发生污染时间}
        """
        ContaminationList = []
        # 将受到污染的节点拿出来
        for i in wnModel.node_name_list:
            if epaDataFrame.loc[43200, i] != 0:
                ContaminationList.append(i)
        ContaminationDirt = {}  # 键存节点名称 值存节点首次发生污染的时间
        for conNode in ContaminationList:
            count = 0
            for quality in epaDataFrame[conNode]:
                if quality == 0:
                    count = count + 1
                else:
                    ContaminationDirt[conNode] = count * 10
                    break
        return ContaminationDirt

    # 主函数  从加载
    def computeTimeDirt(self, wnModel, nodeNumList, rptFile="F:\AWorkSpace\data\ ", isJson = True):
        """
        计算管网所有事件的污染节点以及首次发生污染的时间
        :param wnModel:  wntr水力模型
        :param nodeNumList:  污染事件发生的节点集合
        :param rptFile:  保存的文件路径
        :return:  单个时间的csv文件, 所有事件的总的json文件
        """
        Qdirt = {}
        for nodeName in nodeNumList:
            try:
                nodeWaterQualityDataFrame = self.waterQuality(wnModel, nodeName)
                nodeDirt = self.computeTime(wnModel, nodeWaterQualityDataFrame)
                print(nodeDirt)
                Qdirt[nodeName] = nodeDirt  # 所有节点模拟的字典
            except:
                print("Node %s 发生异常" % nodeName)
        # 将总的节点污染数据作为一个json文件存储起来
        if isJson == True:
            jsonQDirt = json.dumps(Qdirt)
            jsonFileName = rptFile + "waterQuality.json"
            with open(jsonFileName, "w") as f:
                json.dump(jsonQDirt, f)
        return Qdirt


    def parallelComputeTimeDirt(self, wnModel, nodeNumList, rptFile="F:\AWorkSpace\data\ ", parallelNum = 3, isJson = True):
        """
        计算管网所有事件的污染节点以及首次发生污染的时间
        :param wnModel:  wntr水力模型
        :param nodeNumList:  污染事件发生的节点集合
        :param rptFile:  保存的文件路径
        :return:  单个时间的csv文件, 所有事件的总的json文件
        """
        # 切分nodeList
        nodeCount = len(nodeNumList)//parallelNum +10
        wnList = [nodeNumList[i:i + nodeCount] for i in range(0, len(nodeNumList), nodeCount)]
        pool = multiprocessing.Pool(processes=3)
        result = []
        for i in range(parallelNum):
            result.append(pool.apply_async(self.computeTimeDirt, (wnModel, wnList[i], rptFile, False)))
        pool.close()
        pool.join()

        sumDirt = {}
        for i in result:
            sumDirt.update(i.get())     # 从并行里拿出结果并进行字典整合
        if isJson == True:
            jsonQDirt = json.dumps(sumDirt)
            jsonFileName = rptFile + "waterQuality.json"
            with open(jsonFileName, "w") as f:
                json.dump(jsonQDirt, f)
        return sumDirt


if __name__ == "__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    inp3 = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"
    wnMode = waterQualitySim(inp2)
    wn = wnMode.wnModel
    wnlist = wnMode.nodeList
    nodeDirt = wnMode.parallelComputeTimeDirt
    print(wn.name)


    '''
    # 求度为3及以上的节点
    G = wn.get_graph()
    Degree = G.degree()
    k2 = []
    for k, v in Degree.items():
        if v > 2:
            k2.append(k)
    print(len(k2))
    print(k2)
   '''

'''
# 除去已模拟的节点
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
'''





