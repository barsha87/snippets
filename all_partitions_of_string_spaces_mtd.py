#(none of the substrings shd be '')

string = input('Enter String ')
l = len(string)

# can handle upto length 5 string
def fun1():
    i=1
    a=[string]
    while (i<l):
        a.append(string[0:i] + ' ' + string[i:])
        j=i+1
        while (j<l):
            a.append(string[0:i] + ' ' + string[i:j] + ' ' + string[j:])
            k=j+1
            while (k<l):
                a.append(string[0:i] + ' ' + string[i:j] + ' ' + string[j:k] + ' ' + string[k:])
                m=k+1
                while (m<l):
                    a.append(string[0:i] + ' ' + string[i:j] + ' ' + string[j:k] + ' ' + string[k:m] + ' ' + string[m:])
                    m+=1
                k+=1
            j+=1
        i+=1
    print ('\n'.join(a))

fun1()

'''
l: length of string
i is just usual i.. my iterator :P
z is the number of loops= number of spaces required= l-1 at the start
'''

i=1
j=1
z=l-1
a=[string]

def fun2(a,l,i,z):
    str1=string[0:i]
    #a=[]
    while(i<l and z>0):
        str1= str1 + ' '+ string[i:] + ' '
        fun2(a,l,i+1,z-1)
        a.append(str1)
        i+=1
    return a
print('--------------------')
print ('\n'.join(fun2(a,l,i,z)))
