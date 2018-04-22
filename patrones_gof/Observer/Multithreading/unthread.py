from time import sleep, ctime

def loop0():
    print('starr loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:'), ctime()

def loop1():
    print('starr loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:'), ctime()

def main():
    print('Starting at:', ctime())
    loop0()
    loop1()
    print('all DONeE at:', ctime())

if __name__ == "__main__":
    main()
