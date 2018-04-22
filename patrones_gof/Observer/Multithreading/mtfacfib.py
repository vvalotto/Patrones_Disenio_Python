from Multithreading.my_thread import MyThread
from time import ctime, sleep

def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return fib(x - 2) + fib(x - 1)

def fac(x):
    sleep(0.1)
    if x < 2 : return 1
    return x * fac(x - 1)

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return x + sum(x - 1)

funcs = [fib, fac, sum]

n = 12

def main():
    nfuncs = range(len(funcs))

    print('*** Thread Unico')
    for i in nfuncs:
        print('Inicio', funcs[i].__name__, 'en: ', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finalizo en: ', ctime())

    print('*** Thread Multiples')
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i], (n,),
                    funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].get_result())

    print('todo terminado')

if __name__ == "__main__":
    main()
