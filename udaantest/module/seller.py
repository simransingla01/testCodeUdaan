class Seller(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.price = None
        self.productList = []
    def setId(self,id):
        self.id = id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setPrice(self, price):
        self.price = price
    def getPrice(self):
        return self.price
    def setproductList(self, productList):
        self.productList = productList
    def getproductList(self):
        return self.productList