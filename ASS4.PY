# class bankaccount:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number=account_number
#         self.owner_name= owner_name
#         self._balance=balance
#     def get_balance(self):
#         print(f"balance of user is {self._balance}") 
#     def set_balance(self, new_balance):
#         self._balance= new_balance
#         print(f"balance of user is {self._balance}")
#     def get_wit(self, amount):
#         self._balance-=amount
#         print(f"balance of user is {self._balance}")

# user1=bankaccount("123", "mani", "24_000")
# user2=bankaccount("124", "teja", "1_000")

# print(user2)
# print(user1.account_number, user1.owner_name)
# user1.get_balance()
# user1.set_balance(34000)
# user1.get_wit(4000)









# class book:
#     count=0
#     def __init__(self, name, author, lor):
#         self.name=name
#         self.author=author
#         self.lor=[lor]
#         book.count+=1
#     def add_review(self, new_review):
#         self.lor.append(new_review)
#         print("review updated")
#     # @classmethod
#     def review_count(self):
#         print("total reviews:", len(self.lor))
#     def display_reviews(self):
#         for r in self.lor:
#             print(r)


# book1=book("jungle", "mani", "must to read")
# book2=book("jungle", "mani", "must to read")
# print(book1.name, book1.author, book1.lor)
# book1.review_count()
# book1.add_review("superbook")
# book1.add_review("supeok")
# book1.display_reviews()







# class student:
#     def __init__(self, name, roll, marks):
#         if marks >=0: 
#             self.__marks=marks
#         else:
#             print("invalid details")
#         if name!= "": 
#             self.__name=name
#         else:
#             print("invalid details")
#         if roll >=1 and roll<=100:
#             self.__roll=roll
#         else:
#             print("invalid details")

#     def set_details(self, new_name, new_roll, new_marks):
#         if new_marks >=0: 
#             self.__marks=new_marks
#         else:
#             print("invalid details") 
#         if new_name!= "": 
#             self.__name=new_name
#         else:
#             print("invalid details")
#         if new_roll >=1 and new_roll<=100:
#             self.__roll=new_roll
#         else:
#             print("invalid details") 

#     def get_name(self):
#         print(self.__name)
#     def get_roll(self):
#         print(self.__roll)
#     def get_marks(self):
#         print(self.__marks)
#     def get_att(self):
#         print(f"name is {self.__name} and roll number is {self.__roll} and secured marks are : {self.__marks}")
    
# stu1=student("mani", 3, 45)
# stu2=student("", 345,-12)
# stu1.get_att()
# stu1.get_marks()
# stu1.get_name()
# stu1.get_roll()
# stu1.set_details("mani", 3, 43)
# stu1.get_att()









# class shapes:
#     def __init__ (self, area):

#         print(area)

# class triangle(shapes):
#     def __init__(self, b, h):
#         bh=1/2*h*b
#         self.b=b
#         self.h=h
#         super().__init__(bh)
# class circle(shapes):
#     def __init__(self, r):
#         tr=3.14 * r**2
#         self.r=r
#         super().__init__(tr) 
# class rectangle(shapes):
#     def __init__(self, b, h):
#         bh=h*b
#         self.b=b
#         self.h=h
#         super().__init__(bh)

# shape1=circle(20)
# shape2=triangle(2,3)
# shape3=rectangle(2,3)











