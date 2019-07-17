import networkx as nx

# 创建一个用例图：
G = nx.Graph()
dic1 = [(1,2,{'weight':1}), (2,4,{'weight':2}), (1,3,{'weight':3}), (3,4,{'weight':4}), (1,4,{'weight':5}), (5,6,{'weight':6})]
G.add_edges_from(dic1)
# nx.draw(G)
'''
shortest_path(G, source=None,target=None, weight=None)
forunweighted graphs
# weight (None or string, optional (default = None))– If None, every edge has weight/distance/cost 1.
# If a string, use this edge attribute as the edgeweight. Any edge attribute not present defaults to 1.
#当有多条最短路径时，只返回其中的一条
'''
# G = nx.path_graph(5)
# nx.draw(G)
print(nx.shortest_path(G, source=1, target=4))      # [1, 4]


G.clear()
G.add_weighted_edges_from([(0,1,1),(1,2,2),(0,2,0.5)])
print(nx.shortest_path(G, source=0, target=2))

G.add_weighted_edges_from([(0,1,1),(1,2,2),(0,2,15)])
print(nx.shortest_path(G,source=0,target=2,weight='123'))


# all_shortest_paths(G, source,target, weight=None)
# shortest_path_length(G, source=None,target=None, weight=None)
# average_shortest_path_length(G,weight=None)

# Simple Paths
'''
all_simple_paths(G, source, target[,cutoff])
shortest_simple_paths(G, source,target[, ...])
Generateall simple paths in the graph G from source to target, starting from shortestones.
从源到目标生成图G中的简单路径，从shortestones开始
'''
G = nx.cycle_graph(7)
paths = list(nx.shortest_simple_paths(G, 0, 3))
print(paths)
# has_path  判读是否有路径
print(nx.has_path(G, source=0, target=3))   # True

# single_source_shortest_path(G,source, cutoff=None)
# 从2开始，依次列出所有连接点{2: [2], 1: [2, 1], 3: [2, 3], 0: [2, 1, 0], 4: [2, 3, 4], 6: [2, 1, 0, 6], 5: [2, 3, 4, 5]}
print(nx.single_source_shortest_path(G,2))

# single_source_shortest_path_length(G,source)
# {1: 0, 0: 1, 2: 1, 6: 2, 3: 2, 5: 3, 4: 3}
print(nx.single_source_shortest_path_length(G,1))

#predecessor(G, source[, target,cutoff, ...])   前度
print(nx.predecessor(G, 2))

for i in nx.dfs_edges(G, 1):
    print(i)