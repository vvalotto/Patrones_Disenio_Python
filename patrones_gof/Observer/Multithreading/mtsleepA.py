import threading
from time import sleep, ctime

def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    t1 = threading.Thread(target=loop0)
    t2 = threading.Thread(target=loop1)
    print('Starting at:', ctime())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('all DONE at:', ctime())

if __name__ == "__main__":
    main()
