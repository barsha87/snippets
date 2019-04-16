import time

#Remove duplicates from an array (for 10000 elements 0.1 sec)

def func2():
    fin = open('input.txt', 'r')
    a= sorted([int(x) for x in fin.read().split()])
    t1= time.time()
    curr=a[0]
    b=[curr]
    for x in a:
        if curr!=x:
            curr =x
            b.append(curr)
    t2= time.time()
    fin.close()
    fout = open('output.txt', 'w')
    fout.write('   '.join(str(x) for x in b))
    fout.write('\nComputation time in secs: '+ str(t2-t1))
    fout.write('\nTotal elements at the start: '+ str(len(a)))
    fout.write('\nTotal elements after removing duplicates: '+ str(len(b)))
    t3= time.time()
    fout.write('\nTotal time in secs: '+ str(t3-t1))
    fout.close()

def func3():
    fin = open('input.txt', 'r')
    a= [int(x) for x in fin.read().split()]
    t1=time.time()
    i=0
    while i<len(a):
        x=a[i]
        if a.count(x)>1:
            a.remove(x)
            i-=1
        i+=1
    t2 =time.time()
    fin.close()
    fout = open('output1.txt', 'w')
    fout.write('   '.join(str(x) for x in a))
    fout.write('\nComputation time in secs: '+ str(t2-t1))
    fout.write('\nTotal elements after removing duplicates: '+ str(len(a)))
    t3= time.time()
    fout.write('\nTotal time in secs: '+ str(t3-t1))
    fout.close()
   
def func4():
    fin = open('input.txt' , 'r')
    a=[int(x) for x in fin.read().split()]
    fin.close()
    t1=time.time()
    fout = open('output2.txt', 'w')
    a=list(set(a))
    t2=time.time()
    fout.write('   '.join(str(x) for x in a))
    fout.write('\nComputation time in secs: '+ str(t2-t1))
    fout.write('\nTotal elements after removing duplicates: '+ str(len(a)))
    t3= time.time()
    fout.write('\nTotal time in secs: '+ str(t3-t1))
    fout.close()
   
func4()

