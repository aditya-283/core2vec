import json
dict_node = {}

with open('node2vec.txt') as file:
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
                     if index in dict_node.keys():
                             dict_node[index].append(float(digit))
                             continue
                     else:
                            dict_node[index] = [float(digit)]

json.dump(dict_node, open("old_core3.25.txt",'w'))

                           
