import abc

class AbstractNetwork(abc.ABC):
    @property
    @abc.abstractmethod
    def verbose_name(self):
        pass
    
    @property
    @abc.abstractmethod
    def active(self):
        pass

    @property
    @abc.abstractmethod
    def iin_range(self):
        pass
    
    @property
    @abc.abstractmethod
    def length(self):
        pass
    
    @property
    @abc.abstractmethod
    def validation(self):
        pass
    