import pandas as pd,numpy as np
from sklearn import datasets
import random
import re
import matplotlib.pyplot as plt

class DataInit:

    def __init__(self,path):
        self.path = path
        self.df = pd.read_csv(self.path, low_memory=False)
       

    def readFile(self):
        self.df = pd.read_csv(self.path)

    def loadDataSet(self):
        dataSet = np.loadtxt(path)
        return dataSet

    # def head(self, n:int):
    #     return self.df.head(n)

    def head(self, n=5):
        return self.df.head(n)

    def shape(self):
        return self.df.shape

    def dropNaColumn():
        pass

    # 根据列获取非空记录的值
    # para: column:int
    def getNotNaValue(self,column):
        isNotNull = self.df.iloc[:,column].notnull()
        notNulldf = self.df[isNotNull]
        return notNulldf

    # 获取na的数量
    # def getNaNumber(self,start,end):
    #     for i in range(start,end)

    # n个cluster选择的K-means
    def nKMeans()
