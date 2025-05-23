from dbus import ValidationException


# def hello():
#     pass
#
# def goodbye():
#     pass
#
# def goodbye2():
#     pass
#
# try:
#     hello()
#     goodbye()
#     goodbye2()
# except ValueError:
#     print("That's not a number")
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except TypeError:
#     print("That's not a number")
# except NameError:
#     print("That's not a number")
# except SyntaxError:
#     print("That's not a number")
# except IndexError:
#     print("That's not a number")

# alias --> as

# def hello(a: int, b: int):
#     try:
#         return a / b
#     except Exception as e:
#         print(f"ERROR : {e}")


# hello("a", 555)


# try:
#     x = int(input("Type a number: "))
#     y = int(input("Type a number: "))
#     result = x / y
# except ZeroDivisionError:
#     print("You can't divide by zero")
# else:
#     print(f"Выполнился блок else: {result}")
# finally:
#     print("Этот блок выполняется всегда.")


# class TooYoung(Exception):
#     pass
#
# class MyValueError(ValueError):
#     pass
#
#
# def register(age: int):
#     if age < 18:
#         raise TooYoung("You are young")
#     else:
#         print(age)
# #
# #
# #
# # register(15)
#
# try:
#     x = int(input("Type a number: "))
#     if x != 200:
#         raise MyValueError("MY text")
# except IndexError as e:
#     print("IndexError")


# try:
#     pass
# except Exception as e:
# def login(username, password):
#     try:
#         user = check_user_exists(username)
#         if user is None:
#             raise ValidationException("Пользовтеля нет в базе данных")
#         pwd = check_password(username, password)
#         if password != pwd:
#             raise ValidationException("<UNK> <UNK> <UNK> <UNK> <UNK>")



# try:
#     request = "some_address.com"
#     response = request.status
#     if response.status != 200:
#         raise ValidationException("Invalid response")
#
# except Exception as e:
#     print(e)
