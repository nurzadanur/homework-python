class Contact:
    def __init__(self, name, phone_number, contact_id):
        self.name = name
        self.phone_number = phone_number
        self.id = contact_id
    @classmethod
    def validate_phone_number(cls, phone_number):
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр!")
        cls.last_id += 1
        new_contact = Contact(name, phone_number, cls.last_id)
        cls.all_contacts.append(new_contact)

    @classmethod
    def remove_contact(cls, contact_id):
        cls.all_contacts = [contact for contact in cls.all_contacts if contact.id != contact_id]


print(ContactList.all_contacts)

ContactList.add_contact("Вася Пупкин", "0700001000")
ContactList.add_contact("Виктор Цой", "0500003056")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)

ContactList.remove_contact(1)

print("После удаления:")
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)
