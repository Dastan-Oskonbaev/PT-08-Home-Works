from random import randint

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
# aza = Human("Aza", 18)
# akchayim = Human("Achayim", 22)
#
# print(aza.name)
# print(aza.age)

# class Marker:
#     # size = "Round"
#
#     def __init__(self, color, brand="green"):
#         self.color = color
#         self.brand = brand
#         self.size = randint(1, 10)
#
#
#     def draw(self):
#         print(f" {self.brand} Marker is drawing")
#
#
# green_marker = Marker("green", "Green")
#
# red_marker = Marker("red", "RED")
#
# blue_marker = Marker("blue", "Blue")
#
# blue_marker.brand = "RED"

# print(blue_marker.size)
# print(green_marker.size)
# print(red_marker.size)

# blue_marker.draw()


# class Car:
#     def __init__(self, name):
#         self.name = name
#         self.engine = False
#
#
#     def check_engine(self):
#         if self.engine:
#             print("Engine is running")
#         else:
#             print("Engine is not running")
#
#
#     def start(self):
#         self.engine = True
#
#
#     def stop(self):
#         self.engine = False
#
#
# toyota = Car("Toyota")
# toyota.check_engine()
# toyota.start()
# toyota.check_engine()
# toyota.stop()
# toyota.check_engine()

class BankAccount:

    def __init__(self, owner, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.transfers = []

    def check_balance(self):
       print(f" {self.account_number}'s balance = {self.balance}")


    def cash_in(self, amount):
        self.balance += amount
        self.transfers.append(f"Cash in {amount}$")
        print(self.balance)


    def cash_out(self, amount):
        self.balance -= amount
        self.transfers.append(f"Cash out {amount}$")
        print(self.balance)


    def transactions_history(self):
        print(f" {self.account_number}'s transactions history = {self.transfers}")


dastans_account = BankAccount("Dastan",131546849)
dastans_account.check_balance()
dastans_account.cash_in(100)
dastans_account.check_balance()
dastans_account.cash_out(50)
dastans_account.check_balance()

dastans_account.transactions_history()


