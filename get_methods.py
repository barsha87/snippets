import re
f_write = open('file_new.txt', 'w')
l= []
d1 = {}
#count = 0
with open ('all_get.txt') as f:
    for line in f.readlines():
        first, sep, second = line.partition(':')
        new_sec= re.findall('\w*\.*get_\w+', second)
        new_sec = ','.join(new_sec)
        #f_write.write( first + ' : ' + ','.join(new_sec)+"\n")
        if first not in d1:
            d1[first]= []
            d1[first].append(new_sec)
        else:
            if new_sec not in d1[first]:
                d1[first].append(new_sec)  
        #l.append((first, ','.join(new_sec)))
        #count +=1

#l = map(lambda x: " : ". join(x), set(l))

for key in d1: 
    f_write.write(str(key) + ":" + ','.join(d1[key])+ '\n\n')
f_write.close()



