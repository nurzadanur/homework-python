class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation


    def introduce(self):
        print(
            f'Привет! Меня зовут {self.name}, я родился в {self.birth_date},по профессии {self.occupation},')
#я одноклассник Нурзады мы учились в {self.group_name}, я друг Нурзады мое хобби это{self.hobby}')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super ().__init__(name, birth_date, occupation)
        self.group_name = group_name


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super ().__init__(name, birth_date, occupation)
        self.hobby = hobby


classmate1 = Classmate( "Аман", "15.09.2000", "юрист", "А" )
classmate1.introduce()
print(f"я одноклассник Нурзады мы учились в {self.group_name} классе")

friend1 = friend1(name="Алмаз", birth_date = "11.03.2001",  occupation ="пилот", hobby ="скаскалолазание")
friend1.introduce()
print(f"я друг Нурзады мое хобби это{self.hobby}")