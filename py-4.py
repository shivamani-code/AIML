# class stuent:
#     clas="mani"
#     def __init_subclass__(cls):
#         pass

# stu=stuent()
# print(stu)










# class laptops:
#     brand="hp"  #class
#     def __init__(self, ram, space, price):
#         self.space=space
#         self.ram=ram
#         self.price=price
#     def get_price(self): #instence
#         self.price
#     @classmethod
#     def get_brand_type(cls):
#         print(f"brand of the laptop is {cls.brand}") #class
#     @staticmethod
#     def discount(price, discount):
#         final_price=price - (discount*price)/100
#         print(f"discounted price is {final_price}") #static


# print("welcome to data base of laptop(hp)")
# lap1=laptops("16gb", "1tb", "1lakh")
# lap2=laptops("8gb", "2tb", "2lakh")
# lap3=laptops("32gb", "3tb", "3lakh")

# print(lap2)
# print(lap1)
# print(lap3)
# print(lap1.get_price)
# lap1.get_brand_type()
# lap1.discount(40_000, 34)












# class product_store:
#     count=0
#     def __init__(self, name , price):
#         self.name=name
#         self.price=price
#         product_store.count+=1

#     def get_info(self):
#         print(f"{self.name} is of cost {self.price}")

#     @staticmethod
#     def discount(price, discount):
#         final_price=price - (discount*price)/100
#         print(f"the price after discount {final_price} ")

#     def get_count(cls):
#         print(f"total products listed are {cls.count}")

# prd1=product_store("laptop", "40_000")
# prd2=product_store("phone", "20_000")
# prd3=product_store("watch", "1_000")


# print("welcome to product store")
# print(prd1)
# print(prd2)
# print(prd3)
# prd1.get_info()
# product_store.discount(20_00_00, 43)










