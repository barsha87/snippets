#return all partitions of a string

def partitions(string):
    l=len(string)
    i=0;
    while(i<l):
        str1 = string[0:i+1]
        str2 = string[i+1:]
        print (str1," ",str2)
        partitions(str1)
        #partitions(str2)
        i += 1
        
string = input()
partitions(string)


        


