import wntr

# WNTR包含两个模拟器：WNTRSimulator和EpanetSimulator
inp_file = "Net2.inp"
wn = wntr.network.WaterNetworkModel(inp_file)
epanet_sim = wntr.sim.EpanetSimulator(wn)
epanet_sim_results = epanet_sim.run_sim()

#WNTRSimulator是一个纯Python水力模拟引擎，基于与EPANET相同的方程式。
# WNTRSimulator不包括运行水质模拟的方程式。
# WNTRSimulator包括模拟泄漏的选项，并在需求驱动或压力相关的需求模式下运行液压模拟。
#wntr_sim = wntr.sim.WNTRSimulator(wn)
#wntr_sim_results = wntr_sim.run_sim()

'''
print(epanet_sim_results.node.keys()) # node有什么属性
print(epanet_sim_results.link.keys())
print(epanet_sim_results.node['pressure'].loc[: 3*3600])    # 限定显示水力时间
print(epanet_sim_results.link['flowrate'].loc[: 3*3600])
'''


