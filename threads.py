import threading as t
import os
def job1():
    l.acquire()
    print "reading from file",os.getpid()
    print "message from job1 is ",msg[0]
    l.release()
def job2():
    print "calculate some data",os.getpid()
def job3():
    print "reading data from user",os.getpid()
def job4():
    l.acquire()
    msg.append("Hi from job4")
    print "writing to file",os.getpid()
    l.release()

    
#to avoid recursion of main
if __name__ == "__main__":
    print "Main ",os.getpid()
    msg=[]
    l=t.Lock()
    p1=t.Thread(target=job1, args=())
    p2=t.Thread(target=job2())
    p3=t.Thread(target=job3())
    p4=t.Thread(target=job4())
    
    p4.start()
    p2.start()
    p3.start()
    p1.start()
    #join will make the main proscess wait till all processes complete
    p4.join()
    p2.join()
    p3.join()
    p1.join()

    
