f = open('simlex.txt', 'w') # cue target FSG
with open('SimLex-999.txt') as file:
    header = 0
    for line in file:
        if header == 0:
            header = 1
            continue
        arr = line.split()
        #print arr
            f.write(arr[0].upper() + ' ' + arr[1].upper() + ' ' + arr[3] + '\n')
f.close() 

