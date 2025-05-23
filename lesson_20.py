

# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def speak(self):
#         print(f'{self.name} says: {self.color}')
#
#
# class Dog(Animal):
#     def __init__(self, age, name, color):
#         super().__init__(name, color)
#         self.age = age
#
#     def speak(self):
#         print(f'{self.name} says: {self.age} years old')
#
#
#
# animal  = Animal('Animal', 'green')
# print(animal.name)
#
#
# dog = Dog('12', "Dog", "Red")
# print(dog.age, dog.name, dog.color)
#
# animal.speak()
# dog.speak()


# class Shape:
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
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#
#     def area(self):
#         return  3.14 * (self.radius ** 2)
#
#
# circle = Circle(2)
# print(isinstance(circle, Shape))


# class Computer:
#     class CPU:
#         def info(self):
#             return "INTEL CORE I7"
#
#
# cpu = Computer.CPU()
#
# print(cpu.info())


# class Flyer:
#     def fly(self):
#         return 'flying'
#
#
# class Walker:
#     def walk(self):
#         return 'walking'
#
#
#
# class Bird(Flyer, Walker):
#     pass
#
# bird = Bird()
# print(bird.fly())
# print(bird.walk())


# class Player:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#     def take_damage(self, damage):
#         self.hp -= damage
#
# class Mage(Player):
#     def __init__(self, name, hp, mana):
#         super().__init__(name, hp)
#         self.mana = mana
#
#
#     def cast_spell(self, target):
#         damage = self.mana * 0.5
#         if self.mana <= 0:
#             raise Exception("You can't cast spell")
#         else:
#             self.mana -= 20
#             target.take_damage(damage)
#         return self.mana
#
# mage = Mage("Gendalf", 100, 100)
# ogr = Player("Ogr", 100)
#
# mage.cast_spell(ogr)
# print(ogr.hp)
# mage.cast_spell(ogr)
#
# print(ogr.hp)


class User:
    def __init__(self, username):
        self.username = username


    def role(self):
        return "user"


class Admin(User):
    def __init__(self, username, permissions):
        super().__init__(username)
        self.permissions = permissions


    def role(self):
        return "admin"


class Company(User):
    def __init__(self, username, company_name):
        super().__init__(username)
        self.company_name = company_name


    def role(self):
        return "company"


p = User("dastan")
c = Company("dastan", "dastan's company")
a = Admin(p.username, "admin's permissions")

print(a.role())
print(p.role())
print(c.role())