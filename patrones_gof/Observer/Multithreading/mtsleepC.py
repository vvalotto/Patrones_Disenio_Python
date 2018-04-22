import threading
from time import sleep, ctime

loops = [10,2,5]

class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('start loop', nloop,'  0 at:', ctime())
    sleep(nsec)
    print('loop ', nloop, ' done at:', ctime())

def main():
    print('startind at:', ctime())
    threads =[]
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]),
                              loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('todo terminido en:', ctime())

if __name__ == "__main__":
    main()