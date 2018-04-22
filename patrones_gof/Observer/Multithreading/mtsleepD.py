import threading
from time import sleep, ctime

loops = (10, 2, 5)

class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
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
        t = MyThread(loop, (i, loops[i]),
                            loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('todo terminido en:', ctime())

if __name__ == "__main__":
    main()