from abc import ABCMeta, abstractmethod

class Ruteable(metaclass=ABCMeta):

    @abstractmethod
    def rutear(self):
        pass