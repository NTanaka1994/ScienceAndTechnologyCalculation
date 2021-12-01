import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx 
from causalnex.structure.notears import from_pandas
from causalnex.structure import StructureModel

df=pd.read_csv("wine.csv")

SM=from_pandas(df)
SM.remove_edges_below_threshold(0.5)
plt.figure(figsize=(16,9))
pos = nx.spring_layout(SM, k=60)
 
edge_width = [ d['weight']*0.1 for (u,v,d) in SM.edges(data=True)]
nx.draw_networkx_labels(SM, pos)
nx.draw_networkx(SM,pos,node_size=4000,arrowsize=20,alpha=0.6,edge_color='b',width=edge_width)
plt.show()
