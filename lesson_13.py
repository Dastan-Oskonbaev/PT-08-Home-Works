

# def add_(a, b): # Обычная функция
#     return a + b

# a = lambda x, y: x + y #

# a(2, 3)

# a = lambda x: x *2
#
# b = a(5)
# print(b)

# a = lambda x: x ** x
#
# print(a(2))

# even = lambda x: x % 2 == 0
# print(even(3))

# a = lambda x, y: x if x > y else y
#
# print(a(12, 24))

# words = ['apple', 'banana', 'apricot', 'kiwi']

# sort = lambda x: sorted(x)
#
# print(sort(words))

# sort = lambda x: sorted(x[::-1])

# print(sorted(words, key=lambda x: x[-1]))
# print(sorted(words, key=lambda x: len(x)))

# def multiplier(n):
#     return lambda x: x * n
#
# a = multiplier(3)
#
# print(a(5))

# words = ['apple', 'banana', 'apricot', 'kiwi']
#
# def upper_(x):
#     return x.upper()
#
# b = map(upper_, words)
#
# a = map(lambda x: x.upper(), words)
#
#
#
# print(list(a))
# print(list(b))

# nums = [i for i in range(1 , 21)]
# a = map(lambda x: x * 2, nums)
#
# print(list(a))

# nums = [i for i in range(1 , 21)]
#
# def sort_(x):
#     if x % 2 == 0:
#         return x
#
# b = filter(sort_, nums)
#
# a = filter(lambda x: x % 2 == 0, nums)
#
#
# print(list(a))
# print(list(b))


# words = ['apple', 'banana', 'apricot', 'kiwi']
#
#
# a = filter(lambda x: len(x) > 5, words)
#
# print(list(a))

# nums = [i for i in range(1 , 21)]
# a = map(lambda x: x * 85, nums)

# words = ['apple', 'banana', 'apricot', 'kiwi', 'carrot', 'pineapple', 'potato']
# print(list(filter(lambda w: w.startswith("p"), words)))
# print(list(filter(lambda w: "a" in w, words)))

# nums = [i for i in range(1 , 21)]
#
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, nums))))

# words = ['apple', '', 'banana', " ", 'apricot', 'kiwi', 'carrot', "", 'pineapple', 'potato']
#
# # print(list(filter(lambda x: x.replace(" ", ''), words)))
#
# print(list(map(lambda x: x[0], filter(lambda d: d != '' and d != " ", words))))


# prices = [10.5, 20, 5.99] # ➜ ["Цена: 10.5", "Цена: 20.0", "Цена: 5.99"]

# print(list(map(lambda x: "price:" + str(x), map(lambda x: float(x), prices))))


# Оставить только строки, в которых больше 1 слова
# phrases = ["hello world", "hi", "good morning", "yo"] # ➜ ["hello world", "good morning"]
#
# a = filter(lambda x: len(x.split()) > 1, phrases)
#
# print(list(a))
#
# print(phrases[0].split())

