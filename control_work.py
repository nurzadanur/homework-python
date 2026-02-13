class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным.")

    def make_sound(self):
        return "какой звук издает животн?"


class Dog(Animal):
    def make_sound(self):
        return "ГАВ ГАВ!"


class Cat(Animal):
    def make_sound(self):
        return "МЯУ МЯУ!"

dog = Dog("Шарик", 3)

cat = Cat("Муся", 2)
print(f"{dog.get_name()}, говорит {dog.make_sound()}")
print(f"{cat.get_name()}, говорит {cat.make_sound()}")

dog.set_age(5)
cat.set_age(4)

print(f"{dog.get_name()} сейчас {dog.get_age()} лет")
print(f"{cat.get_name()} сейчас {cat.get_age()} лет")



