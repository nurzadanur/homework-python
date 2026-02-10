class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(f'меня зовут {self.name}, я родился в {self.birth_date},по профессии {self.occupation}, высшего образования {education}')


person_aman = Person( name= 'Аман', birth_date= '11.05.2003',
                       occupation= 'бармен', higher_education= False)
print(person_aman.name)
person_aman.introduce()


person_alina = Person( name= 'Алина', birth_date= '19.03.2002',
                        occupation= 'учитель', higher_education= True)
person_alina.introduce()
