import pprint


# file = open('lesson.txt', 'r')
# file_content = file.read()
# print(file_content)
# file.close()


# try:
#     file = open("test.txt", 'r') # r - это режим чтения
#     contents = file.read()
#     print(contents)
# except Exception as e:
#     print(e)


# try:
#     file = open("lesson.txt", 'w') # w - это режим записи
#     file.write("hello world")
#     file.close()
# except Exception as e:
#     print(e)


# try:
#     file = open("lesson.txt", 'a') # a - это режим дозаписи
#     file.write("hello world 2")
#     file.close()
# except Exception as e:
#     print(e)


# file = open('lesson.txt', 'r')
# content = file.read()
# file.close()
# print(type(content))
# print(content)
# print("----" * 20)
#
#
# file = open('lesson.txt', 'r')
# lines = file.readlines()
# file.close()
# print(type(lines))
# print(lines)
# print("----" * 20)
#
#
# file = open('lesson.txt', 'r')
# lines = file.readline(10)
# file.close()
# print(type(lines))
# print(lines)
# print("----" * 20)


# with open('lesson.txt', 'r') as f:
#     content = f.read()
#     for line in content:
#         print(line)
#     pprint.pprint(content)


# with open('lesson.txt', 'r') as f:
#     content = f.readlines()
#     print(content)
    # for line in content:
    #     print(line)
    # pprint.pprint(content)


# with open('test.txt', 'w') as f:
#     nums = [i for i in range(20)]
#     for num in nums:
#         f.write(str(num))


# with open('lesson.txt', 'r') as f:
#     a = f.readline()
#     print(a)
#     b = f.readline()
#     print(b)
#     c = f.readline()
#     print(c)


# nums = [str(i) for i in range(1, 101)]
# a = {"a" : "1", "b" : "2", "c" : "3"}
# with open('test.txt', 'w') as f:
#     for k, v in a.items():
#         f.write(f"{k}: {v}\n")


# nums = [str(i) for i in range(1, 101)]
# with open('test.txt', 'w') as f:
#     for num in nums:
#         f.write(num + '\n')


# def string_(a: str):
#     try:
#         if type(a) == str:
#             return a
#     except TypeError:
#         return f"{a} is not a string"