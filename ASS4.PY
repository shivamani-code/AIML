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



