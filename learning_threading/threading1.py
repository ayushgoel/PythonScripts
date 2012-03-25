#!/usr/bin/env python

import time
import thread

def myfunction(string, sleeptime, max_count, *args):

    counter = 0
    while counter < max_count:
        print "{}. {}".format(counter, string)
        counter += 1
        time.sleep(sleeptime) #sleep for a specified amount of time.
        

if __name__=="__main__":

    print "thread Started : {}".format(thread.start_new_thread(myfunction,("Thread No:1", 2, 10)))
##    thread.exit_thread
##
    while 1:
        pass
