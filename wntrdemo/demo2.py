import wntr
import networkx as nx

# networkX图

# Create a water network model
inp_file = "Net3.inp"
wn = wntr.network.WaterNetworkModel(inp_file)

G = wn.get_graph()
node_name = '123'
# 该图存储为嵌套字典。可以使用以下方法访问节点和链接（请注意，NetworkX 中的链接称为边缘）
print(G.node[node_name])
print(G.adj[node_name])

#该图可用于访问NetworkX方法，
node_degree = G.degree()
bet_cen = nx.betweenness_centrality(G)
wntr.graphics.plot_network(wn, node_attribute=bet_cen, node_size=30,
                           title="Betweenness Centrality")

# NetworkX方法可用于将有向图转换为无向图
uG = G.to_undirected()

#NetworkX方法可用于检查图表是否已连接
print(nx.is_connected(uG))

# 图表按长度加权。然后，此图可用于计算路径长度：
length  = wn.query_link_attribute('length')
G.weight_graph(link_attribute = length)
