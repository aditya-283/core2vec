import json
import numpy as np
from scipy import stats

val_train = []
val_test = []


##node_vec = {}
##with open('NWDO.txt') as file:
##     header = 0
##     for line in file:
##             if header == 0:
##                     header=1
##                     continue
##             first = 1
##             index = 0
##             for digit in line.split():
##                     if first==1:
##                             first = 0
##                             index = int(digit)
##                             #print(index)
##                             continue
##                     if index in node_vec.keys():
##                             node_vec[index].append(float(digit))
##                             continue
##                     else:
##                            node_vec[index] = [float(digit)]

###converting dict to list of lists
##X = [[]]
###0-indexed
##first = 1
##for key in range(1,num_nodes):
##        if first == 1:
##                first=0
##                X[0] = arr[key]
##        else:
##                X.append(arr[key])

#print X
#print node_vec
dict = json.load(open("dicts/old_dict.txt"))
#print dict
allvec = json.load(open("old_core3.25.txt"))



#testing
#with open('tests/wordsim_sim.txt') as file:
with open('tests/mturk.txt') as file:
#with open('tests/combined.txt') as file:
#with open('tests/simlex.txt') as file:
    for line in file:
        arr = line.split(",")
        if arr[0].upper() in dict and arr[1].upper() in dict:
            computed = np.dot(allvec[str(dict[arr[0].upper()])], allvec[str(dict[arr[1].upper()])])
            val_test.append(float(arr[2]))
            val_train.append(computed)
            #print 'pair absent :' + arr[0].upper() + ' ' + arr[1].upper()
        
##print val_test
##print val_train


ans = stats.pearsonr(val_test, val_train)
print ans

##ans = stats.spearmanr(val_test, val_train)
##print ans


##test = np.array(val_test)
##temp = test.argsort()
##ranks_test = np.arange(len(test))[temp.argsort()]
##
##train = np.array(val_train)
##temp2 = train.argsort()
##ranks_train = np.arange(len(train))[temp2.argsort()]
##
##ans = stats.spearmanr(ranks_test, ranks_train)
##print ans
        

