#
#
# class Product:
#     def __init__(self, name, price_som):
#         self.name = name
#         self.price_som = price_som
#
#     @classmethod
#     def to_som(cls, name, price):
#         price_som = price * 87.5
#         return cls(name, price_som)
#
#
# class User:
#     def __init__(self, username, avatar):
#         self.username = username
#         self.avatar = avatar
#
#     def __str__(self):
#         return f"{self.username} {self.avatar}"
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data['username'], data['avatar'])
#
#     @classmethod
#     def from_string(cls, some_string):
#         user = some_string.split(",")
#         return cls(user[0], user[1])
#
#
# users = {
#     "username": "user_1",
#     "avatar": "user_avatar"
# }
#
# users_2 = "user_2,user_2_avatar"
# user_1 = User.from_dict(users)
#
# user_2 = User.from_string(users_2)
# print(user_1)
# print(user_2)


import requests

from bs4 import BeautifulSoup

# url = "https://new.technodom.kg/category/fototehnika-i-kvadrokoptery"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, "lxml")
#
# products = soup.find_all("div", class_="common__recommendations__list__item one-four")
#
# for product in products:
#     title = product.find("div", class_="common__recommendations__list__item__title").text
#     price = product.find("div", class_="common__recommendations__list__item__price").text
#     image = product.find("a")['data-background-image']
#     print(title)
#     print(price)
#     print(image)
#     print("----"*20)

# from bs4 import BeautifulSoup
#
# response = requests.get("https://www.tazabek.kg/")
#
# soup = BeautifulSoup(response.text, "lxml")
#
# news = soup.find_all("div", class_="lenta-row")
#
# urls = []
# for i in news:
#     date = i.find("div", class_="lenta-row-date").text
#     title = i.find("div", class_="lenta-row-title").text
#     news_url = i.find("a")["href"]
#     normal_url = "https://www.tazabek.kg/" + news_url
#     urls.append(normal_url)
#     # print(date)
#     # print(title)
#     # print(normal_url)
#
#
# for url in urls:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "lxml")
#     news = soup.find("h2", class_="title")
#     if news:
#         title = news.text
#         article = soup.find("div", class_="article-text").text
#         print(title)
#         print(article)
#     else:
#         continue

# class Movie:
#     def __init__(self, title, genre, age, image):
#         self.title = title
#         self.genre = genre
#         self.age = age
#         self.image = image
#
#     def __str__(self):
#         propusk = "-----" * 20
#         return (f"Название: {self.title}\n Жанр:{self.genre}\n Возрастное ограничение: {self.age}\n "
#                 f"Ссылка: {self.image}\n {propusk}\n")
#
#     @classmethod
#     def from_parser(cls, title, genre, age, image):
#         return cls(title, genre, age, image)
#
#
#
# import requests
#
# from bs4  import BeautifulSoup
#
# url = "https://manascinema.com"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, "lxml")
#
# products = soup.find_all("a", class_="creation-item")
#
# for product in products:
#     age = product.find("div", class_="age").text
#     title = product.find("div", class_="creation-title").text
#     genre = product.find("div", class_="creation-info").text
#     normal_genre = genre.replace(" ", "")
#     image = product.find("img")["src"]
#     final_image =  url + image
#
#     p = Movie.from_parser(title, normal_genre, age, final_image)
#
#     with open("movies.txt", "a", encoding='utf-8') as file:
#         file.write(p.__str__())

import requests

from bs4  import BeautifulSoup


# class Game:
#     def __init__(self, name, price, image):
#         self.name = name
#         self.price = price
#         self.image = image
#
#
#     @classmethod
#     def from_soup(cls, name, price, image):
#         return cls(name, price, image)
#
#     def __str__(self):
#         propusk = "-----" * 20
#         return (f"Название: {self.name}\n Цена:{self.price}\n"
#                 f"Ссылка: {self.image}\n {propusk}\n")

# class Product:
#     def __init__(self, name, price, image):
#         self.name = name
#         self.price = price
#         self.image = image
#
#
#     @classmethod
#     def from_soup(cls, name, price, image):
#         return cls(name, price, image)
#
#     def __str__(self):
#         propusk = "-----" * 20
#         return (f"Название и описание: {self.name}\n Цена:{self.price}\n"
#                 f"Ссылка: {self.image}\n {propusk}\n")
#
# for i in range (1, 11):
#     url = f"https://www.kivano.kg/elektronika?page={i}"
#
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "lxml")
#
#     items = soup.find_all("div", class_="item product_listbox oh")
#
#     for item in items:
#         name = item.find("div", class_="product_text pull-left").text
#         image = item.find("img")["src"]
#         price = item.find("div", class_="listbox_price text-center").text
#         normal_image = "https://www.kivano.kg" + image
#         product = Product.from_soup(name, price, image)
#         with open("kivano.txt", "a") as file:
#             file.write(product.__str__())

# print("!@#$%^&*(){}:;/?|,"*40)
print("-"*4096)