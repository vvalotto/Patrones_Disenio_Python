
from abc import ABCMeta, abstractmethod

import random

class AbstractSubject(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def sort(self, reverse=False):
        pass


class RealSubject(AbstractSubject):

    def __init__(self):
        self.digits = []

        for i in range(1000000):
            self.digits.append(random.random())

    def sort(self, reverse=False):
        self.digits.sort()

        if reverse:
            self.digits.reverse()


class Proxy(AbstractSubject):

    reference_count = 0

    def __init__(self):

        if not getattr(self.__class__, 'cached_object', None):
            self.__class__.cached_object = RealSubject()
            print('Created new Object')
        else:
            print('Using cached Object')

        self.__class__.reference_count += 1

        print('Count of reference = ', self.__class__.reference_count)

    def sort(self, reverse=False):

        print('Called sort method with args:')
        print(locals().items())
        self.__class__.cached_object.sort(reverse=reverse)

    def __del__(self):
        self.__class__.reference_count -= 1

        if self.__class__.reference_count ==0:
            print('Number of reference_count is 0. Deleting cached object...')
            del self.__class__.cached_object

        print('Deleted Object. Count of Objects =', self.__class__.reference_count)

if __name__ == '__main__':
    proxy1 = Proxy()
    print()

    proxy2 = Proxy()
    print()

    proxy3 = Proxy()
    print()

    proxy1.sort(reverse=True)

    print()
    del proxy2

    print('los objetos se borran cuando el programa termina')