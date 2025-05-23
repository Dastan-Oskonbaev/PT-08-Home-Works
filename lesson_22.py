from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height


# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
#     @abstractmethod
#     def walk(self):
#         pass
#
#
#
# class Dog(Animal):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
#     def eat(self):
#         print('Dog eats')
#
#
#     def make_sound(self):
#         print('Dog makes sound')
#
#
#     def walk(self):
#         print('Dog walks')


# class BancAccount:
#     def __init__(self, card_number, balance, cvv):
#         self.card_number = card_number
#         self._balance = balance
#         self.__cvv = cvv
#
#     def get_cvv(self):
#         return self.__cvv
#
#     @property
#     def aaa(self):
#         return self.__cvv
#
#     @aaa.setter
#     def aaa(self, cvv):
#         self.__cvv = cvv


# b = BancAccount('123456', 10000, '123456')
# # print(b.card_number)
# # print(b._balance)
# # print(b.get_cvv())
#
# print(b.aaa)
#
# b.aaa = 222
#
# print(b.aaa)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __str__(self):
#         return f"{self.name}"
#
#
#     def __repr__(self):
#         return f"USER: name = {self.name}, age = {self.age}"
#
#
# p = Person("John", 36)
#
# print(p)
#
# print([p])


# class Book:
#     def __init__(self, pages):
#         # self.title = title
#         # self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f'{self.pages}'
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
#     def __mul__(self, other): # *
#         pass
#
#     def __truediv__(self, other): # /
#         pass
#
#     def __sub__(self, other): # -
#         pass
#
#     def __pow__(self, other): # **
#         pass
#
#     def __floordiv__(self, other): # //
#         pass
#
#     def __mod__(self, other): # %
#         pass
#
#
#     def __iadd__(self, other):
#         self.pages += other.pages
#         return self
#
#     def __isub__(self, other): # -
#         self.pages -= other.pages
#         return self
#
#
#     def __len__(self):
#         return self.pages
#
#
#     def __eq__(self, other):
#         return self.pages == other.pages
#
#
#     def __lt__(self, other):
#         return self.pages < other.pages
#
#     def __le__(self, other):
#         return self.pages <= other.pages
#
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __ge__(self, other):
#         return self.pages >= other.pages
#
#
#     def __ne__(self, other):
#         return self.pages != other.pages
#
#
#
# b1 = Book(20)
# b2 = Book(10)
#
# print(b1 + b2)
#
# # print(b1 > b2)
# # print(b1 >= b2)
# # print(b1 < b2)
# # print(b1 <= b2)
# # print(b1 == b2)
# print(b2 != b1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


    def __repr__(self):
        return f"class Person: name={self.name}, age={self.age}"


p = Person("John", 36)

print(p)
print([p])



