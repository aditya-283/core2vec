import json
import numpy as np
from scipy import stats
import networkx as nx


val_train = []
val_test = []


G = nx.read_edgelist('numEL.txt', nodetype=int, data=(('weight',float),), create_using=nx.DiGraph())
mat = nx.adjacency_matrix(G)

new = (I - 0.75*mat)
H=nx.DiGraph(new)


#print node_vec
dict = json.load(open("dict.txt"))
print dict

#testing
with open('mturk.txt') as file:
    for line in file:
        arr = line.split(',')
        if arr[0].upper() in dict and arr[1].upper() in dict:
            computed = np.dot(node_vec[dict[arr[0].upper()]], node_vec[dict[arr[1].upper()]])
            val_test.append(float(arr[2]))
            val_train.append(computed)
            #print 'pair absent :' + arr[0].upper() + ' ' + arr[1].upper()
        
    #print val_test
    #print val_train
        
ans = stats.pearsonr(val_test, val_train)
print ans

ans = stats.spearmanr(val_test, val_train)
print ans
        

