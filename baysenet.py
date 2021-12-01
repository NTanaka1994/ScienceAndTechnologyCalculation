from pgmpy.models import BayesianModel
from pgmpy.estimators import BicScore
from pgmpy.estimators import ConstraintBasedEstimator
from pgmpy.inference import VariableElimination

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import networkx as nx

df=pd.read_csv("breast_cancer.csv")
#df=pd.read_csv("iris.csv")

df_cate=df
columns=list(df.columns)
for col in columns:
    df_cate[col]=pd.cut(df[col],2)
df_cate

est=ConstraintBasedEstimator(df_cate)

skel,separating_sets=est.estimate_skeleton(significance_level=0.01)
pdag=est.skeleton_to_pdag(skel,separating_sets)
model=est.pdag_to_dag(pdag)
DAG_model=BayesianModel(model.edges())

nx.draw_circular(DAG_model, with_labels=True, arrowsize=30, node_size=800,alpha=0.3, font_weight='bold')
plt.savefig("beysiannetwork2.png")
plt.show()

DAG_model.fit(df_cate)
cpds=DAG_model.get_cpds()
col=[]
for cpd in cpds:
    col.append(cpd.variable)
tmp=[]
val=[]

for cpd in cpds:
    if len(cpd.values.shape)==1:
        tmp.append(sum(cpd.values))
    else:
        tmp.append(cpd.values)
    val.append(tmp)
    tmp=[]
        #print(cpd.values)
"""
    for j in range(len(cpd.values)):
        if len(cpd.values.shape)==2:
            #print(cpd.values)
            tmp.append(sum(cpd.values[j]))
        elif len(cpd.values.shape)>=2:
            for k in range(len(cpd.values[j])):
                tmp.append(sum(cpd.values[j][k]))
"""
    
    
dfo=pd.DataFrame(val)
dfo=dfo.T
dfo.columns=col
dfo.to_csv("baysiannetwork3.csv",index=False)
