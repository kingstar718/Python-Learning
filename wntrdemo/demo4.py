import wntr
import time


# Create a water network model
start = time.time()
inp_file = "cs11021.inp"
wn = wntr.network.WaterNetworkModel(inp_file)
print("加载模型时间: ",time.time()-start)
wn.options.quality.mode = 'CHEMICAL'

#要跳过水质模拟，请按如下方式设置“质量”选项：
#wn.options.quality.mode = 'NONE'

# 水质模拟
wn.options.time.duration = 12*3600
wn.options.time.report_timestep = 600
wn.options.time.report_start = 0
source_pattern = wntr.network.elements.Pattern.binary_pattern('SourcePattern',
                                                              start_time=3*3600,
                                                              end_time=24*3600,
                                                              duration=wn.options.time.duration,
                                                              step_size=wn.options.time.pattern_timestep)
wn.add_pattern('SourcePattern', source_pattern)
wn.add_source('Source1', '41', 'SETPOINT', 100000, 'SourcePattern')  #name, node_name, source_type, quality, pattern=None

start = time.time()
epanet_sim = wntr.sim.EpanetSimulator(wn)
epanet_sim_results = epanet_sim.run_sim()
print("运行时间: ", time.time()- start)

#print(epanet_sim_results.node['quality'].loc[:12*3600])