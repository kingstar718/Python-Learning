# encoding:utf-8
from json import load, loads, dump, dumps


class WaterQualitySimData():
    def __init__(self, json_path):
        self.json_path = json_path

    def read_node_json(self):
        """
        读取所有节点的污染数据 并转为dirt
        :return: node_dirt
        """
        with open(self.json_path, "r") as f:
            node_json = load(f)
        node_dirt = loads(node_json)
        return node_dirt

    def compute_node(self, new_json_name="new_json.json", is_out=False):
        """
        先行计算所有节点能监测到的事件编号和平均监测时间
        :param: json文件路径
        :return:  json文件  包含所有节点的能监测到的事件编号和平均监测时间
        """
        d = self.read_node_json()
        new_dirt = {}
        for i in d.keys():      # 所有节点编号
            l = []
            i_keys = list(d[i].keys())   # 当前节点的value中的下一级字典中的所有key键
            sum_time = 0
            for j in d[i].keys():
                sum_time = sum_time + int(d[i][j])
            if len(i_keys) != 0:
                average_time = sum_time / len(i_keys)
            else:
                average_time = 720  # 将无法监测到任何事件的节点的监测时间设为水力模拟时间720分钟
                # print("节点 %s 不能监测到任何事件" % i)
            l.append(i_keys)
            l.append(average_time)
            new_dirt[i] = l
            # print("节点 %s 已修改" % i)
        if is_out is True:
            new_json = dumps(new_dirt)
            with open(new_json_name, "w") as f:
                dump(new_json, f)
        return new_dirt

    def change_number(self, final_json="final_json.json", is_out=False):
        """
        将原字典里所有的使用节点编号的替换成index
        :return: final nodeDirt
        """
        change_dirt = {}    # 用于交换的字典, key为节点编号, value为索引
        node_dirt = self.compute_node()
        node_list = list(node_dirt.keys())
        for i, j in enumerate(node_list):
            change_dirt[j] = i

        new_dirt = {}
        d = node_dirt
        for i, j in enumerate(d.keys()):
            new_dirt[i] = d[j]  # 新建字典, key为index, value为原来的nodeDirt的value
        for i in d.values():
            for j in range(len(i[0])):
                k = i[0][j]
                v = change_dirt[k]
                i[0][j] = v  # 将新字典里的values里第一个所有节点的编号改为index
        # print(newDirt)
        if is_out is True:
            new_json = dumps(new_dirt)
            with open(final_json, "w") as f:
                dump(new_json, f)
        return new_dirt


if __name__ == "__main__":
    json_path = "F:\\AWorkSpace\\data\\test\\waterQuality.json"
    # 函数测试
    wnsd = WaterQualitySimData(json_path)
    nodeDirt = wnsd.read_node_json()
    nodeDirt2 = wnsd.compute_node()
    nodeDirt3 = wnsd.change_number()