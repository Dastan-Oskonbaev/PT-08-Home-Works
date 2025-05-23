

# class Bird:
#     def fly(self):
#         print("Bird fly")
#
#
# class Plane:
#     def fly(self):
#         print("Plane fly")
#
#
#
# b = Bird()
# p = Plane()
#
# b.fly()
# p.fly()

#
# class CreditCard:
#     def __init__(self, credit_amount, credit_currency):
#         self.credit_amount = credit_amount
#         self.credit_currency = credit_currency
#
#     def transaction(self, summ):
#         self.credit_amount -= summ
#
#
# class MobilePayment:
#     def __init__(self, mobile_number, card_number, amount):
#         self.mobile_number = mobile_number
#         self.card_number = card_number
#         self.amount = amount
#
#
#     def transaction(self, summ):
#         self.amount -= summ
#
# mobile = MobilePayment("+996770767661", "123456789", 50000)
# credit = CreditCard(10000, "USD")
#
#
# mobile.transaction(1000)
# credit.transaction(1000)


class BankAccount:
    def __init__(self, card_number, balance, cvv):
        self.card_number = card_number # public
        self._balance = balance  # protected
        self.__cvv = cvv # private

    def get_cvv(self, role):
        if role != "admin":
            raise ValueError("Role must be 'admin'")
        else:
            return self.__cvv

    def set_cvv(self, cvv, role):
        if role != "admin":
            raise ValueError("Role must be 'admin'")
        else:
            self.__cvv = cvv


    @property
    def aaa(self):
        return self.__cvv

    @aaa.setter
    def aaa(self, cvv):
        self.__cvv = cvv


aza = BankAccount('123456', '10000', 123)

print(aza.aaa)
aza.aaa = 222
print(aza.aaa)
# print(aza.card_number)
#
# print(aza._balance)
#
# print(aza._BankAccount__cvv)

# print(aza.__cvv)

# print(aza.balance)
# print(aza.get_cvv("admin"))
# aza.set_cvv(222, "admin")
# print(aza.get_cvv("admin"))