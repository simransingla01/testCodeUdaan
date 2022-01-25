import abc
class SellerServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getSeller(self):
        pass