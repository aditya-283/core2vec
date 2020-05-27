from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import networkx as nx
from operator import mul
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
from scipy.spatial import distance


#with open('emb/lesm.emd.txt', 'r') as f:
#    first_line = f.readline()
#    metadata = first_line.split()
#    num_rows = int(metadata[0])
#    num_cols = int(metadata[1])
##    print(num_rows)
##    print(num_cols)

#array2d = [[0 for x in range(num_rows)] for x in range(num_cols)]


arr = {}
with open('emb/7grlesm15.txt') as file:
     header = 0
     for line in file:
             if header == 0:
                     header=1
                     continue
             first = 1
             index = 0
             for digit in line.split():
                     if first==1:
                             first = 0
                             index = int(digit)
                             #print(index)
                             continue
                     if index in arr.keys():
                             arr[index].append(float(digit))
                             continue
                     else:
                             arr[index] = [float(digit)]
X = [[]]
first = 1
for key in range(1,78):
        if first == 1:
                first=0
                X[0] = arr[key]
        else:
                X.append(arr[key])
#print "X is here :"
#print(X)


G = nx.read_edgelist('graph/lesm.txt', nodetype=int, data=(('weight',float),), create_using=nx.DiGraph())
G = G.to_undirected()
core_num = nx.core_number(G)

core_nodes = {}
for x in range(1,78):
    if core_num[x] in core_nodes:
        core_nodes[core_num[x]].append(x)
    else:
        core_nodes[core_num[x]] = []

#print core_nodes


pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

#print "X_r is here:"
#for i in range(0,30):
    #print i, X_r[i]

centroids = {}
for x in core_nodes:
    #print 'value of x is :' + str(x)
    sum1 = 0
    for i in core_nodes[x]:
            sum1 += X_r[i-1]

    centroid = sum1/len(core_nodes[x])
    centroids[x] = centroid

closeness=0
for i in core_nodes:
        cen_dist = 0
        for x in core_nodes[i]:
                cen_dist += distance.euclidean(X_r[x-1],centroids[i])
        cen_dist /= len(core_nodes[i])
        closeness += cen_dist
closeness /= 10
print closeness

avg_dist=0       
for i in core_nodes:
        for j in core_nodes:
                if j<=i:
                        continue
                min_dist = 999999
                for x in core_nodes[i]:
                        for y in core_nodes[j]:
                                #print X_r[x-1],X_r[y-1]
                                dist = distance.euclidean(X_r[x-1],X_r[y-1])
                                #print dist
                                min_dist = min(min_dist,dist)
                #print min_dist
                avg_dist += min_dist

#print avg_dist            
separation = avg_dist/45
print separation
                                



cols = map = ['olive', 'pink', 'green', 'blue', 'red', 'black', 'brown', 'orange', 'grey'] #lesm
map = [(1,'olive'), (2,'pink'), (3,'green'), (4,'blue'), (5,'red'), (6,'black'), (7,'brown'), (8,'orange'), (9,'grey')] #lesm



colours = []
for x in range(1,10):
            colours.append(cols[x-1])

#plt.scatter(X_r[:,0], X_r[:,1], c = colours)
#plt.scatter(centroids[:,0], centroids[:,1])
#plt.scatter(centroids[:,0], centroids[:,1], c = colours)

##fontP = FontProperties()
##fontP.set_size('x-small')
##
##
##handles = [mpatches.Patch(color=colour, label=label) for label, colour in map]
##plt.legend(handles=handles, loc='best', frameon=True, prop = fontP)

#plt.show()


