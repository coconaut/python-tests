from multiprocessing import Process, Lock
import time
__author__ = 'coconaut'


# set up the conditions
names = ["Kant", "Marx", "Nietzsche", "Spinoza", "Socrates"]
num_philosophers = len(names)


# forks are Locks
forks = [Lock() for i in range(num_philosophers)]


# a philosopher is its own process
class Philosopher(Process):
    def __init__(self, name, index):
        # set name - note: don't call the property 'name' as this will be overridden
        # when you init the base class Process
        self.philosopher_name = name

        # find fork indexes
        right_fork_index = index
        left_fork_index = (index - 1) if (index > 0) else (num_philosophers - 1)

        # set priority -> this will prevent the deadlock.
        # Also, need to set Locks in constructor, as the global array won't be accessible in the separate process
        self.first_fork = forks[min(right_fork_index, left_fork_index)]
        self.second_fork = forks[max(right_fork_index, left_fork_index)]

        # initialize the base Process
        Process.__init__(self)

    def run(self):
        # will run on Process start. Idea is to acquire both forks, eat, release.
        while True:
            # need a better log queue as the statements overlap eventually...
            # although, it does sort of illustrate concurrency...
            print "%s is thinking\n" % self.philosopher_name
            with self.first_fork:
                with self.second_fork:
                    print "%s is eating\n" % self.philosopher_name
                    time.sleep(2)

if __name__ == '__main__':

    # create Philosophers
    philosophers = []
    for i in range(num_philosophers):
        philosophers.append(Philosopher(names[i], i))

    # start them and observe
    # the philosophers can't all eat at once due to the locks
    # but no total deadlock due to the prioritization
    for philosopher in philosophers:
        philosopher.start()

