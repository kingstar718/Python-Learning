import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, threshold=np.nan)


def demo1():
    A = np.array([[3, -1], [-1, 3]])
    print('打印A：\n{}'.format(A))
    a, b = np.linalg.eig(A)
    print('打印特征值a：\n{}'.format(a))
    print('打印特征向量b：\n{}'.format(b))

    A = np.array([[-1, 1, 0], [-4, 3, 0], [1, 0, 2]])
    print('打印A：\n{}'.format(A))
    a, b = np.linalg.eig(A)
    print('打印特征值a：\n{}'.format(a))
    print('打印特征向量b：\n{}'.format(b))

    A = np.array([[0.1, 0.2, 0.4, 0.6], [0.2, 0.3, 0.4, 0.2]])
    H = np.dot(A.T, A)
    print("打印H: \n{}".format(H))
    a, b = np.linalg.eig(H)

    print("打印特征值a: \n{}".format(a))
    print("打印特征值b: \n{}".format(b))
    print(b.T)



class weightCalculation():
    def __init__(self, filePath):
        self.filePath = filePath

    # 评价指标Xj是以同等地位参与评价过程这个条件为前提的, 而事实上Xj之间的相对重要性程度是不同的
    def computeW(self):
        p = pd.read_csv(self.filePath)
        #p = p[["demDiff", "perDiff", "AveDia", "diaDiff", "pipeLen", "DiaLen", "Degree"]]
        p = p[["perDiff", "AveDia", "pipeLen", "DiaLen", "Degree"]]
        npl = p.values
        phalanx = np.dot(npl.T, npl)
        a, b = np.linalg.eig(phalanx)  # 计算矩阵的特征值, 特征向量
        b2 = b.T
        l = []
        # 得到最大特征值对应的特征向量并进行归一化
        for i in b2[0]:
            o = i / sum(b2[0])
            l.append(o)
        return l



if __name__=="__main__":
    filePath = "F:\\AWorkSpace\\Python-Learning-Data\\datamining2.csv"
    filePath2 = "F:\\AWorkSpace\\Python-Learning-Data\\datatest.csv"

    l = weightCalculation(filePath).computeW()
    print(l)
    #demo1()

    pass





