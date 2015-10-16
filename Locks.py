from multiprocessing import Process, Lock
import time
__author__ = 'coconaut'


# the with statement will acquire mutex and release when finished
def do_something(mutex, data):
    with mutex:
        print "Do some stuff: %i" % data
        time.sleep(1)


# this should never release the mutex and cause a deadlock
def deadlock(mutex, data):
    mutex.acquire()
    print "Don't some stuff: %i" % data
    time.sleep(1)


# run the releasing function - should print all 10 in any order
def run_do_something():
    print "Running release..."
    mutex = Lock()
    for i in range(0, 10):
        p = Process(target=do_something, args=(mutex, i))
        p.start()


# run the deadlock function - should lock forever after first process
def run_deadlock():
    print "Running deadlock..."
    mutex = Lock()
    for i in range(0, 10):
        p = Process(target=deadlock, args=(mutex, i))
        p.start()


if __name__ == '__main__':
    run_do_something()
    run_deadlock()


