from multiprocessing import Process, Lock
import time
__author__ = 'coconaut'


# the with statement will acquire mutex and release when finished
def do_something(mutex, data):
    print "starting: %i" % data
    with mutex:
        print "Do some stuff: %i" % data
        time.sleep(1)


# this should never release the mutex and cause a deadlock
def deadlock(mutex, data):
    print "starting: %i" % data
    mutex.acquire()
    print "Don't some stuff: %i" % data
    time.sleep(1)


# runner: starts up processes and passes lock, injectable target function
def runner(name, func):
    print "Running %s..." % name
    mutex = Lock()
    for i in range(0, 10):
        p = Process(target=func, args=(mutex, i))
        p.start()


if __name__ == '__main__':
    runner("release", do_something)
    runner("deadlock", deadlock)


