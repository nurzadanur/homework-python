from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date =  datetime.strptime(birth_date, "%d.%m.%Y")
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education
    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.__birth_date.year

        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
            age -= 1
        return age

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. "
              f"мне {self.age} лет "
              f"Моя профессия {self.occupation}. "
              f"У меня {education} высшее образование.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        #education = "есть" if self.higher_education else "нет"
        print(#f"Привет, меня зовут {self.name}. "
              #f"Моя профессия {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group_name}."
             #f"У меня {education} высшее образование."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        #education = "есть" if self.higher_education else "нет"
        print(#f"Привет, меня зовут {self.name}. "
              #f"Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. "
              #f"У меня {education} высшее образование."
        )

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Наше общее воспоминание — {self.shared_memory}.")


classmate1 = Classmate("Аман", "15.09.2000", "юрист", True, "А")
classmate2 = Classmate("Бектур", "10.05.2001", "экономист", True, "Б")

friend1 = Friend("Алмаз", "11.03.2001", "пилот", True, "скалолазание")
friend2 = Friend("Нурсултан", "20.07.2000", "дизайнер", False, "рисование")

best_friend1 = BestFriend("Алина", "05.02.2001", "программист", True, "фотография", "поездка на Иссык-Куль")


people = [classmate1, classmate2, friend1, friend2, best_friend1]
for person in people:
    person.introduce()

