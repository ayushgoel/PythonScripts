#Fibonacci threader

import time, thread, threading

def fib(n):
    a, b = 0, 1
    while a<n:
        yield a
        a, b = b, a+b

		
def get_fibs(n):
    for i in fib(n):
        print "Number generated {}".format(i)
        time.sleep(0.1)
    thread.exit_thread()

if __name__ == '__main__':

    n = thread.start_new_thread(get_fibs, (100,))

    ## Won't work since the thread is still
    ## running and is still not in the dict
    ## containing all the running thread names
    for i in threading.enumerate():
        print i.ident, n
        if i.ident == n:
            print i.name, i.isAlive()
