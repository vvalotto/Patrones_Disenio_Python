import threading
from time import sleep, ctime

loops = [10,2,5]

def loop(nloop, nsec):
    print('start loop', nloop,'  0 at:', ctime())
    sleep(nsec)
    print('loop ', nloop, ' done at:', ctime())

def main():
    print('startind at:', ctime())
    threads =[]
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('todo terminido en:', ctime())

if __name__ == "__main__":
    main()

