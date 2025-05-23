

# class MyMyclass:
#
#     @staticmethod
#     def hello():
#         print("Hello")
#


# class MyMath:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# a = MyMath(1, 2)
#
# print(MyMath.add(1, 2))


# class Weather:
#     def __init__(self, gradus, wind):
#         self.gradus = gradus
#         self.wind = wind
#
#     def get_weather(self):
#         if self.gradus > 25:
#             return "GOOD Weather"
#         elif self.gradus < 25:
#             return "BAD Weather"
#
#     @staticmethod
#     def f_to_celsius(farenheit):
#         return (farenheit - 32) * 5/9
#
#
#
#
# print(Weather.f_to_celsius(500))

# from abc import ABC, abstractmethod
#
#
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
#
#     @staticmethod
#     def area(width, height):
#         return width * height
#
#
# print(Rectangle.area(10, 5))


# def area(width: int, height: int):
#     return width + height
#
#
# a = "ssdfsdf"
# b = 50
#
#
# print(area(a,b))


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     @classmethod
#     def from_dict(cls, data: dict):
#         return cls(data['name'], data['age'])
#
#     def __str__(self):
#         return f'User({self.name}, {self.age})'
#
#
# u1 = User("John", 32)
#
# user_data = {'name': 'Azat', 'age': 20}
#
# u2 = User.from_dict(user_data)
#
# print(u2)

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
#     @classmethod
#     def convert_to_som(cls, name, price_in_usd):
#         price = price_in_usd * 87.3
#         return cls(name, price)
#
#     def __str__(self):
#         return f"{self.name} -- {self.price}"
#
# a = Item.convert_to_som("A", 100)
# print(a)

"""
Single Responsibility Principle
Open Closed Principle
Liskov Substitutional Principle
Interface Segregation Principle
Dependency Inversion Principle
"""

# class Report:
#     def __int__(self, data):
#         self.data = data
#
#
# class FileSaver:
#     @staticmethod
#     def save(data):
#         with open('report.txt', 'a') as file:
#             file.write(data)


#Open Closed Principle

# class Payment:
#     def pay(self, method):
#         if method == "cash":
#             print("Payment method  cash called")
#         elif method == "aplle_pay":
#             print("Payment method  aplle pay")
#         elif method == "credit_card":
#             print("Payment method  credit card")

# class Payment:
#     def pay(self):
#         print("Payment method called")
#
#
# class ApplePayment(Payment):
#     def pay(self):
#         print("Apple Payment method called")
#
#
# class CreditCard(Payment):
#     def pay(self):
#         print("Credit Card Payment method called")


#Liskov Substitutional Principle

# class Bird:
#     def move(self):
#         print("Bird fly")
#
#
# class Pinguin(Bird):
#     def move(self):
#         print("Pinguin moving")


# class Plane:
#     def fly(self):
#         print("Fly")
#
#
# class Tank(Plane):
#     def fly(self):
#         print("Fly")
#
#     def shoot(self):
#         print("Shooting target")


#Interface Segration Principle

class Worker:
    def eat(self):
        print("I am eating...")

    def work(self):
        print("I am working...")

    def sleep(self):
        print("I am sleeping...")


class Robot:
    # def eat(self):
    #     print("I am eating...")

    def work(self):
        print("I am working...")

    # def sleep(self):
    #     print("I am sleeping...")



