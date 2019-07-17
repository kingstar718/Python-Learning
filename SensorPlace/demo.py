import wntr
inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
wn = wntr.network.WaterNetworkModel(inp1)       # 加载管网

pipe_list = wn.pipe_name_list       # 所有pipe
link_list = wn.link_name_list       # 所有link
p = wn.get_link("20")           # 根据特定管道名字拿出管道对象
print(p.diameter)       # 管道的管径
p.diameter = 3          # 设置新的管径        可循环设置
print(p.diameter)       # 查看新的管径
print(wn.get_link("20").diameter)       # 查看新的管径