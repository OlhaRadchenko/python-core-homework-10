from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
       def __init__(self, value):
        if self.is_valid_phone(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number")

    def is_valid_phone(self, value):
        return isinstance(value, str) and len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone.value)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                self.phones[i].validate(new_phone)
                break

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Приклад використання
address_book = AddressBook()
record1 = Record("John Doe")
record1.add_phone("1234567890")
record1.add_phone("9876543210")

record2 = Record("Jane Smith")
record2.add_phone("5555555555")

address_book.add_record(record1)
address_book.add_record(record2)

print(address_book.find("John Doe"))
print(address_book.find("Jane Smith"))

record1.edit_phone("1234567890", "9999999999")
print(address_book.find("John Doe"))

record2.remove_phone(record2.find_phone("5555555555"))
print(address_book.find("Jane Smith"))
