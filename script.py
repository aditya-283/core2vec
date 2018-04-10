from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import networkx as nx
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties



#array2d = [[0 for x in range(num_rows)] for x in range(num_cols)]
arr = {}
with open('core_sw.txt') as file:
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
                             print(index)
                             continue
                     if index in arr.keys():
                             arr[index].append(float(digit))
                             continue
                     else:
                             arr[index] = [float(digit)]
X = [[]]
first = 1
for key in range(1,84):
        if first == 1:
                first=0
                X[0] = arr[key]
        else:
                if key in arr:
                        X.append(arr[key])
#print "X is here :"
#print(X)

Y = np.array(X)
#print X
print(Y)

G = nx.read_edgelist('sw1.txt', nodetype=int)
###G = nx.read_edgelist('graph/lesm.txt', nodetype=int, data=(('weight',float),), create_using=nx.DiGraph())
##G = G.to_undirected()
core_num = nx.core_number(G)
##
print core_num

#kmeans = KMeans(n_clusters=6, random_state=0).fit(Y)
#for node in G.nodes():
#        print core_num[node],
#print(kmeans.labels_)
#print(kmeans.cluster_centers_)

#cnt = Counter()
#print(Counter(kmeans.labels_))


pca = PCA(n_components=2)
X_r = pca.fit_transform(X)
##print "X_r is here:"
##for i in range(0,83):
##    print i, X_r[i]
#plt.figure()
#for i in xrange(0,num_rows):
#    plt.scatter(X_r[i][0], X_r[i][1])
#plt.show()

#X_walk = []
#good_indices = [1,6,7,17]
#for i in good_indices:
#    X_walk.append(X_r[i])
#print X_walk
#
#cols = ['yellow', 'pink', 'green', 'blue']
#map = [(1,'yellow'), (2,'pink'), (3,'green'), (4,'blue')] #karate


cols = ['olive', 'pink', 'green', 'blue', 'red', 'black', 'brown', 'orange', 'grey','purple','cyan'] #lesm
map = [(1,'olive'), (2,'pink'), (3,'green'), (4,'blue'), (5,'red'), (6,'black'), (7,'brown'), (8,'orange'), (9,'grey'), (10, 'purple'),(11, 'cyan')] #lesm



colours = []
for x in range(1,84):
        if x in arr:
                colours.append(cols[core_num[x]])
#all having core_number 4
#plt.scatter(X_r[0][0], X_r[0][1])
#plt.scatter(X_r[5][0], X_r[5][1])
#plt.scatter(X_r[6][0], X_r[6][1])
#plt.scatter(X_r[16][0], X_r[16][1])
plt.scatter(X_r[:,0], X_r[:,1], c = colours)


fontP = FontProperties()
fontP.set_size('x-small')

for i in range(0,81):
    plt.annotate(i+1, (X_r[i][0],X_r[i][1]), FontProperties = fontP)




handles = [mpatches.Patch(color=colour, label=label) for label, colour in map]
plt.legend(handles=handles, loc='best', frameon=True, prop = fontP)


#all having core_number 3
#plt.scatter(X_r[23][0], X_r[23][1])
#plt.scatter(X_r[24][0], X_r[24][1])
#plt.scatter(X_r[25][0], X_r[25][1])
#plt.scatter(X_r[27][0], X_r[27][1])
#plt.scatter(X_r[28][0], X_r[28][1])
#plt.scatter(X_r[29][0], X_r[29][1])
#plt.scatter(X_r[30][0], X_r[30][1])
#plt.scatter(X_r[31][0], X_r[31][1])
#plt.scatter(X_r[32][0], X_r[32][1])
#plt.scatter(X_r[33][0], X_r[33][1])

plt.show()

