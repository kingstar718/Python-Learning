import wntr

# Create a water network model
inp_file = "ky8.inp"
wn = wntr.network.WaterNetworkModel(inp_file)

#print(wn.link_name_list)
'''
for i in wn.link_name_list:
    s = wn.links._data[i]._start_node         #  获取管线首尾节点
    e = wn.links._data[i]._end_node
    print(i, s,e)
'''
#print(wn.links._data['1']._end_node)
# 加载之后的函数

for i in wn.node_name_list:
    wn.nodes._data[i]._initial_quality = 0   # 设置初始节点的水质都为0
'''
for i in wn.node_name_list:
    print(wn.nodes._data[i]._initial_quality)
'''
# 除去源注入
for i in wn.source_name_list:
    wn.remove_source(i)

wn.options.time.report_timestep = 600
#wn._options.quality

'''
print(wn.junction_name_list)    #获得junciton的list
print(wn.node_name_list) # node
print(wn.link_name_list) # link  仅仅获取管网名称 不包含前后节点
'''

#j = simulation.network.elements.Junction('1',wn) # junction类
#print(j.initial_quality)

# Graph the network
#simulation.graphics.plot_network(wn, title=wn.name)

# Simulate hydraulics
wn.options.quality.mode = 'CHEMICAL'  #需要设置为化学物质
sim = wntr.sim.EpanetSimulator(wn)              # 设置初始水质为-, 模拟出来仍有水质存在
results = sim.run_sim()

# Plot results on the network
#pressure_at_5hr = results.node['pressure'].loc[5*3600, :]
#simulation.graphics.plot_network(wn, node_attribute=pressure_at_5hr, node_size=30, title='Pressure at 5 hours')

#print(results.node['quality'])
print(results.node['quality'].loc[ : 3*3600])


'''
G = wn.get_graph()
print(G.nodes())
print(G.node)
'''