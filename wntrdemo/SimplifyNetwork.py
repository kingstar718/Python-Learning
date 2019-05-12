import wntr
import networkx as nx
from networkXDemo import computeDegree
from demo5 import waterQuality, initwnModel
import pandas as pd
import numpy as np

def demo1():
    # Create a water network model
    inp_file = "ky8.inp"
    inp_file2 = "cs11021_2.inp"
    wn = initwnModel(inp_file2)
    # waterQuality(wn, "40")
    # wntr.graphics.plot_network(wn)

    # 管网简化
    skel_wn, remap = wntr.morph.skeletonize(wn, 400, return_map=True)
    wntr.graphics.plot_network(skel_wn)
    nodequ = waterQuality(skel_wn, "40")
    # print(remap)


def demo2():
    # Create a water network model
    inp_file = "ky8.inp"
    inp_file2 = "cs11021_2.inp"
    wn = initwnModel(inp_file)
    # 管网简化
    skel_wn, remap = wntr.morph.skeletonize(wn, 100, return_map=True)

    sim = wntr.sim.EpanetSimulator(wn)
    results_original = sim.run_sim()
    sim = wntr.sim.EpanetSimulator(skel_wn)
    results_skel = sim.run_sim()

    pressure_orig = results_original.node['pressure'].loc[:,skel_wn.junction_name_list]
    pressure_skel = results_skel.node['pressure'].loc[:,skel_wn.junction_name_list]
    pressure_diff = (abs(pressure_orig - pressure_skel)/abs(pressure_orig))*100

    pressure_diff = pressure_diff[:500]

    return pressure_orig, pressure_skel, pressure_diff

if __name__=="__main__":
    orig, skel, diff = demo2()
    #p = np.array([[1,2,3],[4,5,6],[7,8,9]])
    #p = pd.DataFrame(p, index=['a','b','c'], columns=['x', 'y','z'])
    #p.plot()