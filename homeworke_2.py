class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation


    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f"работаю {self.occupation}."
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        print(f"Я одноклассник и учусь в группе {self.group_name}.")
        #print(
            #f"Привет, меня зовут {self.name}, "
            #f"я одноклассник, учусь в группе {self.group_name}, "
            #f"я родился {self.birth_date}, "
            #f"работаю {self.occupation}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print(f"Я друг. Моё хобби — {self.hobby}.")
        #print(
            #f"Привет, меня зовут {self.name}, "
            #f"я друг, "
            #f"я родился {self.birth_date}, "
            #f"работаю {self.occupation}, "
            #f"моё хобби — {self.hobby}.")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Наше общее воспоминание — {self.shared_memory}.")


classmate1 = Classmate("Аман", "15.09.2000", "юрист", "А")
classmate2 = Classmate("Бектур", "10.05.2001", "экономист", "Б")

friend1 = Friend("Алмаз", "11.03.2001", "пилот", "скалолазание")
friend2 = Friend("Нурсултан", "20.07.2000", "дизайнер", "рисование")

best_friend1 = BestFriend("Алина", "05.02.2001", "программист", "фотография", "поездка на Иссык-Куль")


#classmate1.introduce()
#classmate2.introduce()

#friend1.introduce()
#friend2.introduce()

people = [classmate1, classmate2, friend1, friend2, best_friend1]
for person in people:
    person.introduce()

