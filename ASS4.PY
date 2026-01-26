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










# from abc import ABC, abstractmethod

# class vehicle(ABC):
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model=model
#     @abstractmethod
#     def details(self):
#         pass

# class bike(vehicle):
#     def __init__(self, brand, model,cc):
#         super().__init__(brand, model)
#         self.cc=cc
#     def details(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Engine: {self.cc}cc")

# class car(vehicle):
#     def __init__(self, brand, model,seats):
#         super().__init__(brand, model)
#         self.seats=seats
#     def details(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Engine: {self.seats}seats")

# vehicle1 = bike("honda", 3, 500)
# vehicle2 = car("honda", 5, 4)

# vehicle1.details()












# from abc import ABC, abstractmethod

# class employee(ABC):
#     def __init__ (self,hours=0, cph=0 ):
#         self.hours=hours
#         self.cph=cph

#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class parttime(employee):
#     def __init__(self, hours, cph):
#         super().__init__(hours, cph)

#     def calculate_salary(self):
#         print(self.cph*self.hours)
    
# class internship(employee):
#     def __init__(self, cph):
#         super().__init__(cph=cph)

#     def calculate_salary(self):
#         print(self.cph)
    
# class fulltime(employee):
#     def __init__(self, cph):
#         super().__init__(cph=cph)

#     def calculate_salary(self):
#         print(self.cph)
    
# person1=parttime(13, 24)
# person2=fulltime(23_000)
# person3=internship(1500)
# person1.calculate_salary()
# person2.calculate_salary()
# person3.calculate_salary()
















# class person:
#     name=0
#     age=0
#     adr=0

#     def __init__(self, name, age=None , adr=None):
#         self.name=name
#         self.age=age
#         self.adr=adr
    
# person1=person("mani")
# person2=person("HN", 23)
# person3=person("FHG",  45, "sri ram nagar")
# print(person1.name, person1.age, person1.adr)
# print(person2.name, person2.age, person2.adr)
# print(person3.name, person3.age, person3.adr)










# class play:
#     count=0
#     def __init__(self, name,level):
#         self.name=name
#         self.level = level
#         self.count+=1
#     def get_count(self):
#         print(self.count)

# player1=play("mani", 1)
# print(player1.name, player1.level)
# player1.get_count()














# class Herbivore:
#     def eat_plants(self):
#         print("Eats plants")
# class Omnivore:
#     def eat_both(self):
#         print("Eats both plants and meat")
# class Carnivore:
#     def eat_meat(self):
#         print("Eats meat")
# class bear (Herbivore,Omnivore, Carnivore):
#     def identity(self):
#         print("I am a Bear")
    
# b=bear()
# b.eat_both()
# b.eat_meat()
# b.eat_plants()