class Car:
    num = 0
    color = ""
    site = 0
    brand = ""
    price = ""

    def run(self):
        print(self.color, "的车准备着")


car = Car()
car.num = 4
car.color = "红色"
car.site = 4
car.price = 10000000000
car.brand = "benchi"

car.run()


class Person:
    name = ""
    age = 0
    birthday = ""
    sex = ""
    skin_color = ""
    hair_color = ""
    eye_color = ""

    def eat(self):
        print(1)

    def drink(self):
        print(2)

    def sleep(self):
        print(3)


person = Person()
person.name = "威乐"
person.eat()
person.drink()
person.sleep()
