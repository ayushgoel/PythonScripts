#!/usr/bin/env python

#Let us profile code which uses threads
import time
import timeit
from threading import Thread

class MyThread(Thread):

    def __init__(self, bignum = 1000):

        Thread.__init__(self)
        self.bignum = bignum
    
    def run(self):

        for l in range(10):
            for k in range(self.bignum):
                res=0
                for i in range(self.bignum):
                    res+=1


def myadd_nothread(bignum = 1000):

    for l in range(10):
        for k in range(bignum):
            res=0
            for i in range(bignum):
                res+=1

    for l in range(10):
        for k in range(bignum):
            res=0
            for i in range(bignum):
                res+=1

def thread_test(bignum = 1000):
    #We create 2 Thread objects  for the 2 threads.
    thr1=MyThread(bignum)
    thr2=MyThread(bignum)

    thr1.start()
    thr2.start()

    thr1.join()
    thr2.join()
    

def test():

    bignum=1000
    
    a = timeit.Timer(thread_test)
    print "Running two threads"
    print a.timeit(1)

    a = timeit.Timer(myadd_nothread)
    print "Running without threads"
    print a.timeit(1)

if __name__=="__main__":


    import profile
    profile.run('test()')
