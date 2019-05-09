import DataInit,random,re
import matplotlib.pyplot as plt
import pandas as pd, numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn import preprocessing as prepro
from sklearn import metrics

path = r'C:\Users\Jaqen\Documents\DataSet\UserReport.csv'

df = pd.read_csv(path)
df.drop(['account','createDate','id','rebateAmount','actualSaleAmount','activityAndSend','test','juniorRebateAmount','tigerWinAmount','wages','platformSpend','platformDeduct'],axis=1,inplace=True)
df.head(3)
estimator = KMeans(n_clusters=4, init='k-means++', n_init=10, algorithm='elkan').fit(df)
result  = estimator.predict(df)
center = estimator.cluster_centers_
resultList = result.tolist()
indexrange = []
countlist=[]
indexNum =[i for i,v in enumerate(resultList) if v == 3]

for i in range(0,4):
    count = resultList.count(i)
    countlist.append(count)
    indexrange.append(i)

dfmessage =  pd.DataFrame({'编号':indexrange,
                '数量':countlist})


print(dfmessage, '\n\n总数：', len(resultList))

print(metrics.calinski_harabaz_score(df,result))

