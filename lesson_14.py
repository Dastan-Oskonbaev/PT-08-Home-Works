# def hello():
#     print("Hello World")
#
#
# hello()
import time
from random import randint

# def outer():
#     def inner():
#         print("inner")
#     return inner()
#
#
# outer()


# def my_decorator(func):
#     def wrapper():
#         print('Before')
#         func()
#         print('After')
#     return wrapper
#
#
# @my_decorator
# def hello():
#     print('Hello')
#
#
# hello()
#
#
# @my_decorator
# def hello2():
#     print('Hello2')
#
#
# hello2()

# from datetime import datetime
#
#
# def decorator(func):
#     def wrapper():
#         print(f"Before {datetime.now()}")
#         func()
#         print(f"After {datetime.now()}")
#     return wrapper
#
#
# @decorator
# def hello():
#     print('Hello')
#
#
# hello()

# def counter(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         func()
#         count += 1
#         print(f"Функция {func.__name__} вызвалась {count} раз")
#     return wrapper
#
#
# @counter
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
#
#
# @counter
# def goodbye():
#     print("Goodbye")
#
#
# goodbye()
# goodbye()
# goodbye()
# goodbye()


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызов функции {func.__name__} с аргументами({args}, {kwargs})")
#         func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def hello(name):
#     print(f'Hello {name}')
#
#
# @decorator
# def goodbye(name, age, color):
#     print(f'Goodbye {name}, {age}, {color}')
#
# hello("Azat")
#
# goodbye("Bob", 20, color="red")

# Написать декоратор который считает время выполнения функции
# Написать функцию с помощью цикла for который создает список от 1 до 100
# Написать функцию с помощью генератора списков который создает список от 1 до 100

# from datetime import datetime
#
# def decorat(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         end = datetime.now()
#         print(end - start)
#     return wrapper
#
# @decorat
# def list_1():
#     my_list = []
#     for i in range(1000):
#         my_list.append(i)
#
#     return my_list
#
# @decorat
# def list_2():
#     return [i for i in range(1000)]
#
#
# @decorat
# def list_3():
#     return list(map(lambda x: x**2, range(1000)))


# list_1()
# list_2()
# list_3()

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#                 time.sleep(5)
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def hello():
#     print("Hello")
#
# hello()
#
# @repeat(5)
# def goodbye():
#     print("Goodbye")
#
#
# goodbye()
# print(f"Ломаем пентагон {randint(1, 20)} %\n % ")
# time.sleep(5)
# print(f"Ломаем пентагон {randint(1, 20)} %")
# time.sleep(5)
# print(f"Ломаем пентагон {randint(40, 60)} %")
# time.sleep(5)
# print(f"Ломаем пентагон {randint(60, 80)} %")
# time.sleep(5)
# print(f"Ломаем пентагон {randint(80, 99)} %")
# time.sleep(5)
# print(f"Взломали")


# import random
# import string
#
# def generate_password(length: int) -> str:
#     if length < 4:
#         raise ValueError("Пароль должен быть длиной минимум 4 символа")
#
#     chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choices(chars, k=length))
#     return password
#
# # Пример использования:
# length = int(input("Введите длину пароля: "))
# print("Сгенерированный пароль:", generate_password(length))


