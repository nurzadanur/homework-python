class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

@property
    def birth_date(self):
        return self.__birth_date

@property
    def age(self):
    birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
    today = datetime.today()
    return today.year - birth.year - (
        (today.month, today.day) < (birth.month, birth.day)
        )
@property
    def occupation(self):
        return self.__occupation

@property
    def higher_education(self):
        return self.__higher_education



    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(
            f'меня зовут {self.name},
            f'по профессии {self.occupation}, '
            f'высшего образования {education}')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(
            f'меня зовут {self.name},
            f'моя профессии {self.occupation}, '
            f' у меня {education} высшее образование'
            f"Я учился с Нурзадой в группе {self.group_name}.")



class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(
            f'меня зовут {self.name},
            f'моя профессии {self.occupation}, '
            f'у меня {education} высшее образование'
            f"мое хобби {self.hobby}.")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(
            f'меня зовут {self.name},
            f'моя профессии {self.occupation}, '
            f'у меня {education} высшее образование'
            f"мое хобби {self.hobby}."
            f"Наше общее воспоминание — {self.shared_memory}.")


classmate1 = Classmate("Аман", "15.09.2000", "юрист", "есть", "A")
classmate2 = Classmate("Бектур", "10.05.2001", "экономист", "есть", "B")

friend1 = Friend("Алмаз", "11.03.2001", "пилот", "есть", "скалолазание")
friend2 = Friend("Нурсултан", "20.07.2000", "дизайнер", "нет", "рисование")

best_friend1 = BestFriend("Алина", "05.02.2001", "программист", "фотография", "поездка на Иссык-Куль")




people = [classmate1, classmate2, friend1, friend2, best_friend1]
for person in people:
    person.introduce()



    # Изменение приватных атрибутов через сеттеры
    dog.set_name("Max")
    dog.set_age(4)
    cat.set_name("Luna")
    cat.set_age(3)

    # Проверка изменений
    print(f"{dog.get_name()} is {dog.get_age()} years old and says: {dog.make_sound()}")
    print(f"{cat.get_name()} is {cat.get_age()} years old and says: {cat.make_sound()}")



cat.set_age(2)
print(cat.get_age())

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Свойство name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Свойство age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print("Возраст не может быть отрицательным.")

    # Метод для демонстрации полиморфизма
    def make_sound(self):
        return "Some generic animal sound"

# Класс-наследник Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Класс-наследник Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Создание объектов
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

# Вывод звуков животных
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")

# Изменение атрибутов через свойства
dog.name = "Max"
dog.age = 4
cat.name = "Luna"
cat.age = 3

# Проверка изменений
print(f"{dog.name} is {dog.age} years old and says: {dog.make_sound()}")
print(f"{cat.name} is {cat.age} years old and says: {cat.make_sound()}")










