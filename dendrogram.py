import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn import preprocessing
import matplotlib.pyplot as plt
import csv
# methodのリスト
#method_list = ("average", "centroid", "complete", "median", "single", "ward", "weighted")

# dataを20個生成
df=pd.read_csv("wine.csv",encoding="shift-jis")
data=df.values
label=df["category"].values
# DataFrameオブジェクト生成
data=preprocessing.minmax_scale(data)
df=pd.DataFrame(data)

# クラスタリング
Z=linkage(df, method="average", metric="euclidean")
dendrogram(Z, labels=label)
plt.show()
