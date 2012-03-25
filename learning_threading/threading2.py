#!/usr/bin/env python

import time
import thread

## Implementing consumer-producer problem using threads and locks

product = []

def producer(lock, produce_time, lim, *args):
    pr_val = 0
    while True:
        print "Producing.."
        time.sleep(produce_time)
        print "Produced {}".format(pr_val)

        lock.acquire_lock()
        print "P: Lock ACK"
        product.append(pr_val)
        print "Added product {}".format(pr_val)
        lock.release_lock()
        print "P: Release ACK"
        
        pr_val += 1
        if pr_val > lim:
            break

def consumer(lock, consume_time, waiting_time, lim, *args):
    con_val = 0
    got_product = False

    while True:

        lock.acquire_lock()
        print "C: Lock ACK"
        try:
            con_val = product.pop()
            print "Retrieved value {}".format(con_val)
            got_product = True
        except IndexError:
            print "No produce!"
            got_product = False
        lock.release_lock()
        print "C: Release ACK"

        if got_product:
            print "Consuming.. {}".format(con_val)
            time.sleep(consume_time)
        else:
            print "Waiting for produce"
            time.sleep(waiting_time)
            
        if con_val == lim:
            break
        
if __name__=="__main__":

    lock=thread.allocate_lock()
    max_produce = 3
    thread.start_new_thread(producer,(lock, 1, max_produce))
    thread.start_new_thread(consumer,(lock, 2, 1, max_produce))

    # Required for commandline output
    while 1:
        pass
