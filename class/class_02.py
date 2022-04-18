"""
Created by hu-jinwen on 2022/4/17
"""


class Cat:
    def eat(self):
        print("%s吃饭" % self.name)

    def drink(self):
        print("%s喝水" % self.name)


tom = Cat()
tom.name = "Tom"

tom.eat()
tom.drink()
print(tom)


lazy_cat = Cat()
lazy_cat.name = "Lazy_cat"

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
