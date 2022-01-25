# from udaantest.service.purchaserserviceinterface import PurchaserServiceInterface
# from udaantest.module.purchaser import Purchaser
# from udaantest.service.sellerservice import sellerService
# from udaantest.service.sellerserviceinterface import SellerServiceInterface
# from udaantest.module.seller import Seller
#
# def purchaserService(PurchaserServiceInterface):
#     purchaser = Purchaser()
#     purchaserDict = {}
#     def getSeller(self,id,name):
#         purchaser.getId(id)
#         purchaser.getName(name)
#         self.__init__.purchaserDict['id']=purchaser
#         return purchaserDict
#
#     user = sellerService(1, 'abc', 200, ['abc', 'cdf', 'efg', 'hij'])
    # add products to cart

def buy(product_list, product_id):
    product_list = []
    product_id = None
    print("Please add products to cart: ")
    product_list.append(input('product_id'))
    return product_list
    #
    # deal_time = {'abc': 10, 'cdf': 20, 'efg': 30, 'hij':40}
    # def deal(self,deal_time,productList):
    #     for i in range(Seller.getproductList().productList):
    #         if productList[i] < deal_time[productList['i']]:
    #             print("Deal claimed")
    #
    #         else:
    #             print("Item not available")
b = buy(['abc', 'cdf', 'efg', 'hij'],12)
print(b)
