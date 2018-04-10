import json

dict2 = {}
i = 1
f1 = open('NEWnumEL.txt', 'w') # cue target FSG
with open('newwordEL.txt') as file:
    for line in file:
        arr = line.split()
        if arr[0] not in dict2:
            dict2[arr[0]] = i
            i += 1
        if arr[1] not in dict2:
            dict2[arr[1]] = i
            i += 1
        f1.write(str(dict2[arr[0]]) + ' ' + str(dict2[arr[1]]) + ' ' + arr[2] + '\n')

f1.close()

##f2 = open("dict.txt","w")
##f2.write( str(dict) )
##f2.close()

json.dump(dict2, open("newdict.txt",'w'))
