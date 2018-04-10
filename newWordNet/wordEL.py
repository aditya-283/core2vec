#write idx idx edgelist
#write idx word dictionary

f = open('newwordEL.txt', 'w') # cue target FSG
with open('newcuetar.txt') as file:
    header = 0
    for line in file:
        if header == 0:
            header = 1
            continue
        line = line.replace(" ", ",")
        line = line.replace("\t", ",")
        #print line
        arr = line.split(",")
        #print arr
        if arr[2].isdigit():
            f.write(arr[0].upper() + ' ' + arr[1].upper() + ' ' + arr[4] + '\n')
f.close() 

