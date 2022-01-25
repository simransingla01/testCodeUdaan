import abc
class PurchaserServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getPurchaser(self):
        pass